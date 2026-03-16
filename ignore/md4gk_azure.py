from __future__ import annotations

import argparse
import os
import re
from dataclasses import dataclass
from pathlib import Path

from litellm import completion

_LLM_NORMALIZE_MD_INSTRUCTION = """You are a technical documentation normalizer.

You will receive a raw markdown document extracted from a webpage.

Your task is to CLEAN and NORMALIZE the markdown so that ALL documents follow the same structure and are ready for knowledge graph extraction.

---

OBJECTIVES

1. Remove noise and formatting inconsistencies.
2. Convert technical information into normalized tables.
3. Standardize headings and section order.
4. Preserve all technical parameters and specifications.
5. Make the output deterministic so that hundreds of documents share the exact same schema.

Do NOT summarize technical information.
Do NOT remove specifications.

---

OUTPUT STRUCTURE

Every normalized document MUST follow this structure exactly:

# Metadata

| Field        | Value                                               |
| ------------ | --------------------------------------------------- |
| Title        |                                                     |
| Page Type    | Product / Software / Article / Technique / Resource |
| Source URL   |                                                     |
| Category     |                                                     |
| Last Updated |                                                     |

# Overview

Short factual description extracted from the page.

# Key Features

| Feature | Description |

# Technical Specifications

## Electrical Specifications

| Parameter | Value | Unit | Notes |

## Hardware Specifications

| Parameter | Value | Unit | Notes |

## Measurement Specifications

| Parameter | Value | Unit | Notes |

## Environmental / Temperature

| Parameter | Value | Unit | Notes |

## General Specifications

| Parameter | Value | Unit | Notes |

# Test Techniques / Control Modes

| Technique | Description | Key Parameters |

# Software Integration

| Software | Description | Capability |

# System Architecture / Infrastructure

| Component | Description |

# Accessories / Optional Modules

| Module | Description | Link |

# Related Products / Systems

| Product | Description | Link |

# Notes

Additional technical details that do not fit into tables.

---

NORMALIZATION RULES

1. Remove:

* HTML artifacts
* navigation links
* SVG placeholders
* duplicated headings
* empty bullet points
* marketing phrases

2. Convert bullet lists to tables whenever possible.

Example:

Input:

* 4 Current Ranges per Channel
* <100ppm Measurement Precision
* 24-bit Voltage Resolution

Output:

| Feature | Description |
| Current ranges per channel | 4 |
| Measurement precision | <100 ppm |
| Voltage resolution | 24 bit |

3. SPECIFICATION TABLE RULES

Do not collapse specification matrices.

If a parameter has multiple configurations or variants,
preserve them as columns.

Use the following format:

| Parameter | Config 1 | Config 2 | Config 3 | Unit | Notes |

Example:

Input:
Current Ranges
5A
1A
100mA
1mA
10A
1A
100mA
1mA

Output:

| Parameter | Config A | Config B | Unit |
|---|---|---|---|
| Max Current | 5 | 10 | A |
| Sub Range 1 | 1 | 1 | A |
| Sub Range 2 | 100 | 100 | mA |
| Sub Range 3 | 1 | 1 | mA |
4. Standardize parameter names.

Examples:

Voltage Range
Current Range
Measurement Precision
Measurement Resolution
Input Impedance
Temperature Range
Channel Count
Data Acquisition Rate

5. Extract control/test techniques.

Examples:

CC -> Constant Current
CV -> Constant Voltage
CCCV -> Constant Current Constant Voltage

Convert to:

| Technique | Description |

6. Convert linked features into table rows.

Example:

[Centralized Infrastructure](link)

->

| Component | Description | Link |

7. Related products must always be in a table.

8. Keep all numeric values exactly as written.

9. Do not invent missing data.

10. If a section is not present in the document, still include the heading and leave the table empty.

11. If the raw markdown contains a source line like "- URL: https://...", copy that exact URL into the Metadata table Source URL field.

12. Preserve source footnotes and annotation lines such as "*Autocalibration box is sold separately." and "**EIS testing device is sold separately." in the Notes section.

---

FORMATTING RULES

* Use Markdown only
* Use tables for structured information
* Use sentence case for parameters
* Units must be separated from values
* Do not include explanations about the transformation

---

FINAL OUTPUT

Return only the normalized markdown document following the schema above.
"""


@dataclass(frozen=True)
class AzureModelConfig:
    model: str
    api_key: str
    api_base: str
    api_version: str


def load_dotenv_file(env_file: Path) -> None:
    """Load simple KEY=VALUE pairs from a .env file into the process environment."""
    if not env_file.exists():
        return

    for raw_line in env_file.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key:
            os.environ.setdefault(key, value)


def resolve_azure_model_config(
    model: str | None = None,
    deployment: str | None = None,
    api_key: str | None = None,
    api_base: str | None = None,
    api_version: str | None = None,
    env_file: Path | None = None,
) -> AzureModelConfig:
    """Resolve Azure OpenAI model and credentials from args and .env values."""
    if env_file is not None:
        load_dotenv_file(env_file)

    deployment = (
        deployment
        or os.getenv("MD4GK_AZURE_DEPLOYMENT")
        or os.getenv("AZURE_OPENAI_DEPLOYMENT")
        or ""
    ).strip()

    model = (model or os.getenv("MD4GK_MODEL") or "").strip()
    if not model:
        if not deployment:
            raise ValueError(
                "Missing Azure deployment. Set MD4GK_AZURE_DEPLOYMENT (or AZURE_OPENAI_DEPLOYMENT) or pass --deployment."
            )
        model = f"azure/{deployment}"
    elif not model.startswith("azure/"):
        model = f"azure/{model}"

    api_key = (
        api_key
        or os.getenv("MD4GK_AZURE_API_KEY")
        or os.getenv("AZURE_OPENAI_API_KEY")
        or ""
    ).strip()
    if not api_key:
        raise ValueError("Missing Azure API key. Set MD4GK_AZURE_API_KEY or AZURE_OPENAI_API_KEY.")

    api_base = (
        api_base
        or os.getenv("MD4GK_AZURE_API_BASE")
        or os.getenv("AZURE_OPENAI_API_BASE")
        or os.getenv("AZURE_OPENAI_ENDPOINT")
        or ""
    ).strip()
    if not api_base:
        raise ValueError(
            "Missing Azure API base. Set MD4GK_AZURE_API_BASE, AZURE_OPENAI_API_BASE, or AZURE_OPENAI_ENDPOINT."
        )

    api_version = (
        api_version
        or os.getenv("MD4GK_AZURE_API_VERSION")
        or os.getenv("AZURE_OPENAI_API_VERSION")
        or "2024-02-15-preview"
    ).strip()

    return AzureModelConfig(
        model=model,
        api_key=api_key,
        api_base=api_base.rstrip("/"),
        api_version=api_version,
    )


def normalize_markdown_text(text: str) -> str:
    """Normalize model text output into plain markdown."""
    text = text.strip()
    if not text:
        return ""

    if text.startswith("```"):
        text = re.sub(r"^```(?:markdown|md)?\s*", "", text)
        text = re.sub(r"\s*```$", "", text).strip()

    return text


def normalize_markdown_with_azure(markdown: str, config: AzureModelConfig) -> str:
    """Run LLM normalization on local markdown text using Azure OpenAI via LiteLLM."""
    prompt = f"{_LLM_NORMALIZE_MD_INSTRUCTION}\n\nRaw markdown:\n{markdown}"
    response = completion(
        model=config.model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
        api_key=config.api_key,
        api_base=config.api_base,
        api_version=config.api_version,
    )
    content = response.choices[0].message.content or ""
    return normalize_markdown_text(content)


def process_existing_markdown_normalization(
    input_dir: Path,
    output_dir: Path,
    config: AzureModelConfig,
    limit: int = 0,
) -> None:
    """Normalize existing markdown files with Azure OpenAI and write cleaned markdown files."""
    if not input_dir.exists():
        raise FileNotFoundError(f"Input markdown directory not found: {input_dir}")

    files = sorted(input_dir.rglob("*.md"))
    if limit > 0:
        files = files[:limit]
    if not files:
        print("No markdown files found for Azure normalization.")
        return

    output_dir.mkdir(parents=True, exist_ok=True)
    success = 0
    failed = 0

    for file_path in files:
        try:
            markdown = file_path.read_text(encoding="utf-8")
            normalized = normalize_markdown_with_azure(markdown, config=config)
            if not normalized:
                raise ValueError("LLM returned empty normalized markdown")

            rel = file_path.relative_to(input_dir)
            out_path = output_dir / rel
            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_text(normalized.rstrip() + "\n", encoding="utf-8")
            success += 1
            print(f"[LLM-NORMALIZE] {file_path} -> {out_path}")
        except Exception as exc:  # noqa: BLE001
            failed += 1
            print(f"[LLM-NORMALIZE-FAIL] {file_path} ({exc})")

    print("\n=== Azure Markdown Normalize Summary ===")
    print(f"Input dir: {input_dir}")
    print(f"Output dir: {output_dir}")
    print(f"Files processed: {len(files)}")
    print(f"Success: {success}")
    print(f"Failed: {failed}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Normalize existing markdown exports into a consistent schema using Azure OpenAI."
    )
    parser.add_argument("--input-dir", default="md_export_old", help="Directory containing source markdown files.")
    parser.add_argument(
        "--output-dir",
        default="md_export_normalized_azure",
        help="Directory where normalized markdown files will be written.",
    )
    parser.add_argument(
        "--model",
        default="",
        help="LiteLLM model. You can pass deployment name or full azure/<deployment> string.",
    )
    parser.add_argument(
        "--deployment",
        default="",
        help="Azure OpenAI deployment name, used when --model is omitted.",
    )
    parser.add_argument(
        "--api-key",
        default="",
        help="Optional Azure API key. If omitted, resolve from .env/environment.",
    )
    parser.add_argument(
        "--api-base",
        default="",
        help="Azure OpenAI endpoint/base URL. If omitted, resolve from .env/environment.",
    )
    parser.add_argument(
        "--api-version",
        default="",
        help="Azure OpenAI API version. If omitted, resolve from .env/environment.",
    )
    parser.add_argument(
        "--env-file",
        default=".env",
        help="Path to .env file used for Azure config resolution.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=0,
        help="Limit number of markdown files to process (0 means all).",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    config = resolve_azure_model_config(
        model=args.model or None,
        deployment=args.deployment or None,
        api_key=args.api_key or None,
        api_base=args.api_base or None,
        api_version=args.api_version or None,
        env_file=Path(args.env_file),
    )
    process_existing_markdown_normalization(
        input_dir=Path(args.input_dir),
        output_dir=Path(args.output_dir),
        config=config,
        limit=max(0, args.limit),
    )


if __name__ == "__main__":
    main()
