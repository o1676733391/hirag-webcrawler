from __future__ import annotations

import argparse
import asyncio
import csv
import os
import re
import sys
import time
from pathlib import Path
from urllib.parse import urlparse

from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from lxml import html as lxml_html

# Crawl4AI renders <button>/<a class="btn"> elements as "[ Label ](url)" —
# space-padded brackets are the tell-tale sign of a CTA button, not content.
_CTA_LINE_RE = re.compile(r"^\s*\[ [^\]]+ \]\([^)]+\)\s*$", re.MULTILINE)

# In-page anchor links in lists  e.g. "  * [Highlights](url#highlights)"
# These are always jump-nav, never real content.
_ANCHOR_NAV_ITEM_RE = re.compile(
	r"^\s{0,6}\*\s+\[[^\]]+\]\([^)]*#[^)\s]+\)\s*$", re.MULTILINE
)

_SLUG_TOKEN_RE = re.compile(r"[a-z0-9]+")
_HEADING_LINE_RE = re.compile(r"^(#{1,4})\s+(.+?)\s*$")
_STRIP_MARKUP_RE = re.compile(r"!?\[[^\]]*\]\([^)]+\)|[`*_>#]")
_SLUG_STOP = frozenset({"product", "products", "category", "tag", "page", "html"})
_SHORT_VALUE_LINE_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9%+\-./<>=~()\sx\"']*$")

_TABLE_DIV_XPATH = (
	"//div["
	"contains(translate(@class,'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'table') "
	"or contains(translate(@id,'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'table')"
	"]"
)
_TABLE_TOKEN_RE = re.compile(r"(?:^|[^a-z])table(?:[^a-z]|$)", re.IGNORECASE)


def _slug_tokens(url: str) -> set[str]:
	"""Extract meaningful tokens from the URL path for heading matching."""
	from urllib.parse import urlparse as _urlparse
	path = _urlparse(url).path
	tokens: list[str] = []
	for seg in path.split("/"):
		seg = seg.removesuffix(".html")
		tokens.extend(_SLUG_TOKEN_RE.findall(seg.lower()))
	return {t for t in tokens if t not in _SLUG_STOP}


def _find_content_start(lines: list[str], url: str) -> int:
	"""
	Return the index of the line where real page content begins.

	Strategy:
	  1. Match each heading line against URL slug tokens.
	     The heading whose text overlaps most with the URL slug is the
	     primary content heading — everything before it is site chrome.
	  2. If no URL-matched heading is found (score < 0.4), fall back to
	     the first H1 or H2 heading anywhere in the first 300 lines.
	  3. If still nothing, keep the full output (start at 0).
	"""
	url_tokens = _slug_tokens(url)

	best_idx = -1
	best_score = 0.0

	for i, line in enumerate(lines[:300]):
		m = _HEADING_LINE_RE.match(line.strip())
		if not m:
			continue
		if not url_tokens:
			# No URL tokens — accept first H1/H2 as content start.
			if len(m.group(1)) <= 2:
				return i
			continue
		# Score = fraction of URL tokens covered by heading words.
		heading_plain = _STRIP_MARKUP_RE.sub(" ", m.group(2))
		heading_tokens = set(_SLUG_TOKEN_RE.findall(heading_plain.lower()))
		overlap = len(url_tokens & heading_tokens)
		if overlap == 0:
			continue
		score = overlap / max(1, len(url_tokens))
		if score > best_score:
			best_score = score
			best_idx = i

	if best_score >= 0.4 and best_idx >= 0:
		return best_idx

	# Fallback: first H1 or H2 in the document.
	for i, line in enumerate(lines[:300]):
		m = _HEADING_LINE_RE.match(line.strip())
		if m and len(m.group(1)) <= 2:
			return i

	return 0


def slugify(value: str) -> str:
	"""Convert text to a safe filesystem slug."""
	value = value.strip().lower()
	value = re.sub(r"[^a-z0-9]+", "-", value)
	value = value.strip("-")
	return value or "untitled"


def read_links(file_path: Path) -> list[str]:
	"""Read URLs from a text file, skipping empty lines and comments."""
	lines = file_path.read_text(encoding="utf-8").splitlines()
	links: list[str] = []
	for line in lines:
		clean = line.strip().lstrip("\ufeff")
		if not clean or clean.startswith("#"):
			continue
		links.append(clean)
	return links


def configure_console_encoding() -> None:
	"""Force UTF-8 stdout/stderr to avoid Rich unicode crashes on Windows."""
	os.environ.setdefault("PYTHONIOENCODING", "utf-8")
	try:
		if hasattr(sys.stdout, "reconfigure"):
			sys.stdout.reconfigure(encoding="utf-8", errors="replace")
		if hasattr(sys.stderr, "reconfigure"):
			sys.stderr.reconfigure(encoding="utf-8", errors="replace")
	except Exception:
		# Keep crawler running even if reconfigure is not supported in this shell.
		pass


def build_output_path(output_root: Path, url: str) -> Path:
	"""
	Map URL path into nested directories:
	- / -> root/home.md
	- /product -> product/index.md
	- /product/item-a -> product/item-a.md
	- /a/b/c -> a/b/c.md
	"""
	parsed = urlparse(url)
	segments = [slugify(seg) for seg in parsed.path.split("/") if seg]

	if not segments:
		return output_root / "root" / "home.md"

	# Normalize a segment that looks like a web page file.
	if segments[-1].endswith("-html"):
		segments[-1] = segments[-1].removesuffix("-html")

	if parsed.path.endswith("/"):
		# Directory-style URL gets index.md.
		return output_root.joinpath(*segments) / "index.md"

	if len(segments) == 1:
		return output_root / segments[0] / "index.md"

	return output_root.joinpath(*segments[:-1]) / f"{segments[-1]}.md"


def pick_markdown(result: object) -> str:
	"""Extract markdown text from Crawl4AI result across possible API variants."""
	# Newer shape: result.markdown (str)
	markdown = getattr(result, "markdown", None)
	if isinstance(markdown, str) and markdown.strip():
		return markdown

	# Some versions expose markdown in markdown_v2 fields.
	markdown_v2 = getattr(result, "markdown_v2", None)
	if markdown_v2 is not None:
		raw = getattr(markdown_v2, "raw_markdown", None)
		if isinstance(raw, str) and raw.strip():
			return raw

		fit = getattr(markdown_v2, "fit_markdown", None)
		if isinstance(fit, str) and fit.strip():
			return fit

	return ""


def extract_table_like_div_html_blocks(page_html: str) -> list[str]:
	"""Return original HTML snippets for div tags whose class/id contains 'table'."""
	if not page_html.strip():
		return []

	try:
		doc = lxml_html.fromstring(page_html)
	except Exception:
		return []

	blocks: list[str] = []
	seen: set[str] = set()
	for node in doc.xpath(_TABLE_DIV_XPATH):
		cls = (node.get("class") or "").strip()
		nid = (node.get("id") or "").strip()
		probe = f"{cls} {nid}".lower()
		# Avoid false positives like "tabletPortrait".
		if "tablet" in probe:
			continue
		if not (_TABLE_TOKEN_RE.search(cls) or _TABLE_TOKEN_RE.search(nid)):
			continue
		try:
			block = lxml_html.tostring(node, encoding="unicode", pretty_print=True).strip()
		except Exception:
			continue
		if not block or block in seen:
			continue
		seen.add(block)
		blocks.append(block)

	return blocks


def _row_cells_from_tr(tr_node: object) -> list[str]:
	if not hasattr(tr_node, "xpath"):
		return []
	cells = tr_node.xpath("./th|./td")
	row: list[str] = []
	for cell in cells:
		text = " ".join(" ".join(cell.xpath(".//text()")).split())
		if text:
			row.append(text)
	return row


def _markdown_table_from_rows(rows: list[list[str]]) -> str:
	if not rows:
		return ""
	max_cols = max((len(r) for r in rows), default=0)
	if max_cols == 0:
		return ""

	if max_cols == 2:
		headers = ["Parameter", "Value"]
	elif max_cols == 3:
		headers = ["Parameter", "Sub-parameter", "Value"]
	else:
		headers = [f"Column {i}" for i in range(1, max_cols + 1)]

	lines = [
		"| " + " | ".join(headers) + " |",
		"| " + " | ".join(["---"] * len(headers)) + " |",
	]
	for row in rows:
		padded = row + [""] * (max_cols - len(row))
		lines.append("| " + " | ".join(padded) + " |")
	return "\n".join(lines)


def extract_markdown_tables_from_html(page_html: str) -> list[str]:
	"""Extract readable markdown tables from native HTML table/tr/td markup."""
	if not page_html.strip():
		return []

	try:
		doc = lxml_html.fromstring(page_html)
	except Exception:
		return []

	out: list[str] = []
	for table in doc.xpath("//table"):
		rows: list[list[str]] = []
		for tr in table.xpath(".//tr"):
			cells = _row_cells_from_tr(tr)
			if cells:
				rows.append(cells)

		md_table = _markdown_table_from_rows(rows)
		if md_table:
			out.append(md_table)
	return out


def replace_flattened_markdown_table_section(
	markdown: str,
	section_heading: str,
	replacement_table_md: str,
	replacement_heading: str,
) -> str:
	"""Replace a flattened section block with a parsed markdown table section."""
	if not replacement_table_md.strip():
		return markdown

	pattern = re.compile(
		rf"(?ms)^###\s+{re.escape(section_heading)}\s*\n.*?(?=^##\s|^###\s|\Z)"
	)
	new_block = f"### {replacement_heading}\n\n{replacement_table_md}\n"
	if pattern.search(markdown):
		return pattern.sub(new_block, markdown, count=1)
	return markdown


def _norm_cell_text(text: str) -> str:
	parts = [p.strip() for p in text.splitlines() if p.strip()]
	return " | ".join(parts)


def _row_cells_from_node(row_node: object) -> list[str]:
	if not hasattr(row_node, "xpath"):
		return []
	children = row_node.xpath("./div")
	if len(children) < 2:
		return []
	cells: list[str] = []
	for child in children:
		text = " ".join(" ".join(child.xpath(".//text()")).split())
		cell = _norm_cell_text(text)
		if cell:
			cells.append(cell)
	return cells


def build_readable_tables_from_html_blocks(html_blocks: list[str]) -> str:
	"""Convert extracted specification-table HTML blocks into readable markdown tables."""
	sections: list[str] = []

	for block in html_blocks:
		try:
			doc = lxml_html.fromstring(block)
		except Exception:
			continue

		table_nodes = doc.xpath(
			".//*["
			"contains(concat(' ', normalize-space(@class), ' '), ' specifications-table ') "
			"or contains(concat(' ', normalize-space(@class), ' '), ' temperature-chamber-table ')"
			"]"
		)
		for table in table_nodes:
			title = ""
			title_nodes = table.xpath(".//*[contains(@class,'battery-testing-cell')]/text()")
			if title_nodes:
				title = " ".join(" ".join(title_nodes).split())

			part_lines: list[str] = []
			if title:
				part_lines.append(f"### {title}")

			# Section blocks use wrappers that include one heading area and one rows area.
			section_nodes = table.xpath("./div/*[./div[contains(@class,'frame-1321315510')]]")
			for sec in section_nodes:
				name_text = " ".join(" ".join(sec.xpath("./div[1]//text()")).split())
				section_name = _norm_cell_text(name_text) or "Section"
				rows_wrap = sec.xpath("./div[contains(@class,'frame-1321315510')][1]")
				if not rows_wrap:
					continue

				rows: list[list[str]] = []
				max_cols = 0
				for row_node in rows_wrap[0].xpath("./div"):
					cells = _row_cells_from_node(row_node)
					if len(cells) < 2:
						continue
					rows.append(cells)
					max_cols = max(max_cols, len(cells))

				if not rows:
					continue

				headers = ["Parameter"] + [f"Value {i}" for i in range(1, max_cols)]
				part_lines.append(f"#### {section_name}")
				part_lines.append("| " + " | ".join(headers) + " |")
				part_lines.append("| " + " | ".join(["---"] * len(headers)) + " |")
				for row in rows:
					cells = row + [""] * (max_cols - len(row))
					part_lines.append("| " + " | ".join(cells) + " |")
				part_lines.append("")

			if part_lines:
				sections.append("\n".join(part_lines).strip())

	# Deduplicate repeated parsed sections.
	if not sections:
		return ""
	unique: list[str] = []
	seen: set[str] = set()
	for sec in sections:
		if sec in seen:
			continue
		seen.add(sec)
		unique.append(sec)
	return "\n\n".join(unique)


def replace_flattened_system_specs(markdown: str, parsed_tables: str) -> str:
	"""Replace flattened System Specifications section with parsed tables if present."""
	if not parsed_tables.strip():
		return markdown

	section = f"## System Specifications (Parsed from HTML)\n\n{parsed_tables}\n"
	pattern = re.compile(
		r"(?ms)^##\s+System Specifications\s*\n.*?(?=^##\s|\Z)"
	)
	if pattern.search(markdown):
		return pattern.sub(section, markdown, count=1)

	return f"{markdown}\n\n{section}".strip()


def clean_markdown_content(markdown: str, url: str = "") -> str:
	"""Remove site header/navbar/footer noise from crawled markdown."""
	if not markdown.strip():
		return ""

	lines = markdown.splitlines()

	# Skip everything before the primary content heading.
	start_idx = _find_content_start(lines, url)
	cleaned = lines[start_idx:]

	# Cut common footer markers if present.
	footer_markers = (
		"ARBIN-logo_white.svg",
		"Arbin Instruments. All Rights Reserved",
		"Terms & Conditions",
		"MITS accessibility statement",
		"Voluntary Product Accessibility Template",
	)

	end_idx = len(cleaned)
	for i, line in enumerate(cleaned):
		if any(marker in line for marker in footer_markers):
			end_idx = i
			break

	body = "\n".join(cleaned[:end_idx])

	# Strip CTA button lines ([ Download Brochure ](url)) and in-page anchor nav.
	body = _CTA_LINE_RE.sub("", body)
	body = _ANCHOR_NAV_ITEM_RE.sub("", body)

	# Collapse any runs of 3+ blank lines left by the removals.
	body = re.sub(r"\n{3,}", "\n\n", body).strip()
	return body


def looks_like_flattened_table(markdown: str) -> bool:
	"""Detect markdown sections that were flattened from a div-based table layout."""
	window = 0
	short_plain = 0
	numericish = 0

	def flush() -> bool:
		nonlocal window, short_plain, numericish
		matched = window >= 12 and short_plain >= 10 and numericish >= 6
		window = 0
		short_plain = 0
		numericish = 0
		return matched

	for raw_line in markdown.splitlines():
		line = raw_line.strip()
		if not line:
			if flush():
				return True
			continue
		if line.startswith(("#", "*", "-", ">")) or "](" in line:
			if flush():
				return True
			continue
		window += 1
		if len(line.split()) <= 4 and _SHORT_VALUE_LINE_RE.fullmatch(line):
			short_plain += 1
		if any(ch.isdigit() for ch in line):
			numericish += 1

	return flush()


def build_run_config() -> CrawlerRunConfig:
	"""Return the standard Crawl4AI run config for page rendering."""
	return CrawlerRunConfig(
		wait_until="networkidle",
		scan_full_page=True,
		delay_before_return_html=0.3,
		page_timeout=15000,
		excluded_tags=["script", "style", "noscript"],
		verbose=False,
	)


def build_run_config_from_args(args: argparse.Namespace) -> CrawlerRunConfig:
	"""Build Crawl4AI run config from CLI flags."""
	return CrawlerRunConfig(
		wait_until=args.wait_until,
		scan_full_page=args.scan_full_page,
		delay_before_return_html=args.delay_before_return_html,
		page_timeout=max(1000, args.page_timeout_ms),
		excluded_tags=["script", "style", "noscript"],
		verbose=False,
	)


def _fmt_seconds(value: float) -> str:
	"""Format elapsed time values for concise progress logs."""
	return f"{value:.2f}s"


async def crawl_and_export(
	links: list[str],
	output_root: Path,
	max_concurrency: int,
	retries: int,
	run_config: CrawlerRunConfig,
	request_timeout: float,
	table_processing: bool,
	append_table_div_html: bool,
) -> None:
	output_root.mkdir(parents=True, exist_ok=True)
	semaphore = asyncio.Semaphore(max_concurrency)

	success = 0
	failed = 0
	index_rows: list[tuple[str, str]] = []
	run_started = time.perf_counter()
	url_durations: list[float] = []

	print(f"[DEBUG] Starting crawl with {len(links)} links, max_concurrency={max_concurrency}", flush=True)

	async with AsyncWebCrawler(verbose=False) as crawler:
		print(f"[DEBUG] AsyncWebCrawler initialized", flush=True)

		async def process_url(url: str) -> None:
			nonlocal success, failed
			print(f"[DEBUG] Entering process_url for {url}", flush=True)
			url_started = time.perf_counter()
			print(f"[START] {url}")
			out_path = build_output_path(output_root, url)
			out_path.parent.mkdir(parents=True, exist_ok=True)

			print(f"[DEBUG] Waiting for semaphore slot for {url}", flush=True)
			async with semaphore:
				print(f"[DEBUG] Acquired semaphore for {url}", flush=True)
				last_error = "Unknown error"
				for attempt in range(1, retries + 1):
					attempt_started = time.perf_counter()
					try:
						print(f"[DEBUG] Starting fetch for {url} attempt {attempt}/{retries}", flush=True)
						fetch_started = time.perf_counter()
						result = await asyncio.wait_for(
							crawler.arun(url=url, config=run_config),
							timeout=max(1.0, request_timeout)
						)
						fetch_elapsed = time.perf_counter() - fetch_started
						print(
							f"[STEP] {url} attempt {attempt}/{retries} fetch+render: {_fmt_seconds(fetch_elapsed)}"
						)

						clean_started = time.perf_counter()
						raw_markdown = pick_markdown(result)
						raw_html = getattr(result, "html", "") or ""
						markdown = clean_markdown_content(raw_markdown, url=url)
						clean_elapsed = time.perf_counter() - clean_started
						print(f"[STEP] {url} markdown cleanup: {_fmt_seconds(clean_elapsed)}")

						if not markdown.strip():
							raise RuntimeError("No markdown content returned")

						table_started = time.perf_counter()
						if table_processing:
							html_tables = extract_markdown_tables_from_html(raw_html)
							if html_tables:
								# The largest HTML table is usually the full technical specifications grid.
								best_specs_table = max(html_tables, key=lambda t: t.count("\n"))
								markdown = replace_flattened_markdown_table_section(
									markdown=markdown,
									section_heading="Specifications",
									replacement_table_md=best_specs_table,
									replacement_heading="Specifications (Parsed from HTML table)",
								)
								print(f"[STEP] {url} native html tables parsed: {len(html_tables)}")

							table_div_html_blocks = extract_table_like_div_html_blocks(raw_html)
							if table_div_html_blocks:
								readable_tables = build_readable_tables_from_html_blocks(table_div_html_blocks)
								print(
									f"[STEP] {url} div-table blocks found: {len(table_div_html_blocks)}, parsed sections: {'yes' if readable_tables else 'no'}"
								)
								if readable_tables:
									markdown = replace_flattened_system_specs(markdown, readable_tables)
								if append_table_div_html:
									html_blocks = "\n\n".join(
										f"```html\n{block}\n```" for block in table_div_html_blocks
									)
									markdown = (
										f"{markdown}\n\n"
										f"## Table-like Div HTML (Original)\n\n"
										f"{html_blocks}"
									)
						table_elapsed = time.perf_counter() - table_started
						print(f"[STEP] {url} table processing total: {_fmt_seconds(table_elapsed)}")

						write_started = time.perf_counter()
						content = (
							f"# Source\n\n"
							f"- URL: {url}\n\n"
							f"# Content\n\n{markdown}\n"
						)
						out_path.write_text(content, encoding="utf-8")
						write_elapsed = time.perf_counter() - write_started
						rel_path = out_path.relative_to(output_root).as_posix()
						index_rows.append((url, rel_path))
						success += 1
						url_elapsed = time.perf_counter() - url_started
						url_durations.append(url_elapsed)
						done = success + failed
						print(
							f"[OK] {url} -> {out_path} | write: {_fmt_seconds(write_elapsed)} | total: {_fmt_seconds(url_elapsed)}"
						)
						print(f"[PROGRESS] {done}/{len(links)} completed")
						print(f"[DEBUG] Successfully completed {url}", flush=True)
						return
					except asyncio.TimeoutError as exc:
						last_error = f"Timeout: {str(exc)}"
						attempt_elapsed = time.perf_counter() - attempt_started
						print(f"[DEBUG] Timeout error on {url}: {last_error}", flush=True)
						if attempt < retries:
							print(
								f"[RETRY] {url} attempt {attempt}/{retries} failed after {_fmt_seconds(attempt_elapsed)}: {last_error}"
							)
							await asyncio.sleep(1)
					except Exception as exc:  # noqa: BLE001
						last_error = str(exc)
						attempt_elapsed = time.perf_counter() - attempt_started
						print(f"[DEBUG] Exception on {url}: {last_error}", flush=True)
						if attempt < retries:
							print(
								f"[RETRY] {url} attempt {attempt}/{retries} failed after {_fmt_seconds(attempt_elapsed)}: {last_error}"
							)
							await asyncio.sleep(1)

				failed += 1
				url_elapsed = time.perf_counter() - url_started
				done = success + failed
				print(f"[FAIL] {url} ({last_error}) | total: {_fmt_seconds(url_elapsed)}")
				print(f"[PROGRESS] {done}/{len(links)} completed")
				print(f"[DEBUG] Failed to process {url}", flush=True)

		print(f"[DEBUG] Creating tasks for all {len(links)} URLs", flush=True)
		tasks = [process_url(url) for url in links]
		print(f"[DEBUG] Gathering tasks", flush=True)
		await asyncio.gather(*tasks)
		print(f"[DEBUG] All tasks completed", flush=True)

	index_path = output_root / "index.csv"
	with index_path.open("w", encoding="utf-8", newline="") as fp:
		writer = csv.writer(fp)
		writer.writerow(["url", "markdown_path"])
		for url, rel_path in sorted(index_rows, key=lambda x: (x[0], x[1])):
			writer.writerow([url, rel_path])

	print("\n=== Crawl Summary ===")
	print(f"Total links: {len(links)}")
	print(f"Success: {success}")
	print(f"Failed: {failed}")
	total_elapsed = time.perf_counter() - run_started
	print(f"Total elapsed: {_fmt_seconds(total_elapsed)}")
	if url_durations:
		avg_elapsed = sum(url_durations) / len(url_durations)
		print(f"Average successful URL time: {_fmt_seconds(avg_elapsed)}")
	print(f"Output dir: {output_root}")
	print(f"Index file: {index_path}")


def parse_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser(
		description=(
			"Crawl all links with crawl4ai and export markdown grouped by "
			"parent/sub-parent URL path directories."
		)
	)
	parser.add_argument(
		"--input",
		default="link_tree_unique_links.txt",
		help="Input txt file containing one URL per line.",
	)
	parser.add_argument(
		"--output",
		default="md_export",
		help="Root directory for markdown exports.",
	)
	parser.add_argument(
		"--max-concurrency",
		type=int,
		default=5,
		help="Maximum number of concurrent crawl requests.",
	)
	parser.add_argument(
		"--retries",
		type=int,
		default=2,
		help="Retry attempts per URL.",
	)
	parser.add_argument(
		"--request-timeout",
		type=float,
		default=20.0,
		help="Per-URL timeout (seconds) for crawl fetch+render.",
	)
	parser.add_argument(
		"--page-timeout-ms",
		type=int,
		default=15000,
		help="Crawl4AI page timeout in milliseconds.",
	)
	parser.add_argument(
		"--delay-before-return-html",
		type=float,
		default=0.3,
		help="Extra wait (seconds) before collecting rendered HTML.",
	)
	parser.add_argument(
		"--wait-until",
		default="networkidle",
		help="Playwright wait condition passed to Crawl4AI (e.g., load, domcontentloaded, networkidle).",
	)
	parser.add_argument(
		"--scan-full-page",
		action=argparse.BooleanOptionalAction,
		default=True,
		help="Enable/disable full-page scanning in Crawl4AI.",
	)
	parser.add_argument(
		"--table-processing",
		action=argparse.BooleanOptionalAction,
		default=True,
		help="Enable/disable HTML-table and div-table markdown reconstruction.",
	)
	parser.add_argument(
		"--append-table-div-html",
		action=argparse.BooleanOptionalAction,
		default=True,
		help="Append original table-like div HTML blocks into output markdown.",
	)
	parser.add_argument(
		"--limit",
		type=int,
		default=0,
		help="Process only the first N URLs from input (0 = all).",
	)
	return parser.parse_args()


def main() -> None:
	configure_console_encoding()
	args = parse_args()

	input_file = Path(args.input)
	if not input_file.exists():
		raise FileNotFoundError(f"Input file not found: {input_file}")

	links = read_links(input_file)
	if not links:
		print("No links found in input file.")
		return
	if args.limit > 0:
		links = links[:args.limit]

	run_config = build_run_config_from_args(args)

	asyncio.run(
		crawl_and_export(
			links=links,
			output_root=Path(args.output),
			max_concurrency=max(1, args.max_concurrency),
			retries=max(1, args.retries),
			run_config=run_config,
			request_timeout=max(1.0, args.request_timeout),
			table_processing=args.table_processing,
			append_table_div_html=args.append_table_div_html,
		)
	)


if __name__ == "__main__":
	main()
