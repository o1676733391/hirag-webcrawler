from __future__ import annotations

import argparse
import re
from pathlib import Path

# Match http/https links and stop before common closing separators.
URL_PATTERN = re.compile(r"https?://[^\s\]\[\)\(\"'<>]+")


def extract_unique_links(text: str) -> list[str]:
    """Extract unique links while preserving first-seen order."""
    seen: set[str] = set()
    unique_links: list[str] = []

    for match in URL_PATTERN.findall(text):
        # Clean trailing punctuation that can appear in plain-text lists.
        link = match.rstrip(".,;:")
        if link not in seen:
            seen.add(link)
            unique_links.append(link)

    return unique_links


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Extract and deduplicate links from a text file."
    )
    parser.add_argument(
        "input_file",
        nargs="?",
        default="categories_export/categories_summary.txt",
        help="Path to source text file (default: categories_export/categories_summary.txt)",
    )
    parser.add_argument(
        "-o",
        "--output",
        default="categories_export/unique_links.txt",
        help="Output file path (default: categories_export/unique_links.txt)",
    )

    args = parser.parse_args()
    input_path = Path(args.input_file)
    output_path = Path(args.output)

    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    text = input_path.read_text(encoding="utf-8")
    unique_links = extract_unique_links(text)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(unique_links) + "\n", encoding="utf-8")

    print(f"Found {len(unique_links)} unique links.")
    print(f"Saved to: {output_path}")


if __name__ == "__main__":
    main()
