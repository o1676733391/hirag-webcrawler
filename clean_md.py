#!/usr/bin/env python3
import argparse
import re
from pathlib import Path

# Markdown links/images: [text](url) or ![alt](url)
# URL part allows escaped characters like \) that appear in crawled markdown.
_MD_LINK_RE = re.compile(r"!?\[[^\]]*\]\(((?:\\.|[^\\)])+)(?:\s+\"[^\"]*\")?\)")
# Autolink form: <https://...>
_AUTO_LINK_RE = re.compile(r"<([^>]+)>")
# Bare URLs for quick filtering when they appear alone in a line
_BARE_URL_RE = re.compile(r"\bhttps?://\S+\b", re.IGNORECASE)

_VIDEO_EXT_RE = re.compile(r"\.(mp4|webm|mov|m4v)(?:[?#].*)?$", re.IGNORECASE)


def _clean_url(url: str) -> str:
    u = url.strip().strip('"\'')
    if u.startswith("<") and u.endswith(">") and len(u) > 2:
        u = u[1:-1].strip()
    # Crawl markdown can escape parentheses in urls.
    u = u.replace(r"\(", "(").replace(r"\)", ")")
    return u


def _is_noise_url(url: str) -> bool:
    u = _clean_url(url).lower()
    return (
        u.startswith("data:")
        or u.startswith("javascript:")
        or _VIDEO_EXT_RE.search(u) is not None
    )


def _strip_noise_links_from_line(line: str) -> str:
    out = line

    # Remove markdown links/images that point to noise URLs.
    def _replace_md(match: re.Match[str]) -> str:
        target = match.group(1)
        return "" if _is_noise_url(target) else match.group(0)

    out = _MD_LINK_RE.sub(_replace_md, out)

    # Remove autolinks that point to noise URLs.
    def _replace_auto(match: re.Match[str]) -> str:
        target = match.group(1)
        return "" if _is_noise_url(target) else match.group(0)

    out = _AUTO_LINK_RE.sub(_replace_auto, out)

    # If a line is just punctuation after removal, drop it.
    if re.fullmatch(r"\s*[|>\-:.,/]*\s*", out):
        return ""

    return out.rstrip()


def clean_markdown_text(text: str) -> str:
    cleaned_lines: list[str] = []
    for raw_line in text.splitlines():
        line = raw_line.rstrip("\n")

        # Common video-player UI artifacts from crawler output.
        if re.fullmatch(r"\s*Video Player\s*", line, re.IGNORECASE):
            continue
        if re.fullmatch(r"\s*\d{1,2}:\d{2}\s*", line):
            continue
        if re.fullmatch(r"\s*[;:][)\]]\s*", line):
            continue

        # Drop html video/audio tags directly.
        if re.search(r"<\s*/?\s*(video|audio)\b", line, re.IGNORECASE):
            continue

        cleaned = _strip_noise_links_from_line(line)

        # Drop single bare noise URL line.
        stripped = cleaned.strip()
        if stripped:
            m = _BARE_URL_RE.fullmatch(stripped)
            if m and _is_noise_url(m.group(0)):
                continue

        if cleaned.strip() == "":
            # keep at most one blank line between blocks
            if cleaned_lines and cleaned_lines[-1] == "":
                continue
            cleaned_lines.append("")
            continue

        cleaned_lines.append(cleaned)

    # Remove leading/trailing blank lines for neat files.
    while cleaned_lines and cleaned_lines[0] == "":
        cleaned_lines.pop(0)
    while cleaned_lines and cleaned_lines[-1] == "":
        cleaned_lines.pop()

    return "\n".join(cleaned_lines) + "\n"


def _iter_md_files(source: Path):
    if source.is_file() and source.suffix.lower() == ".md":
        yield source
        return
    if source.is_dir():
        yield from source.rglob("*.md")


def run(source: Path, output: Path | None, in_place: bool) -> tuple[int, int]:
    files = list(_iter_md_files(source))
    if not files:
        return 0, 0

    changed = 0
    for src in files:
        before = src.read_text(encoding="utf-8", errors="ignore")
        after = clean_markdown_text(before)
        if after == before:
            continue

        changed += 1
        if in_place:
            src.write_text(after, encoding="utf-8", newline="\n")
        else:
            assert output is not None
            rel = src.relative_to(source if source.is_dir() else source.parent)
            dest = output / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(after, encoding="utf-8", newline="\n")

    return len(files), changed


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Remove markdown image/video/link noise (data: URIs, javascript:, video URLs)."
    )
    parser.add_argument("--source", required=True, help="Source markdown file or folder")
    parser.add_argument("--output", help="Output folder when not using --in-place")
    parser.add_argument("--in-place", action="store_true", help="Rewrite files in place")
    args = parser.parse_args()

    source = Path(args.source).resolve()
    if not source.exists():
        raise SystemExit(f"Source not found: {source}")

    if not args.in_place and not args.output:
        raise SystemExit("Provide --in-place or --output")

    output = Path(args.output).resolve() if args.output else None
    if output and not args.in_place:
        output.mkdir(parents=True, exist_ok=True)

    total, changed = run(source, output, args.in_place)
    mode = "in-place" if args.in_place else f"to {output}"
    print(f"Processed {total} markdown files ({changed} changed) {mode}.")


if __name__ == "__main__":
    main()
