# MD4GK Documentation

This document explains how to use `md4gk.py` to normalize markdown files into a consistent, knowledge-graph-ready schema using an LLM.

## What md4gk does

- Reads markdown files from an input directory
- Sends each file to an LLM with a normalization instruction
- Writes normalized markdown to a mirrored output directory structure
- Tracks token usage (prompt/completion/total)
- Supports provider/model/api-key resolution from CLI, config file, and `.env`

## Requirements

- Python 3.8+
- Install dependencies:

```bash
pip install litellm
```

## Quick start

```bash
py md4gk.py --input-dir test-llm --output-dir test-llm-normalized --provider openai
```

## CLI flags

### Core paths

- `--input-dir`: Source markdown directory (default: `md_export_old`)
- `--output-dir`: Destination directory for normalized markdown (default: `md_export_normalized`)
- `--limit`: Number of files to process, `0` means all (default: `0`)

### Model/provider

- `--provider`: `gemini` or `openai`
- `--model`: Full LiteLLM model string (example: `openai/gpt-4o-mini`)
- `--api-key`: Explicit API key
- `--env-file`: Path to `.env` used for config/key resolution (default: `.env`)

### Instruction and config

- `--instruction-file`: Path to txt/markdown file used as normalization prompt instruction
- `--config-file`: Path to txt config file (`key=value` format)

## Config file format (`--config-file`)

Use plain text with one `key=value` per line.
Lines starting with `#` are ignored.

Supported keys:

- `input_dir`
- `output_dir`
- `provider`
- `model`
- `api_key`
- `env_file`
- `limit`
- `instruction_file`

Example:

```text
# sample.md4gk.config.txt
input_dir=test-llm
output_dir=test-llm-normalized
provider=openai
model=openai/gpt-4o-mini
api_key=
env_file=.env
limit=0
instruction_file=sample.md4gk.instruction.txt
```

## Precedence rules

Configuration is resolved in this order:

1. CLI flags (highest priority)
2. `--config-file` values
3. Built-in defaults / `.env` fallbacks

This means you can run with a config file and override only one value from CLI.

## Usage examples

### Use config file only

```bash
py md4gk.py --config-file sample.md4gk.config.txt
```

### Use config file + override limit from CLI

```bash
py md4gk.py --config-file sample.md4gk.config.txt --limit 10
```

### Use custom instruction prompt

```bash
py md4gk.py \
  --input-dir test-llm \
  --output-dir test-llm-normalized \
  --provider openai \
  --instruction-file sample.md4gk.instruction.txt
```

### Use config file with sample instruction

```bash
py md4gk.py --config-file sample.md4gk.config.txt --api-key YOUR_OPENAI_API_KEY
```

## Environment variable resolution

`md4gk.py` supports provider/model/api-key resolution from environment variables.

Provider:

- `MD4GK_PROVIDER`

Model:

- `MD4GK_MODEL`
- `MD4GK_GEMINI_MODEL` (gemini fallback)
- `MD4GK_OPENAI_MODEL` (openai fallback)

API keys:

- Gemini: `MD4GK_GEMINI_API_KEY`, `GEMINI_API_KEY`, `GOOGLE_API_KEY`
- OpenAI: `MD4GK_OPENAI_API_KEY`, `OPENAI_API_KEY`

## Output behavior

- Processes all `*.md` files recursively under input directory
- Writes normalized files to output directory, preserving relative paths
- Prints per-file success/failure logs
- Prints token usage summary at the end

## Troubleshooting

- `Missing API key`: provide `--api-key`, set key in `.env`, or set environment variable.
- `Instruction file not found`: verify `--instruction-file` path.
- `Config file not found`: verify `--config-file` path.
- `LLM returned empty normalized markdown`: inspect source markdown and prompt instruction quality.
