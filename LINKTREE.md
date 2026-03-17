# Linktree Crawler Documentation

This document explains how to use `linktree.py` to crawl internal website links, group links into categories, and export text reports.

## What `linktree.py` does

`linktree.py` crawls a website starting from a root URL and produces:

- A link tree (`parent -> children`)
- Category-based link exports
- A global deduplicated link list

It supports language filtering so you can keep only English URLs (default) or include all locales.

## Requirements

Install dependencies:

```bash
pip install requests certifi beautifulsoup4
```

## Basic usage

```bash
py linktree.py --url https://example.com
```

This runs with defaults:

- `--max-depth 1`
- `--language-mode english`
- `--allowed-locales en,en-us,en-gb`
- `--timeout 10`
- `--output-tree link_tree.txt`
- `--output-unique-links unique_links.txt`
- `--output-categories-dir categories_export`

## CLI options

### `--url` (required)
Root URL to start crawling from.

Example:

```bash
--url https://www.arbin.com
```

### `--max-depth`
Maximum recursion depth from the root URL.

- `0`: crawl only root page
- `1`: root + one level of child links
- `2+`: deeper traversal

### `--language-mode`
Language filter behavior:

- `english` (default): keep only English locale paths
- `all`: keep all locale paths

### `--allowed-locales`
Comma-separated locale prefixes allowed when `--language-mode english`.

Default:

```text
en,en-us,en-gb
```

Example:

```bash
--allowed-locales en,en-us
```

### `--timeout`
HTTP timeout (seconds) per request.

### `--output-tree`
Output file path for the link tree report.

### `--output-unique-links`
Output file path for the global unique link report.

### `--output-categories-dir`
Output directory for category reports:

- `categories_summary.txt`
- `category_<category_name>.txt` files

## Examples

### 1) Standard English crawl

```bash
py linktree.py --url https://www.arbin.com --max-depth 1
```

### 2) Include all languages

```bash
py linktree.py --url https://www.arbin.com --language-mode all --max-depth 2
```

### 3) Custom outputs and timeout

```bash
py linktree.py \
  --url https://www.arbin.com \
  --max-depth 2 \
  --timeout 20 \
  --output-tree out/link_tree.txt \
  --output-unique-links out/unique_links.txt \
  --output-categories-dir out/categories
```

## Output files

### Link tree report
File: `link_tree.txt` (or custom path)

Structure:

```text
=== LINK TREE ===

[Parent] https://example.com/
  - https://example.com/products
  - https://example.com/resources
```

### Unique links report
File: `unique_links.txt` (or custom path)

Structure:

```text
=== UNIQUE LINKS ===

- https://example.com/
- https://example.com/products
```

### Categories reports
Directory: `categories_export/` (or custom path)

- `categories_summary.txt`: all categories and links
- `category_<category_name>.txt`: one file per category

## How categorization works

The script uses two strategies:

1. Dropdown extraction (preferred)
- Parses navigation/menu containers (`nav`, `header`, `.menu`, `.navbar`, `.navigation`)
- Uses menu parent labels as category names
- Collects submenu links

2. URL keyword fallback
- Used if dropdown categories are not found
- Maps links by keyword into:
  - `Products`
  - `Resources`
  - `Support`
  - `Company`
  - `Other`

## Link filtering rules

The crawler only keeps internal links (`http/https` and same domain) and skips:

- Anchors (`#...`)
- `mailto:` links
- `javascript:` links
- Cloudflare email protection URLs (`/cdn-cgi/l/email-protection`)
- Common non-HTML assets (pdf, images, archives, media, office files)

In `english` mode, locale-prefixed paths are allowed only if they match `--allowed-locales`.

## Console output

During execution, the script prints sampled child links for each parent and then prints exported file paths.

## Troubleshooting

### No links found

- Verify `--url` is reachable in browser.
- Increase `--timeout`.
- Use `--language-mode all` to rule out locale filtering.
- Some sites render links via JavaScript that static HTML parsing cannot see.

### Too many irrelevant links

- Lower `--max-depth`.
- Keep `--language-mode english`.
- Narrow `--allowed-locales`.

### Categories look wrong or incomplete

- Site menus may differ from expected dropdown structures.
- Fallback keyword categorization may group links broadly; review `categories_summary.txt` and adjust keyword logic in code if needed.

## Script entry point

Run directly:

```bash
py linktree.py --url https://example.com
```

Or import functions from `linktree.py` in another Python module if you need custom pipelines.
