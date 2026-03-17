from __future__ import annotations

import argparse
import os
import re
from dataclasses import dataclass
from pathlib import Path

from litellm import completion

_DEFAULT_INPUT_DIR = "md_export_old"
_DEFAULT_OUTPUT_DIR = "md_export_normalized"
_DEFAULT_ENV_FILE = ".env"
_DEFAULT_LIMIT = 0

_LLM_NORMALIZE_MD_INSTRUCTION = """You are a technical documentation normalization engine.

You will receive a raw markdown document extracted from a webpage.

Your task is to CLEAN and NORMALIZE the markdown so it can be safely used for knowledge graph extraction.

The normalized document must preserve ALL factual information from the original document.

Do not summarize.
Do not remove technical details.
Do not invent missing information.

Your output must be deterministic so that hundreds of documents share a consistent schema.

--------------------------------

PRIMARY GOAL

Convert messy webpage markdown into structured, machine-readable markdown while preserving all factual information.

--------------------------------

STEP 1 — DETERMINE PAGE TYPE

Classify the document into one of these types:

Product  
Software  
Technique  
Article  
Resource  

Use the content of the page to determine the type.

Examples:

Product → hardware specifications, current ranges, voltage ranges  
Software → APIs, features, integrations  
Technique → scientific methods (e.g. CCCV, EIS)  
Units should not be included in the value column but can be mentioned in the notes or context if necessary for clarity.
Article → industry news, research commentary  
Resource → documentation, whitepapers, tutorials

--------------------------------

STEP 2 — CLEAN THE DOCUMENT

Remove:

HTML artifacts  
navigation links  
social media links  
SVG placeholders  
duplicate headings  
author profile sections  
post navigation blocks  
empty bullets  
advertising text  

Preserve:

technical specifications  
data tables  
technical descriptions  
statistics  
footnotes  
annotations  

--------------------------------

STEP 3 — NORMALIZE STRUCTURE

All documents must begin with this metadata block.

# Metadata

| Field | Value1 |
|------|------|
| Title | |
| Page Type | |
| Source URL | |
| Category | |
| Last Updated | |

--------------------------------

STEP 4 — STRUCTURE BASED ON PAGE TYPE

Use the appropriate schema depending on the detected Page Type.

--------------------------------

PRODUCT PAGE STRUCTURE

# Overview

Short factual description of the product.

# Key Features

| Feature | Description |

# Technical Specifications

## Electrical Specifications
| Parameter | Value1 | Value2 | Value3 | ... | Notes | (if multiple electrical specs exist, split into separate tables by category)

## Hardware Specifications
| Parameter | Value1 | Value2 | Value3 | ... | Notes | (if multiple hardware specs exist, split into separate tables by category)

## Measurement Specifications
| Parameter | Value1 | Value2 | Value3 | ... | Notes | (if multiple measurement specs exist, split into separate tables by category)

## Environmental / Temperature
| Parameter | Value1 | Value2 | Value3 | ... | Notes | (if multiple environmental specs exist, split into separate tables by category)

## General Specifications
| Parameter | Value1 | Value2 | Value3 | ... | Notes | (if general specs exist that don't fit other categories)

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

--------------------------------

ARTICLE PAGE STRUCTURE

# Overview

Short factual summary.

# Key Points

| Topic | Summary |

# Detailed Explanation

Preserve the narrative explanation from the article.
Break large sections into logical subsections if necessary.

# Data / Statistics

| Metric | Value1 | Value2 | Value3 | ... | Context | Notes | 

# Industry Context

| Factor | Description |

# Related Technologies / Concepts

| Concept | Description |

# Notes

--------------------------------

TECHNIQUE PAGE STRUCTURE

# Overview

Explanation of the scientific technique.

# Principle

Describe the physical or electrochemical principle.

# Key Parameters

| Parameter | Description |

# Applications

| Application | Description |

# Related Techniques

| Technique | Description |

# Notes

--------------------------------

SOFTWARE PAGE STRUCTURE

# Overview

Description of the software.

# Key Features

| Feature | Description |

# Capabilities

| Capability | Description |

# Integrations

| Software | Purpose |

# System Requirements

| Requirement | Value |

# Notes

--------------------------------

STEP 5 — TABLE NORMALIZATION RULES

Convert bullet lists to tables whenever possible.

Example

Input

• 4 current ranges  
• <100 ppm precision  
• 24-bit resolution  

Output

| Feature | Description |
| Current ranges | 4 |
| Measurement precision | <100 ppm |
| Resolution | 24 bit |

--------------------------------

SPECIFICATION MATRIX RULE

If multiple configuration params exist, split them as slash "/" . DO NOT group all cases into 1 value. Instead, split into separate columns for each case. DO NOT drop any cases. 
Example: 
| Parameter | Value 1 | Value 2 | Value 3 | Value 4 | Value 5 | Value 6 | Value 7 | Value 8 | Value 9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Number of Channels | 48 | 12 | 12 | 48 | 12 | 12 | 32 | 8 | 8 | |
| Voltage Ranges | -6V/6V | -6V/6V | -6V/6V | 2V/10V | 2V/10V | 2V/10V | 2V/20V | 2V/20V | 2V/20V | V |
| Current Ranges | 100A/25A | 300A/150A/50A | 400A/200A/50A | 100A/25A | 300A/150A/50A | 400A/200A/50A | 100A/25A | 300A/150A/50A | 400A/200A/50A |
--------------------------------

STEP 6 — PARAMETER NORMALIZATION

Standardize parameter names when possible.

Examples:

Voltage Range  
Current Range  
Measurement Precision  
Measurement Resolution  
Input Impedance  
Temperature Range  
Channel Count  
Data Logging Rate  

--------------------------------

STEP 7 — INFORMATION PRESERVATION

Never remove factual information.

Narrative explanations must remain in the document if they contain useful context.

Tables should only be used for structured data.

--------------------------------

STEP 8 — NOTES

Preserve footnotes and annotations.

Examples

*Autocalibration box is sold separately.*

**EIS testing device is sold separately.**

--------------------------------

STEP 9 — MISSING DATA

If a section exists in the schema but not in the source document, include the section but leave the table empty.

--------------------------------

FORMATTING RULES

Use Markdown only  
Use tables for structured data  
Use sentence case for parameter names  
Do not explain the transformation  

--------------------------------

FINAL OUTPUT

Return only the normalized markdown document.
"""


@dataclass(frozen=True)
class ModelConfig:
	provider_name: str
	model: str
	api_key: str | None


@dataclass(frozen=True)
class UsageStats:
	prompt_tokens: int = 0
	completion_tokens: int = 0
	total_tokens: int = 0


def extract_usage_stats(response: object) -> UsageStats:
	"""Extract token usage from a LiteLLM response when available."""
	usage = getattr(response, "usage", None)
	if usage is None and isinstance(response, dict):
		usage = response.get("usage")
	if usage is None:
		return UsageStats()

	if isinstance(usage, dict):
		prompt_tokens = int(usage.get("prompt_tokens") or 0)
		completion_tokens = int(usage.get("completion_tokens") or 0)
		total_tokens = int(usage.get("total_tokens") or 0)
	else:
		prompt_tokens = int(getattr(usage, "prompt_tokens", 0) or 0)
		completion_tokens = int(getattr(usage, "completion_tokens", 0) or 0)
		total_tokens = int(getattr(usage, "total_tokens", 0) or 0)

	return UsageStats(
		prompt_tokens=prompt_tokens,
		completion_tokens=completion_tokens,
		total_tokens=total_tokens,
	)


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


def pick_provider_api_key(provider_name: str) -> str | None:
	"""Resolve provider-specific API key from environment variables."""
	provider_name = provider_name.lower().strip()
	if provider_name == "gemini":
		return (
			os.getenv("MD4GK_GEMINI_API_KEY")
			or os.getenv("GEMINI_API_KEY")
			or os.getenv("GOOGLE_API_KEY")
		)
	if provider_name == "openai":
		return os.getenv("MD4GK_OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY")
	return None


def resolve_model_config(
	provider_name: str | None = None,
	model: str | None = None,
	api_key: str | None = None,
	env_file: Path | None = None,
) -> ModelConfig:
	"""Resolve provider/model/api key from CLI args and .env values."""
	if env_file is not None:
		load_dotenv_file(env_file)

	provider_name = (provider_name or os.getenv("MD4GK_PROVIDER") or "gemini").strip().lower()
	if provider_name not in {"gemini", "openai"}:
		raise ValueError("Provider must be 'gemini' or 'openai'")

	model = (model or os.getenv("MD4GK_MODEL") or "").strip()
	if not model:
		if provider_name == "gemini":
			model = os.getenv("MD4GK_GEMINI_MODEL", "gemini/gemini-flash-latest").strip()
		else:
			model = os.getenv("MD4GK_OPENAI_MODEL", "openai/gpt-4o-mini").strip()

	api_key = (api_key or pick_provider_api_key(provider_name) or "").strip() or None
	if not api_key:
		raise ValueError(
			f"Missing API key for {provider_name}. Set it in .env or pass --api-key."
		)

	return ModelConfig(provider_name=provider_name, model=model, api_key=api_key)


def normalize_markdown_text(text: str) -> str:
	"""Normalize model text output into plain markdown."""
	text = text.strip()
	if not text:
		return ""

	if text.startswith("```"):
		text = re.sub(r"^```(?:markdown|md)?\s*", "", text)
		text = re.sub(r"\s*```$", "", text).strip()

	return text


def normalize_markdown_with_llm(
	markdown: str,
	provider: str,
	api_token: str | None = None,
	instruction_text: str | None = None,
) -> tuple[str, UsageStats]:
	"""Run direct LLM normalization on local markdown text and return cleaned markdown and usage."""
	instruction = (instruction_text or _LLM_NORMALIZE_MD_INSTRUCTION).strip()
	prompt = f"{instruction}\n\nRaw markdown:\n{markdown}"
	kwargs = {
		"model": provider,
		"messages": [{"role": "user", "content": prompt}],
		"temperature": 0,
	}
	if api_token:
		kwargs["api_key"] = api_token

	response = completion(**kwargs)
	content = response.choices[0].message.content or ""
	return normalize_markdown_text(content), extract_usage_stats(response)


def process_existing_markdown_normalization(
	input_dir: Path,
	output_dir: Path,
	provider: str,
	api_token: str | None = None,
	limit: int = 0,
	instruction_text: str | None = None,
) -> None:
	"""Normalize existing markdown files with an LLM and write cleaned markdown files."""
	if not input_dir.exists():
		raise FileNotFoundError(f"Input markdown directory not found: {input_dir}")

	files = sorted(input_dir.rglob("*.md"))
	if limit > 0:
		files = files[:limit]
	if not files:
		print("No markdown files found for local LLM normalization.")
		return

	output_dir.mkdir(parents=True, exist_ok=True)
	success = 0
	failed = 0
	total_usage = UsageStats()

	for file_path in files:
		try:
			markdown = file_path.read_text(encoding="utf-8")
			normalized, usage = normalize_markdown_with_llm(
				markdown,
				provider=provider,
				api_token=api_token,
				instruction_text=instruction_text,
			)
			if not normalized:
				raise ValueError("LLM returned empty normalized markdown")

			rel = file_path.relative_to(input_dir)
			out_path = output_dir / rel
			out_path.parent.mkdir(parents=True, exist_ok=True)
			out_path.write_text(normalized.rstrip() + "\n", encoding="utf-8")
			success += 1
			total_usage = UsageStats(
				prompt_tokens=total_usage.prompt_tokens + usage.prompt_tokens,
				completion_tokens=total_usage.completion_tokens + usage.completion_tokens,
				total_tokens=total_usage.total_tokens + usage.total_tokens,
			)
			print(
				f"[LLM-NORMALIZE] {file_path} -> {out_path} "
				f"(prompt_tokens={usage.prompt_tokens}, completion_tokens={usage.completion_tokens}, total_tokens={usage.total_tokens})"
			)
		except Exception as exc:  # noqa: BLE001
			failed += 1
			print(f"[LLM-NORMALIZE-FAIL] {file_path} ({exc})")

	print("\n=== Local Markdown Normalize Summary ===")
	print(f"Input dir: {input_dir}")
	print(f"Output dir: {output_dir}")
	print(f"Files processed: {len(files)}")
	print(f"Success: {success}")
	print(f"Failed: {failed}")
	print(f"Prompt tokens: {total_usage.prompt_tokens}")
	print(f"Completion tokens: {total_usage.completion_tokens}")
	print(f"Total tokens: {total_usage.total_tokens}")


def parse_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser(
		description="Normalize existing markdown exports into a consistent knowledge-graph-ready schema."
	)
	parser.add_argument("--input-dir", default=_DEFAULT_INPUT_DIR, help="Directory containing source markdown files.")
	parser.add_argument(
		"--output-dir",
		default=_DEFAULT_OUTPUT_DIR,
		help="Directory where normalized markdown files will be written.",
	)
	parser.add_argument(
		"--provider",
		choices=["gemini", "openai"],
		default="",
		help="LLM provider family. If omitted, use MD4GK_PROVIDER from .env.",
	)
	parser.add_argument(
		"--model",
		default="",
		help="Full LiteLLM model string. If omitted, resolve provider-specific default from .env.",
	)
	parser.add_argument(
		"--api-key",
		default="",
		help="Optional explicit API key. If omitted, resolve provider key from .env.",
	)
	parser.add_argument(
		"--env-file",
		default=_DEFAULT_ENV_FILE,
		help="Path to .env file used for provider/model/api-key resolution.",
	)
	parser.add_argument(
		"--limit",
		type=int,
		default=_DEFAULT_LIMIT,
		help="Limit number of markdown files to process (0 means all).",
	)
	parser.add_argument(
		"--instruction-file",
		default="",
		help="Path to a txt/markdown file containing the LLM normalization instruction. If omitted, use the built-in instruction.",
	)
	parser.add_argument(
		"--config-file",
		default="",
		help="Path to txt config file (key=value) for md4gk settings.",
	)
	return parser.parse_args()


def read_instruction_file(path: str) -> str | None:
	"""Read custom instruction text from file if provided."""
	if not path:
		return None
	instruction_path = Path(path)
	if not instruction_path.exists():
		raise FileNotFoundError(f"Instruction file not found: {instruction_path}")
	text = instruction_path.read_text(encoding="utf-8").strip()
	if not text:
		raise ValueError(f"Instruction file is empty: {instruction_path}")
	return text


def read_txt_config(path: str) -> dict[str, str]:
	"""Read key=value pairs from a txt config file."""
	if not path:
		return {}
	config_path = Path(path)
	if not config_path.exists():
		raise FileNotFoundError(f"Config file not found: {config_path}")

	config: dict[str, str] = {}
	for raw_line in config_path.read_text(encoding="utf-8").splitlines():
		line = raw_line.strip()
		if not line or line.startswith("#") or "=" not in line:
			continue
		key, value = line.split("=", 1)
		key = key.strip().lower().replace("-", "_")
		value = value.strip().strip('"').strip("'")
		if key:
			config[key] = value
	return config


def main() -> None:
	args = parse_args()
	txt_config = read_txt_config(args.config_file)

	def pick_value(cli_value: str, cli_default: str, config_key: str) -> str:
		if cli_value != cli_default:
			return cli_value
		return txt_config.get(config_key, cli_value)

	input_dir_value = pick_value(args.input_dir, _DEFAULT_INPUT_DIR, "input_dir")
	output_dir_value = pick_value(args.output_dir, _DEFAULT_OUTPUT_DIR, "output_dir")
	env_file_value = pick_value(args.env_file, _DEFAULT_ENV_FILE, "env_file")
	provider_value = pick_value(args.provider, "", "provider")
	model_value = pick_value(args.model, "", "model")
	api_key_value = pick_value(args.api_key, "", "api_key")
	instruction_file_value = pick_value(args.instruction_file, "", "instruction_file")

	limit_value = args.limit
	if args.limit == _DEFAULT_LIMIT and "limit" in txt_config:
		limit_value = int(txt_config["limit"])

	instruction_text = read_instruction_file(instruction_file_value)
	config = resolve_model_config(
		provider_name=provider_value or None,
		model=model_value or None,
		api_key=api_key_value or None,
		env_file=Path(env_file_value),
	)
	process_existing_markdown_normalization(
		input_dir=Path(input_dir_value),
		output_dir=Path(output_dir_value),
		provider=config.model,
		api_token=config.api_key,
		limit=max(0, limit_value),
		instruction_text=instruction_text,
	)


if __name__ == "__main__":
	main()
