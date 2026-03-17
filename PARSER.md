# Parser Script Documentation

This document explains how to use `parser.py` to process crawled website links and export cleaned, structured markdown files for each page.

## What `parser.py` does

- Reads a list of URLs from a text file (one per line)
- Crawls each URL using Crawl4AI (headless browser rendering)
- Extracts readable markdown content from each page
- Cleans up navigation/footer noise
- Optionally reconstructs tables from HTML
- Writes one markdown file per page, organized by URL path
- Produces an index CSV summarizing all exports

## Requirements

- Python 3.11 (Recommended)
- Install dependencies:

```bash
pip install crawl4ai lxml
```

## Basic usage

```bash
py parser.py --input unique_links.txt --output md_export
```

## CLI options

### `--input`
Input text file with one URL per line. (Default: `link_tree_unique_links.txt`)

### `--output`
Root directory for markdown exports. (Default: `md_export`)

### `--max-concurrency`
Maximum number of concurrent crawl requests. (Default: 5)

### `--retries`
Retry attempts per URL. (Default: 2)

### `--request-timeout`
Timeout (seconds) for each crawl request. (Default: 20.0)

### `--page-timeout-ms`
Timeout (milliseconds) for page rendering in Crawl4AI. (Default: 15000)

### `--delay-before-return-html`
Extra wait (seconds) before collecting rendered HTML. (Default: 0.3)

### `--wait-until`
Playwright wait condition for Crawl4AI (`load`, `domcontentloaded`, `networkidle`). (Default: `networkidle`)

### `--scan-full-page`
Enable/disable full-page scanning. (Default: enabled)

### `--table-processing`
Enable/disable HTML-table and div-table markdown reconstruction. (Default: enabled)

### `--append-table-div-html`
Append original table-like div HTML blocks into output markdown. (Default: enabled)

### `--limit`
Process only the first N URLs from input (0 = all). (Default: 0)

### `--footer-markers`
Path to a txt file with footer marker strings (one per line).

- When provided, markdown cleanup trims content from the first matched marker to the end.
- When omitted, no site-specific footer markers are applied.

### `--slug-stop`
Path to a txt file with URL slug stop words (one per line).

- These tokens are ignored when matching URL path tokens to heading text.
- Useful for generic words like `product`, `category`, `page`.

## Output structure

- Markdown files for each URL, organized by URL path (e.g., `md_export/products/item-a.md`)
- `index.csv`: summary of all crawled URLs and their output paths

## How it works

1. Reads URLs from the input file
2. Crawls each URL using Crawl4AI (with retries and concurrency)
3. Extracts markdown content, cleans up navigation/footer, and reconstructs tables if enabled
4. Writes cleaned markdown to the appropriate output path
5. Logs crawl summary and writes an index CSV

## Example commands

### Standard run

```bash
py parser.py --input unique_links.txt --output md_export
```

### Limit to first 10 URLs and increase concurrency

```bash
py parser.py --input unique_links.txt --output md_export --limit 10 --max-concurrency 10
```

### Disable table processing

```bash
py parser.py --input unique_links.txt --output md_export --table-processing false
```

### Use txt config flags for site-specific cleanup

```bash
py parser.py \
	--input unique_links.txt \
	--output md_export \
	--footer-markers sample.footer-markers.txt \
	--slug-stop sample.slug-stop.txt
```

## Sample config files

- `sample.footer-markers.txt`: example markers for `--footer-markers`
- `sample.slug-stop.txt`: example stop words for `--slug-stop`
- `sample.config.parser.txt`: combined reference template

## Troubleshooting

- If you see encoding errors on Windows, the script will attempt to force UTF-8 output.
- If some pages are missing content, try increasing `--page-timeout-ms` or `--delay-before-return-html`.
- If you get no output, check that your input file exists and contains valid URLs.
- For sites that render content via JavaScript, keep `scan-full-page` enabled.

## Script entry point

Run directly:

```bash
py parser.py --input unique_links.txt --output md_export
```

Or import functions from `parser.py` in another Python module for custom pipelines.
