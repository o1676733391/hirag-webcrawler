"""Quick verification of the updated clean_markdown_content function."""
from parser import clean_markdown_content
from pathlib import Path

tests = [
    (
        "md_export_parser_check/product/10a-flat-pouch-cell-battery-holder.md",
        "https://www.arbin.com/product/10a-flat-pouch-cell-battery-holder",
        "product",
    ),
    (
        "md_export_parser_check/company/index.md",
        "https://www.arbin.com/company.html",
        "company",
    ),
    (
        "md_export_parser_check/software-solution/cross-platform-mits.md",
        "https://www.arbin.com/software-solution/cross-platform-mits.html",
        "software",
    ),
]

out_lines = []
for path, url, label in tests:
    raw = Path(path).read_text(encoding="utf-8")
    raw_md = raw.split("# Content\n\n", 1)[1] if "# Content" in raw else raw
    cleaned = clean_markdown_content(raw_md, url)
    first_content = cleaned[:400].strip()
    out_lines.append(f"=== {label.upper()} ({url}) ===")
    out_lines.append(first_content)
    out_lines.append("")

Path("_verify_result.txt").write_text("\n".join(out_lines), encoding="utf-8")
print("Written _verify_result.txt")
