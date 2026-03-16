"""html_to_md.py — Parse Figma-style HTML exports into GraphRAG-ready Markdown.

Designed to handle deeply nested "div soup" (e.g. Figma-exported pages) by
focusing on text content and relative nesting depth rather than class names.

Usage:
    python html_to_md.py --source html_pages --output md_parsed

Dependencies:
    pip install beautifulsoup4 lxml
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

from bs4 import BeautifulSoup, NavigableString, Tag

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

_NOISE_TAGS = frozenset(
    {"nav", "footer", "script", "style", "header", "noscript", "aside", "iframe"}
)

# CSS class fragments that signal UI chrome, not content
_NOISE_CLASS_RE = re.compile(
    r"\b(nav|menu|sidebar|footer|cookie|popup|modal|overlay|banner|breadcrumb|"
    r"toolbar|topbar|widget|advertisement|ad-)\b",
    re.I,
)

# Text patterns to silently discard (separators, legal boilerplate, skip links)
_SKIP_TEXT_RE = re.compile(
    r"^\s*$"
    r"|^[\|•·—–\-_=]+\s*$"
    r"|skip\s+to\s+(main\s+)?content"
    r"|copyright\s+\©"
    r"|all\s+rights\s+reserved",
    re.I,
)

# Heuristic max word/char count for a "title-like" string
_TITLE_MAX_WORDS = 9
_TITLE_MAX_CHARS = 110

# Detect strings that are clearly data values, not labels.
# Strings containing units, percentages, numbers, symbols → not a heading.
_DATA_VALUE_RE = re.compile(
    r"[\d%°±≤≥~+\-/<>]"         # numeric/symbol content
    r"|\b(ohm|hz|ma|mv|mw|µ|ppm|db|ms|ns|kg|mm|cm|°c|°f|fsr|dc|ac|rms)\b"
    r"|\bN/A\b"
    r"|\d+\s*[a-zA-Z]",          # digit immediately followed by unit letter
    re.I,
)


# ---------------------------------------------------------------------------
# Step 1 – Boilerplate Removal
# ---------------------------------------------------------------------------


def clean_html(soup: BeautifulSoup) -> BeautifulSoup:
    """
    Remove navigation, footers, scripts, styles and class-identified noise.
    Operates in-place on *soup* and also returns it.
    """
    # 1. Remove known noisy semantic tags.
    for tag in soup.find_all(_NOISE_TAGS):
        tag.decompose()

    # 2. Remove elements whose CSS classes suggest UI chrome.
    #    Iterate over a static list copy because decompose mutates the tree.
    for tag in list(soup.find_all(True, class_=True)):
        css = " ".join(tag.get("class", []))
        if _NOISE_CLASS_RE.search(css):
            tag.decompose()

    # 3. Remove elements hidden via inline styles.
    for tag in list(soup.find_all(style=True)):
        style = tag["style"].replace(" ", "").lower()
        if "display:none" in style or "visibility:hidden" in style:
            tag.decompose()

    # 4. Remove empty anchor decorations (icon-only links).
    for a in list(soup.find_all("a")):
        if not a.get_text(strip=True):
            a.decompose()

    return soup


# ---------------------------------------------------------------------------
# Step 2 – Low-level helpers for structure detection
# ---------------------------------------------------------------------------


def _own_text(tag: Tag) -> str:
    """Direct text nodes of *tag* only — excludes text inside child elements."""
    return " ".join(
        t.strip()
        for t in tag.children
        if isinstance(t, NavigableString) and t.strip()
    )


def _full_text(tag: Tag) -> str:
    """All visible text inside *tag*, whitespace-normalised."""
    return " ".join(tag.get_text(" ", strip=True).split())


def _tag_children(tag: Tag) -> list[Tag]:
    """Return only direct Tag children (skip NavigableString nodes)."""
    return [c for c in tag.children if isinstance(c, Tag)]


def _is_title_like(text: str) -> bool:
    """
    Heuristic: text is 'title-like' when it is short, contains no trailing
    period and does not look like a technical measurement value.
    """
    text = text.strip()
    if not text or text.endswith("."):
        return False
    if _DATA_VALUE_RE.search(text):
        return False
    word_count = len(text.split())
    return word_count <= _TITLE_MAX_WORDS and len(text) <= _TITLE_MAX_CHARS


def _heading_level(depth: int) -> int:
    """
    Map nesting depth to Markdown heading level (H1–H4).
    Top-level containers start at H2 so H1 is reserved for the page title.
    """
    return min(depth + 2, 4)


# ---------------------------------------------------------------------------
# Step 3 – Grid / key-value detection
# ---------------------------------------------------------------------------


def _all_children_are_leaves(tag: Tag) -> bool:
    """True when every direct child Tag contains no further child Tags."""
    children = _tag_children(tag)
    return bool(children) and all(not _tag_children(c) for c in children)


def _uniform_column_count(children: list[Tag]) -> int | None:
    """
    If every child in *children* has the same non-zero number of sub-children,
    return that column count; otherwise return None.
    This signals a grid/table layout.
    """
    if not children:
        return None
    counts = [len(_tag_children(c)) for c in children]
    if counts[0] > 0 and len(set(counts)) == 1:
        return counts[0]
    return None


def _try_kv_flat(children: list[Tag]) -> list[dict] | None:
    """
    Detect alternating label/value pairs in a *flat* list of leaf children.
    Pattern:  [label0, value0, label1, value1, …]
    Returns a list of 'kv' nodes on success, None otherwise.
    """
    if len(children) < 2 or len(children) % 2 != 0:
        return None
    pairs: list[dict] = []
    for i in range(0, len(children), 2):
        key_txt = _full_text(children[i])
        val_txt = _full_text(children[i + 1])
        # Both sides must have content; key must look like a label.
        if not key_txt or not val_txt:
            return None
        if not _is_title_like(key_txt):
            return None
        pairs.append({"type": "kv", "key": key_txt.rstrip(":"), "value": val_txt})
    return pairs


def _try_kv_rows(children: list[Tag], col_count: int) -> list[dict] | None:
    """
    Detect a 2-column grid where each row is a (label, value) pair.
    Each child in *children* must have exactly *col_count* == 2 sub-children
    and the first column of every row must be title-like.
    """
    if col_count != 2:
        return None
    pairs: list[dict] = []
    for row in children:
        cols = _tag_children(row)
        if len(cols) != 2:
            return None
        key_txt = _full_text(cols[0])
        val_txt = _full_text(cols[1])
        if not key_txt or not val_txt:
            return None
        if not _is_title_like(key_txt):
            return None
        pairs.append({"type": "kv", "key": key_txt.rstrip(":"), "value": val_txt})
    return pairs if pairs else None


def _build_table(children: list[Tag], col_count: int) -> dict | None:
    """
    Build a 'table' node from a grid container.
    The first child row is used as column headers.
    """
    if col_count < 2 or len(children) < 2:
        return None
    def row_cells(child: Tag) -> list[str]:
        return [_full_text(c) for c in _tag_children(child)]

    headers = row_cells(children[0])
    rows = [row_cells(c) for c in children[1:] if row_cells(c)]
    if not rows:
        return None
    return {"type": "table", "headers": headers, "rows": rows}


# ---------------------------------------------------------------------------
# Step 4 – Recursive structure extractor
# ---------------------------------------------------------------------------


def extract_structure(tag: Tag, depth: int = 0) -> list[dict]:
    """
    Recursively walk *tag* and return a flat list of typed node dicts.

    Node types emitted:
      heading  – {'type': 'heading', 'level': int, 'text': str}
      para     – {'type': 'para',    'text': str}
      kv       – {'type': 'kv',      'key': str, 'value': str}
      table    – {'type': 'table',   'headers': list[str], 'rows': list[list[str]]}
      list     – {'type': 'list',    'items': list[str]}
      hr       – {'type': 'hr'}

    Nesting depth drives heading level so that the deeper a "frame" is, the
    smaller the heading — mimicking a visual hierarchy even when class names
    are opaque Figma-generated tokens like 'frame-4291'.
    """
    nodes: list[dict] = []

    if not tag.get_text(strip=True):
        return nodes

    name: str = getattr(tag, "name", "") or ""

    # ---- Semantic HTML — handled directly, skip recursive descent ----------

    if name in ("h1", "h2", "h3", "h4", "h5", "h6"):
        text = _full_text(tag)
        if text:
            nodes.append({"type": "heading", "level": int(name[1]), "text": text})
        return nodes

    if name == "p":
        text = _full_text(tag)
        if text and not _SKIP_TEXT_RE.search(text):
            nodes.append({"type": "para", "text": text})
        return nodes

    if name in ("ul", "ol"):
        items = [_full_text(li) for li in tag.find_all("li", recursive=False)]
        items = [i for i in items if i]
        if items:
            nodes.append({"type": "list", "items": items})
        return nodes

    if name == "table":
        headers: list[str] = []
        rows: list[list[str]] = []
        thead = tag.find("thead")
        if thead:
            headers = [_full_text(th) for th in thead.find_all(["th", "td"])]
        for tr in tag.find_all("tr"):
            if tr.find_parent("thead"):
                continue
            cells = [_full_text(td) for td in tr.find_all(["td", "th"])]
            if cells:
                rows.append(cells)
        if rows:
            nodes.append({"type": "table", "headers": headers, "rows": rows})
        return nodes

    if name == "hr":
        nodes.append({"type": "hr"})
        return nodes

    # ---- Generic container (div, section, article, main, span …) ----------

    children = _tag_children(tag)
    own = _own_text(tag)

    # Emit own text before descending into children.
    if own and not _SKIP_TEXT_RE.search(own):
        if _is_title_like(own):
            nodes.append({"type": "heading", "level": _heading_level(depth), "text": own})
        else:
            nodes.append({"type": "para", "text": own})

    # Leaf node — tag has no child Tags, only text.
    if not children:
        return nodes  # own text already emitted above

    # ---- Strategy A: flat leaf children — alternating KV pairs ----------
    if _all_children_are_leaves(tag):
        kv = _try_kv_flat(children)
        if kv:
            nodes.extend(kv)
            return nodes

        # Not KV — emit as a bulleted list if all items are concise.
        texts = [_full_text(c) for c in children if _full_text(c)]
        if texts and all(len(t.split()) <= 20 for t in texts):
            nodes.append({"type": "list", "items": texts})
            return nodes

    # ---- Strategy B: uniform-column grid (rows each have n columns) ------
    col_count = _uniform_column_count(children)
    if col_count is not None:
        # 2-column grid: try label-value rows first.
        kv_rows = _try_kv_rows(children, col_count)
        if kv_rows:
            nodes.extend(kv_rows)
            return nodes

        # Multi-column grid with header row → Markdown table.
        table_node = _build_table(children, col_count)
        if table_node:
            nodes.append(table_node)
            return nodes

    # ---- Strategy C: mixed / deeply nested frames — recurse --------------
    for child in children:
        nodes.extend(extract_structure(child, depth + 1))

    return nodes


# ---------------------------------------------------------------------------
# Step 5 – Markdown rendering
# ---------------------------------------------------------------------------


def _md_table(headers: list[str], rows: list[list[str]]) -> str:
    """Render a GitHub-flavoured Markdown pipe table from raw cell data."""
    col_count = max(len(headers), max((len(r) for r in rows), default=0))
    if col_count == 0:
        return ""

    def pad(row: list[str], n: int) -> list[str]:
        return list(row) + [""] * (n - len(row))

    h = pad(headers, col_count) if headers else [""] * col_count
    sep = ["---"] * col_count
    lines = [
        "| " + " | ".join(h) + " |",
        "| " + " | ".join(sep) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(pad(row, col_count)) + " |")
    return "\n".join(lines)


def render_markdown(nodes: list[dict], title: str = "") -> str:
    """
    Convert a flat list of typed node dicts into a clean Markdown string.
    *title* is prepended as an H1 when provided.
    Technical values (units, measurements) are always kept on the same line
    as their key — the kv node format guarantees this.
    """
    parts: list[str] = []

    if title:
        parts.append(f"# {title}")

    for node in nodes:
        kind = node["type"]

        if kind == "heading":
            parts.append(f"{'#' * node['level']} {node['text']}")

        elif kind == "para":
            parts.append(node["text"])

        elif kind == "kv":
            # Key and value always on one line — preserves "100G Ohm", "+/-0.01% FSR".
            parts.append(f"**{node['key']}**: {node['value']}")

        elif kind == "list":
            parts.append("\n".join(f"- {item}" for item in node["items"]))

        elif kind == "table":
            tbl = _md_table(node["headers"], node["rows"])
            if tbl:
                parts.append(tbl)

        elif kind == "hr":
            parts.append("---")

    # Collapse runs of 3+ blank lines into exactly two.
    raw = "\n\n".join(p for p in parts if p.strip())
    raw = re.sub(r"\n{3,}", "\n\n", raw)
    return raw.strip()


# ---------------------------------------------------------------------------
# Step 6 – Single-file orchestration
# ---------------------------------------------------------------------------


def parse_html_file(html_path: Path) -> str:
    """
    Parse one HTML file into a Markdown string.

    Content root preference order (most-specific to least):
      1. <main>
      2. <article>
      3. <div id="content|main|app"> (regex)
      4. <body>
      5. root soup object
    """
    html = html_path.read_text(encoding="utf-8", errors="replace")
    soup = BeautifulSoup(html, "lxml")

    # Derive page title from <title> or first <h1> before cleaning.
    page_title = ""
    title_tag = soup.find("title")
    if title_tag:
        page_title = title_tag.get_text(strip=True)
    if not page_title:
        h1 = soup.find("h1")
        if h1:
            page_title = h1.get_text(strip=True)

    clean_html(soup)

    root: Tag = (
        soup.find("main")
        or soup.find("article")
        or soup.find("div", id=re.compile(r"^(content|main|app)$", re.I))
        or soup.body
        or soup
    )

    nodes = extract_structure(root, depth=0)
    return render_markdown(nodes, title=page_title)


# ---------------------------------------------------------------------------
# Step 7 – CLI entry point and batch processing
# ---------------------------------------------------------------------------


def configure_console_encoding() -> None:
    """Force UTF-8 stdout/stderr (mirrors parser.py – avoids Windows crash)."""
    os.environ.setdefault("PYTHONIOENCODING", "utf-8")
    try:
        if hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        if hasattr(sys.stderr, "reconfigure"):
            sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


def main() -> None:
    configure_console_encoding()

    ap = argparse.ArgumentParser(
        description=(
            "Parse Figma-style HTML files into clean, hierarchical Markdown "
            "optimised for GraphRAG ingestion."
        )
    )
    ap.add_argument(
        "--source",
        default="html_pages",
        help="Directory containing .html source files (searched recursively).",
    )
    ap.add_argument(
        "--output",
        default="md_parsed",
        help="Root directory for generated .md files.",
    )
    ap.add_argument(
        "--encoding",
        default="utf-8",
        help="Output file encoding (default: utf-8).",
    )
    args = ap.parse_args()

    source_dir = Path(args.source)
    output_dir = Path(args.output)

    if not source_dir.exists():
        raise FileNotFoundError(f"Source directory not found: {source_dir}")

    html_files = sorted(source_dir.rglob("*.html"))
    if not html_files:
        print(f"No .html files found under {source_dir}")
        return

    output_dir.mkdir(parents=True, exist_ok=True)

    ok = err = skipped = 0
    for html_path in html_files:
        try:
            md_text = parse_html_file(html_path)

            if not md_text.strip():
                print(f"[SKIP] {html_path} — no content extracted")
                skipped += 1
                continue

            # Mirror source directory tree in output.
            relative = html_path.relative_to(source_dir)
            out_path = output_dir / relative.with_suffix(".md")
            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_text(md_text, encoding=args.encoding)

            print(f"[OK]   {html_path} -> {out_path}")
            ok += 1
        except Exception as exc:
            print(f"[ERR]  {html_path}: {exc}")
            err += 1

    print(f"\nDone — {ok} converted, {skipped} skipped (empty), {err} failed.")
    print(f"Output: {output_dir.resolve()}")


if __name__ == "__main__":
    main()
