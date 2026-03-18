# HiRAG Documentation

This document explains how to run HiRAG on normalized markdown produced by `md4gk.py`.

## What `hirag_runner.py` does

- Reads normalized markdown files from a directory (default: `demo_v2_norm`)
- Inserts each markdown file as a document into a HiRAG index
- Saves index and graph artifacts to a working directory (default: `hirag_workdir`)
- Supports retrieval + answer generation in `hi` mode and other HiRAG modes

## Requirements

- Python 3.11+ recommended
- Install HiRAG dependencies:

```bash
pip install -r HiRAG/requirements.txt
pip install -e HiRAG
```

- Set OpenAI key (or pass `--openai-api-key`):

```bash
set OPENAI_API_KEY=YOUR_OPENAI_API_KEY
```

Or put it in `.env` (default file loaded by `hirag_runner.py`):

```bash
OPENAI_API_KEY=YOUR_OPENAI_API_KEY
OPENAI_BASE_URL=
```

## Basic usage

Build index from normalized corpus:

```bash
py hirag_runner.py --input-dir demo_v2_norm --working-dir hirag_workdir
```

Build index and ask a question:

```bash
py hirag_runner.py --input-dir demo_v2_norm --working-dir hirag_workdir --query "What are Arbin's main product families?" --mode hi
```

Ask a new question using existing index only:

```bash
py hirag_runner.py --working-dir hirag_workdir --skip-index --query "How does regenerative testing help EV battery validation?" --mode hi
```

## CLI options

### Core paths

- `--input-dir`: normalized markdown folder (default: `demo_v2_norm`)
- `--working-dir`: HiRAG cache/index folder (default: `hirag_workdir`)
- `--limit`: only index the first N markdown files (default: `0`, all)
- `--config-file`: optional `key=value` config file
- `--env-file`: `.env` file path (default: `.env`)

### OpenAI settings

- `--openai-api-key`: API key (fallback: `OPENAI_API_KEY` env)
- `--openai-base-url`: optional compatible base URL
- `--chat-model`: chat model for generation (default: `gpt-4o-mini`)
- `--temperature`: generation temperature (optional)
- `--top-p`: generation top_p (optional)
- `--embedding-model`: embedding model (default: `text-embedding-3-small`)
- `--embedding-dim`: embedding dimension (default: `1536`)

### HiRAG behavior

- `--enable-llm-cache`: `true/false` (default: `true`)
- `--enable-hierachical-mode`: `true/false` (default: `true`)
- `--enable-naive-rag`: `true/false` (default: `true`)
- `--embedding-batch-num`: embedding batch size (default: `6`)
- `--embedding-func-max-async`: max async embed calls (default: `8`)

### Query options

- `--skip-index`: do not insert docs; use existing working dir index
- `--query`: question text to run after indexing
- `--mode`: one of `hi`, `naive`, `hi_nobridge`, `hi_local`, `hi_global`, `hi_bridge`
- `--top-k`: top-k entities (default: `20`)
- `--top-m`: top-m entities per community (default: `10`)

## Sample config file

Use `sample.hirag.config.txt` and run:

```bash
py hirag_runner.py --config-file sample.hirag.config.txt --query "What are key EV testing capabilities?" --mode hi
```

## Troubleshooting

- `Config file not found`: verify `--config-file` path
- `Input markdown directory not found`: verify `--input-dir`
- OpenAI auth errors: set `OPENAI_API_KEY` or pass `--openai-api-key`
- If indexing is expensive, first test with `--limit 20`
