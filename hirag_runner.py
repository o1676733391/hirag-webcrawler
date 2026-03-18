from __future__ import annotations

import argparse
import asyncio
import json
import math
import os
import random
import re
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Optional

import numpy as np
from openai import AsyncOpenAI, BadRequestError


_DEFAULT_INPUT_DIR = "demo_v2_norm"
_DEFAULT_WORKING_DIR = "hirag_workdir"
_DEFAULT_LIMIT = 0
_DEFAULT_QUERY_MODE = "hi"
_DEFAULT_ENV_FILE = ".env"
_DEFAULT_CONFIG_FILE = "hirag.config"


@dataclass
class EmbeddingFunc:
    embedding_dim: int
    max_token_size: int
    func: Callable

    async def __call__(self, *args, **kwargs) -> np.ndarray:
        return await self.func(*args, **kwargs)


@dataclass
class TokenUsageStats:
    chat_prompt_tokens: int = 0
    chat_completion_tokens: int = 0
    chat_total_tokens: int = 0
    chat_api_calls: int = 0
    chat_cache_hits: int = 0
    embedding_prompt_tokens: int = 0
    embedding_total_tokens: int = 0
    embedding_api_calls: int = 0
    chat_wall_seconds: float = 0.0
    embedding_wall_seconds: float = 0.0


def _usage_value(usage, key: str) -> int:
    if usage is None:
        return 0
    value = getattr(usage, key, 0)
    if value is None:
        return 0
    return int(value)


def print_token_usage_summary(stats: TokenUsageStats) -> None:
    print("\n=== Token Usage Summary ===")
    print(f"Chat API calls: {stats.chat_api_calls}")
    print(f"Chat cache hits: {stats.chat_cache_hits}")
    print(f"Chat prompt tokens: {stats.chat_prompt_tokens}")
    print(f"Chat completion tokens: {stats.chat_completion_tokens}")
    print(f"Chat total tokens: {stats.chat_total_tokens}")
    print(f"Embedding API calls: {stats.embedding_api_calls}")
    print(f"Embedding prompt tokens: {stats.embedding_prompt_tokens}")
    print(f"Embedding total tokens: {stats.embedding_total_tokens}")
    print(f"Chat wall time (s): {stats.chat_wall_seconds:.3f}")
    print(f"Embedding wall time (s): {stats.embedding_wall_seconds:.3f}")
    if stats.chat_api_calls > 0:
        print(f"Avg chat call time (s): {stats.chat_wall_seconds / stats.chat_api_calls:.3f}")
    if stats.embedding_api_calls > 0:
        print(f"Avg embedding call time (s): {stats.embedding_wall_seconds / stats.embedding_api_calls:.3f}")
    print(f"Combined total tokens: {stats.chat_total_tokens + stats.embedding_total_tokens}")


def print_progress_usage(stats: TokenUsageStats, processed_docs: int) -> None:
    print("\n=== Progress Usage ===")
    print(f"Processed docs: {processed_docs}")
    print(f"Chat API calls: {stats.chat_api_calls}")
    print(f"Chat cache hits: {stats.chat_cache_hits}")
    print(f"Chat total tokens: {stats.chat_total_tokens}")
    print(f"Embedding API calls: {stats.embedding_api_calls}")
    print(f"Embedding total tokens: {stats.embedding_total_tokens}")
    print(f"Combined total tokens: {stats.chat_total_tokens + stats.embedding_total_tokens}")
    print(f"Chat wall time (s): {stats.chat_wall_seconds:.3f}")
    print(f"Embedding wall time (s): {stats.embedding_wall_seconds:.3f}")


def wrap_embedding_func_with_attrs(**kwargs):
    def final_decorator(func) -> EmbeddingFunc:
        return EmbeddingFunc(**kwargs, func=func)

    return final_decorator


def parse_bool(value: str) -> bool:
    v = value.strip().lower()
    if v in {"1", "true", "t", "yes", "y", "on"}:
        return True
    if v in {"0", "false", "f", "no", "n", "off"}:
        return False
    raise ValueError(f"Invalid boolean value: {value}")


def parse_optional_float(value):
    if value is None:
        return None
    text = str(value).strip()
    if text == "":
        return None
    return float(text)


def normalize_entity_name(name: str) -> str:
    cleaned = str(name).strip().strip('"').strip("'")
    cleaned = cleaned.replace("&quot;", "")
    return " ".join(cleaned.split())


def split_source_ids(raw_source_id: str, sep: str) -> list[str]:
    if not raw_source_id:
        return []
    parts = [p.strip() for p in str(raw_source_id).split(sep)]
    return [p for p in parts if p]


def sanitize_text(value: str) -> str:
    cleaned = value.encode("utf-8", errors="ignore").decode("utf-8", errors="ignore")
    cleaned = re.sub(r"[\ud800-\udfff]", "", cleaned)
    cleaned = cleaned.replace("\u2028", " ").replace("\u2029", " ")
    return re.sub(r"[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]", "", cleaned)


def ultra_sanitize_text(value: str) -> str:
    base = sanitize_text(value)
    return "".join(ch for ch in base if ch in {"\n", "\t"} or ch.isprintable())


def sanitize_messages(messages: list[dict]) -> list[dict]:
    sanitized: list[dict] = []
    for message in messages:
        content = message.get("content", "")
        if not isinstance(content, str):
            content = str(content)
        sanitized.append({"role": message.get("role", "user"), "content": sanitize_text(content)})
    return sanitized


def ultra_sanitize_messages(messages: list[dict]) -> list[dict]:
    sanitized: list[dict] = []
    for message in messages:
        content = message.get("content", "")
        if not isinstance(content, str):
            content = str(content)
        sanitized.append({"role": message.get("role", "user"), "content": ultra_sanitize_text(content)})
    return sanitized


def make_json_safe(value):
    if isinstance(value, str):
        return sanitize_text(value)
    if isinstance(value, bool) or value is None:
        return value
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        if math.isfinite(value):
            return value
        return None
    if isinstance(value, dict):
        return {str(k): make_json_safe(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [make_json_safe(v) for v in value]
    return sanitize_text(str(value))


def sanitize_chat_kwargs(kwargs: dict) -> dict:
    allowed = {
        "max_tokens",
        "temperature",
        "top_p",
        "presence_penalty",
        "frequency_penalty",
        "stop",
        "response_format",
        "seed",
        "tools",
        "tool_choice",
    }
    sanitized: dict = {}
    for key, value in kwargs.items():
        if key in allowed:
            sanitized[key] = make_json_safe(value)
    return sanitized


def read_txt_config(path: str) -> dict[str, str]:
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


def load_env_file(path: Path) -> None:
    if not path.exists():
        return

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" not in line:
            continue

        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


def resolve_hi_import(repo_root: Path):
    try:
        from hirag import HiRAG, QueryParam  # type: ignore
        return HiRAG, QueryParam
    except ImportError:
        hirag_src = repo_root / "HiRAG"
        if not hirag_src.exists():
            raise
        sys.path.insert(0, str(hirag_src))
        from hirag import HiRAG, QueryParam  # type: ignore
        return HiRAG, QueryParam


def collect_markdown_docs(input_dir: Path, limit: int = 0) -> list[tuple[str, str]]:
    files = sorted(input_dir.rglob("*.md"))
    if limit > 0:
        files = files[:limit]

    docs: list[tuple[str, str]] = []
    for file_path in files:
        rel = file_path.relative_to(input_dir).as_posix()
        body = file_path.read_text(encoding="utf-8", errors="ignore").strip()
        if not body:
            continue
        docs.append((rel, f"# Source\n{rel}\n\n{body}"))
    return docs


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build/query a HiRAG index from normalized markdown output.")
    parser.add_argument("--input-dir", default=_DEFAULT_INPUT_DIR, help="Normalized markdown folder.")
    parser.add_argument("--working-dir", default=_DEFAULT_WORKING_DIR, help="HiRAG storage cache directory.")
    parser.add_argument("--limit", type=int, default=_DEFAULT_LIMIT, help="Limit markdown files to insert (0 means all).")
    parser.add_argument(
        "--insert-batch-size",
        type=int,
        default=8,
        help="Number of documents to insert per HiRAG insert call (higher is usually faster).",
    )
    parser.add_argument("--config-file", default=_DEFAULT_CONFIG_FILE, help="Optional key=value config file.")
    parser.add_argument("--env-file", default=_DEFAULT_ENV_FILE, help="Path to .env file.")
    parser.add_argument(
        "--skip-normalization",
        default="false",
        help="Skip text sanitation/normalization before API payload construction (true/false).",
    )

    parser.add_argument("--openai-api-key", default="", help="OpenAI API key (fallback: OPENAI_API_KEY env).")
    parser.add_argument("--openai-base-url", default="", help="OpenAI compatible base URL (optional).")
    parser.add_argument("--embedding-model", default="text-embedding-3-small", help="Embedding model name.")
    parser.add_argument("--embedding-dim", type=int, default=1536, help="Embedding vector dimension.")
    parser.add_argument("--chat-model", default="gpt-4o-mini", help="Chat model for response generation.")
    parser.add_argument("--temperature", type=float, default=None, help="Generation temperature for chat model.")
    parser.add_argument("--top-p", type=float, default=None, help="Generation top_p for chat model.")

    parser.add_argument("--enable-llm-cache", default="true", help="Enable HiRAG response cache (true/false).")
    parser.add_argument("--enable-hierachical-mode", default="true", help="Enable hierarchical retrieval mode.")
    parser.add_argument("--enable-naive-rag", default="true", help="Enable naive retrieval mode.")
    parser.add_argument("--embedding-batch-num", type=int, default=6, help="Embedding batch size.")
    parser.add_argument("--embedding-func-max-async", type=int, default=8, help="Max async embedding requests.")
    parser.add_argument(
        "--chunk-token-size",
        type=int,
        default=1200,
        help="Chunk token size for indexing (larger means fewer chunks, usually faster).",
    )
    parser.add_argument(
        "--chunk-overlap-token-size",
        type=int,
        default=100,
        help="Chunk overlap token size for indexing.",
    )
    parser.add_argument(
        "--entity-extract-max-gleaning",
        type=int,
        default=1,
        help="Extra relation extraction refinement loops per chunk (lower is faster).",
    )
    parser.add_argument(
        "--best-model-max-async",
        type=int,
        default=8,
        help="Max async LLM calls during indexing/query (higher can be faster if rate limits allow).",
    )

    # NEW: latency/throughput controls
    parser.add_argument(
        "--openai-max-inflight-embeddings",
        type=int,
        default=0,
        help="Max concurrent embedding requests from this runner (0 = unlimited).",
    )
    parser.add_argument(
        "--openai-max-inflight-chat",
        type=int,
        default=0,
        help="Max concurrent chat completion requests from this runner (0 = unlimited).",
    )
    parser.add_argument(
        "--openai-max-retries",
        type=int,
        default=5,
        help="Max retries for transient OpenAI API errors (429/5xx/timeouts).",
    )

    # NEW: custom_graph caps for speed
    parser.add_argument(
        "--custom-entity-scan-limit",
        type=int,
        default=500,
        help="custom_graph only: max candidate entities scanned in chunk text matching.",
    )
    parser.add_argument(
        "--custom-max-relations",
        type=int,
        default=200,
        help="custom_graph only: cap relation lines included in context.",
    )
    parser.add_argument(
        "--custom-max-source-chunks",
        type=int,
        default=40,
        help="custom_graph only: cap source chunks included in context.",
    )

    parser.add_argument("--skip-index", action="store_true", help="Skip insertion and only query existing index.")
    parser.add_argument("--query", default="", help="Question to ask after indexing.")
    parser.add_argument(
        "--mode",
        choices=["hi", "naive", "hi_nobridge", "hi_local", "hi_global", "hi_bridge", "custom_graph"],
        default=_DEFAULT_QUERY_MODE,
        help="Query mode.",
    )
    parser.add_argument("--top-k", type=int, default=20, help="Top-k entities for retrieval.")
    parser.add_argument("--top-m", type=int, default=10, help="Top-m entities per community.")
    parser.add_argument(
        "--strategy-top-k-chunks",
        type=int,
        default=8,
        help="Custom strategy only: number of top chunks to retrieve from chunk vector DB.",
    )
    parser.add_argument(
        "--strategy-hops",
        type=int,
        default=1,
        help="Custom strategy only: graph expansion hops from seed entities.",
    )
    parser.add_argument("--response-type", default="Single Paragraph", help="Answer style passed to HiRAG QueryParam.")
    parser.add_argument(
        "--max-token-for-text-unit",
        type=int,
        default=6000,
        help="Max tokens reserved for source text units in query context.",
    )
    parser.add_argument(
        "--max-token-for-local-context",
        type=int,
        default=6000,
        help="Max tokens reserved for local entity context.",
    )
    parser.add_argument(
        "--max-token-for-bridge-knowledge",
        type=int,
        default=3000,
        help="Max tokens reserved for bridge knowledge context.",
    )
    parser.add_argument(
        "--max-token-for-community-report",
        type=int,
        default=3000,
        help="Max tokens reserved for community report context.",
    )
    parser.add_argument(
        "--community-single-one",
        default="true",
        help="If true, use one community report in context when supported.",
    )
    return parser.parse_args()


def _is_retryable_exception(exc: Exception) -> bool:
    status = getattr(exc, "status_code", None)
    if isinstance(status, int) and (status == 429 or 500 <= status <= 599):
        return True
    if isinstance(exc, (TimeoutError, ConnectionError)):
        return True
    name = exc.__class__.__name__.lower()
    if "timeout" in name or "connection" in name or "ratelimit" in name:
        return True
    return False


async def _with_retries(coro_factory: Callable[[], "asyncio.Future"], max_retries: int) -> object:
    attempt = 0
    while True:
        try:
            return await coro_factory()
        except Exception as exc:  # noqa: BLE001
            attempt += 1
            if attempt > max_retries or not _is_retryable_exception(exc):
                raise
            base = min(20.0, 0.5 * (2 ** (attempt - 1)))
            await asyncio.sleep(base + random.random() * 0.25)


def main() -> None:
    args = parse_args()
    txt_config = read_txt_config(args.config_file)

    def pick_value(cli_value, cli_default, config_key):
        if cli_value != cli_default:
            return cli_value
        return txt_config.get(config_key, cli_value)

    input_dir_value = pick_value(args.input_dir, _DEFAULT_INPUT_DIR, "input_dir")
    working_dir_value = pick_value(args.working_dir, _DEFAULT_WORKING_DIR, "working_dir")
    env_file_value = pick_value(args.env_file, _DEFAULT_ENV_FILE, "env_file")
    skip_normalization_value = parse_bool(str(pick_value(args.skip_normalization, "false", "skip_normalization")))
    openai_api_key_value = pick_value(args.openai_api_key, "", "openai_api_key")
    openai_base_url_value = pick_value(args.openai_base_url, "", "openai_base_url")
    embedding_model_value = pick_value(args.embedding_model, "text-embedding-3-small", "embedding_model")
    embedding_dim_value = int(pick_value(args.embedding_dim, 1536, "embedding_dim"))
    chat_model_value = pick_value(args.chat_model, "gpt-4o-mini", "chat_model")
    temperature_value = parse_optional_float(pick_value(args.temperature, None, "temperature"))
    top_p_value = parse_optional_float(pick_value(args.top_p, None, "top_p"))

    enable_llm_cache_value = parse_bool(str(pick_value(args.enable_llm_cache, "true", "enable_llm_cache")))
    enable_hierachical_mode_value = parse_bool(str(pick_value(args.enable_hierachical_mode, "true", "enable_hierachical_mode")))
    enable_naive_rag_value = parse_bool(str(pick_value(args.enable_naive_rag, "true", "enable_naive_rag")))

    embedding_batch_num_value = int(pick_value(args.embedding_batch_num, 6, "embedding_batch_num"))
    embedding_func_max_async_value = int(pick_value(args.embedding_func_max_async, 8, "embedding_func_max_async"))
    chunk_token_size_value = int(pick_value(args.chunk_token_size, 1200, "chunk_token_size"))
    chunk_overlap_token_size_value = int(pick_value(args.chunk_overlap_token_size, 100, "chunk_overlap_token_size"))
    entity_extract_max_gleaning_value = int(pick_value(args.entity_extract_max_gleaning, 1, "entity_extract_max_gleaning"))
    best_model_max_async_value = int(pick_value(args.best_model_max_async, 8, "best_model_max_async"))

    limit_value = args.limit
    if args.limit == _DEFAULT_LIMIT and "limit" in txt_config:
        limit_value = int(txt_config["limit"])
    insert_batch_size_value = int(pick_value(args.insert_batch_size, 8, "insert_batch_size"))

    response_type_value = pick_value(args.response_type, "Single Paragraph", "response_type")
    max_token_for_text_unit_value = int(pick_value(args.max_token_for_text_unit, 6000, "max_token_for_text_unit"))
    max_token_for_local_context_value = int(pick_value(args.max_token_for_local_context, 6000, "max_token_for_local_context"))
    max_token_for_bridge_knowledge_value = int(pick_value(args.max_token_for_bridge_knowledge, 3000, "max_token_for_bridge_knowledge"))
    max_token_for_community_report_value = int(pick_value(args.max_token_for_community_report, 3000, "max_token_for_community_report"))
    community_single_one_value = parse_bool(str(pick_value(args.community_single_one, "true", "community_single_one")))
    strategy_top_k_chunks_value = int(pick_value(args.strategy_top_k_chunks, 8, "strategy_top_k_chunks"))
    strategy_hops_value = int(pick_value(args.strategy_hops, 1, "strategy_hops"))

    repo_root = Path(__file__).resolve().parent
    input_dir = (repo_root / str(input_dir_value)).resolve()
    working_dir = (repo_root / str(working_dir_value)).resolve()
    env_file = (repo_root / str(env_file_value)).resolve()

    load_env_file(env_file)

    if not input_dir.exists():
        raise FileNotFoundError(f"Input markdown directory not found: {input_dir}")

    HiRAG, QueryParam = resolve_hi_import(repo_root)

    resolved_api_key = openai_api_key_value or os.getenv("OPENAI_API_KEY", "")
    resolved_base_url = openai_base_url_value or os.getenv("OPENAI_BASE_URL", "")
    client_kwargs: dict = {}
    if resolved_api_key:
        client_kwargs["api_key"] = resolved_api_key
    if resolved_base_url:
        client_kwargs["base_url"] = resolved_base_url

    # PERF: reuse a single client for all calls
    openai_async_client = AsyncOpenAI(**client_kwargs)

    # PERF: optional inflight limits to stabilize throughput and latency
    embedding_sem: Optional[asyncio.Semaphore] = None
    chat_sem: Optional[asyncio.Semaphore] = None
    if args.openai_max_inflight_embeddings and args.openai_max_inflight_embeddings > 0:
        embedding_sem = asyncio.Semaphore(args.openai_max_inflight_embeddings)
    if args.openai_max_inflight_chat and args.openai_max_inflight_chat > 0:
        chat_sem = asyncio.Semaphore(args.openai_max_inflight_chat)

    usage_stats = TokenUsageStats()

    @wrap_embedding_func_with_attrs(embedding_dim=embedding_dim_value, max_token_size=8192)
    async def openai_embedding(texts: list[str]) -> np.ndarray:
        nonlocal usage_stats

        if skip_normalization_value:
            safe_texts = [t if isinstance(t, str) else str(t) for t in texts]
        else:
            safe_texts = [sanitize_text(t if isinstance(t, str) else str(t)) for t in texts]

        async def _call():
            t0 = time.perf_counter()
            resp = await openai_async_client.embeddings.create(
                model=embedding_model_value,
                input=safe_texts,
                encoding_format="float",
            )
            usage_stats.embedding_wall_seconds += time.perf_counter() - t0
            usage_stats.embedding_api_calls += 1
            usage_stats.embedding_prompt_tokens += _usage_value(resp.usage, "prompt_tokens")
            usage_stats.embedding_total_tokens += _usage_value(resp.usage, "total_tokens")
            return resp

        if embedding_sem is None:
            response = await _with_retries(_call, max_retries=max(0, int(args.openai_max_retries)))
        else:
            async with embedding_sem:
                response = await _with_retries(_call, max_retries=max(0, int(args.openai_max_retries)))

        return np.array([item.embedding for item in response.data])

    async def openai_complete(prompt, system_prompt=None, history_messages=None, **kwargs) -> str:
        nonlocal usage_stats

        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        if history_messages:
            messages.extend(history_messages)
        messages.append({"role": "user", "content": prompt})
        if not skip_normalization_value:
            messages = sanitize_messages(messages)

        hashing_kv = kwargs.pop("hashing_kv", None)
        safe_kwargs = sanitize_chat_kwargs(kwargs)
        if temperature_value is not None and "temperature" not in safe_kwargs:
            safe_kwargs["temperature"] = temperature_value
        if top_p_value is not None and "top_p" not in safe_kwargs:
            safe_kwargs["top_p"] = top_p_value

        if hashing_kv is not None:
            from hirag._utils import compute_args_hash  # type: ignore

            args_hash = compute_args_hash(chat_model_value, messages)
            cached = await hashing_kv.get_by_id(args_hash)
            if cached is not None:
                usage_stats.chat_cache_hits += 1
                return cached["return"]
        else:
            args_hash = None

        payload = {
            "model": str(chat_model_value) if skip_normalization_value else sanitize_text(str(chat_model_value)),
            "messages": messages,
            **safe_kwargs,
        }
        json.dumps(payload, ensure_ascii=False, allow_nan=False)

        async def _call():
            t0 = time.perf_counter()
            resp = await openai_async_client.chat.completions.create(**payload)
            usage_stats.chat_wall_seconds += time.perf_counter() - t0
            return resp

        try:
            if chat_sem is None:
                response = await _with_retries(_call, max_retries=max(0, int(args.openai_max_retries)))
            else:
                async with chat_sem:
                    response = await _with_retries(_call, max_retries=max(0, int(args.openai_max_retries)))
        except BadRequestError as exc:
            err_text = str(exc)
            if "parse the JSON body" not in err_text:
                raise

            fallback_payload = {"model": str(chat_model_value), "messages": ultra_sanitize_messages(messages)}
            json.dumps(fallback_payload, ensure_ascii=False, allow_nan=False)

            async def _fallback_call():
                t0 = time.perf_counter()
                resp = await openai_async_client.chat.completions.create(**fallback_payload)
                usage_stats.chat_wall_seconds += time.perf_counter() - t0
                return resp

            if chat_sem is None:
                response = await _with_retries(_fallback_call, max_retries=max(0, int(args.openai_max_retries)))
            else:
                async with chat_sem:
                    response = await _with_retries(_fallback_call, max_retries=max(0, int(args.openai_max_retries)))

        usage_stats.chat_api_calls += 1
        usage_stats.chat_prompt_tokens += _usage_value(response.usage, "prompt_tokens")
        usage_stats.chat_completion_tokens += _usage_value(response.usage, "completion_tokens")
        usage_stats.chat_total_tokens += _usage_value(response.usage, "total_tokens")
        content = response.choices[0].message.content or ""

        if hashing_kv is not None and args_hash is not None:
            await hashing_kv.upsert({args_hash: {"return": content, "model": chat_model_value}})

        return content

    graph = HiRAG(
        working_dir=str(working_dir),
        enable_llm_cache=enable_llm_cache_value,
        embedding_func=openai_embedding,
        best_model_func=openai_complete,
        cheap_model_func=openai_complete,
        enable_hierachical_mode=enable_hierachical_mode_value,
        chunk_token_size=max(200, chunk_token_size_value),
        chunk_overlap_token_size=max(0, min(chunk_overlap_token_size_value, max(0, chunk_token_size_value - 1))),
        embedding_batch_num=embedding_batch_num_value,
        embedding_func_max_async=embedding_func_max_async_value,
        entity_extract_max_gleaning=max(0, entity_extract_max_gleaning_value),
        best_model_max_async=max(1, best_model_max_async_value),
        enable_naive_rag=enable_naive_rag_value,
    )

    async def run_custom_strategy_query(query: str):
        from hirag.prompt import GRAPH_FIELD_SEP  # type: ignore
        from hirag._utils import always_get_an_event_loop  # type: ignore

        _ = always_get_an_event_loop  # silence lint if not used by runtime

        nx_graph = graph.chunk_entity_relation_graph._graph
        if nx_graph is None or nx_graph.number_of_nodes() == 0:
            return "No graph data found in current working_dir. Run indexing first without --skip-index."

        seed_entities: set[str] = set()
        chunk_ids_from_search: set[str] = set()
        candidate_entities: set[str] = set()

        if graph.entities_vdb is not None:
            entity_hits = await graph.entities_vdb.query(query, top_k=max(1, args.top_k))
            for hit in entity_hits:
                entity_name = normalize_entity_name(hit.get("entity_name", ""))
                if entity_name:
                    upper = entity_name.upper()
                    seed_entities.add(upper)
                    candidate_entities.add(upper)

        if graph.chunks_vdb is not None and strategy_top_k_chunks_value > 0:
            chunk_hits = await graph.chunks_vdb.query(query, top_k=max(1, strategy_top_k_chunks_value))
            for hit in chunk_hits:
                hit_id = str(hit.get("id", "")).strip()
                if hit_id:
                    chunk_ids_from_search.add(hit_id)

        node_lookup: dict[str, str] = {}
        for node_id in nx_graph.nodes:
            normalized = normalize_entity_name(node_id)
            if normalized:
                node_lookup[normalized.upper()] = node_id

        if chunk_ids_from_search:
            chunk_dps = await graph.text_chunks.get_by_ids(list(chunk_ids_from_search))
            content_list = [dp.get("content", "") for dp in chunk_dps if dp is not None]
            joined = "\n".join(content_list).upper()

            candidates: list[str] = list(candidate_entities)
            if len(candidates) < args.custom_entity_scan_limit:
                for name in node_lookup.keys():
                    if name in candidate_entities:
                        continue
                    if len(name) < 4:
                        continue
                    candidates.append(name)
                    if len(candidates) >= args.custom_entity_scan_limit:
                        break
            else:
                candidates = candidates[: args.custom_entity_scan_limit]

            for normalized_name in candidates:
                if normalized_name in joined:
                    seed_entities.add(normalized_name)

        if not seed_entities:
            query_upper = query.upper()
            scan_cap = max(100, int(args.custom_entity_scan_limit))
            for i, normalized_name in enumerate(node_lookup.keys()):
                if i >= scan_cap:
                    break
                if len(normalized_name) < 4:
                    continue
                if normalized_name in query_upper:
                    seed_entities.add(normalized_name)

        if not seed_entities:
            return "No relevant entities found from query/chunks. Try a more specific query or increase top-k."

        hops = max(1, min(2, strategy_hops_value))
        expanded_nodes: set[str] = set()
        frontier: set[str] = set()
        for seed in seed_entities:
            original = node_lookup.get(seed)
            if original is not None:
                frontier.add(original)
                expanded_nodes.add(original)

        for _ in range(hops):
            next_frontier: set[str] = set()
            for node in frontier:
                for neighbor in nx_graph.neighbors(node):
                    if neighbor not in expanded_nodes:
                        expanded_nodes.add(neighbor)
                        next_frontier.add(neighbor)
            frontier = next_frontier
            if not frontier:
                break

        entity_lines: list[str] = []
        relation_lines: list[str] = []
        source_chunk_ids: set[str] = set(chunk_ids_from_search)

        for node in sorted(expanded_nodes):
            node_data = nx_graph.nodes.get(node, {})
            entity_type = node_data.get("entity_type", "UNKNOWN")
            description = sanitize_text(str(node_data.get("description", "")))
            entity_lines.append(f"- {normalize_entity_name(node)} [{entity_type}]: {description}")
            for cid in split_source_ids(str(node_data.get("source_id", "")), GRAPH_FIELD_SEP):
                source_chunk_ids.add(cid)

        # cap relation lines for latency
        for src, tgt, edge_data in nx_graph.edges(data=True):
            if len(relation_lines) >= max(10, int(args.custom_max_relations)):
                break
            if src in expanded_nodes and tgt in expanded_nodes:
                desc = sanitize_text(str(edge_data.get("description", "")))
                weight = edge_data.get("weight", "")
                relation_lines.append(
                    f"- {normalize_entity_name(src)} -> {normalize_entity_name(tgt)} (weight={weight}): {desc}"
                )

        source_docs: list[str] = []
        if source_chunk_ids:
            limited_ids = list(source_chunk_ids)[: max(5, int(args.custom_max_source_chunks))]
            chunk_rows = await graph.text_chunks.get_by_ids(limited_ids)
            for row in chunk_rows:
                if row is None:
                    continue
                content = sanitize_text(str(row.get("content", "")))
                if content:
                    source_docs.append(content)

        def join_and_trim(lines: list[str], max_chars: int) -> str:
            text = "\n".join(lines)
            if len(text) <= max_chars:
                return text
            return text[:max_chars] + "\n...[truncated]"

        entities_context = join_and_trim(entity_lines, max(800, max_token_for_local_context_value * 4))
        relations_context = join_and_trim(relation_lines, max(800, max_token_for_bridge_knowledge_value * 4))
        sources_context = join_and_trim(source_docs, max(1200, max_token_for_text_unit_value * 4))

        system_prompt = (
            "You are a RAG answer assistant. Answer only using the provided context. "
            "If context is insufficient, say you cannot confirm from indexed documents.\n\n"
            f"Response style: {response_type_value}\n\n"
            "[Entities]\n"
            f"{entities_context}\n\n"
            "[Relations]\n"
            f"{relations_context}\n\n"
            "[Source Chunks]\n"
            f"{sources_context}"
        )

        return await openai_complete(query, system_prompt=system_prompt)

    try:
        if not args.skip_index:
            docs = collect_markdown_docs(input_dir=input_dir, limit=max(0, limit_value))
            if not docs:
                print("No markdown files found to index.")
                return

            print(f"Indexing {len(docs)} markdown documents from: {input_dir}")
            inserted = 0
            failed = 0
            progress_mark = 0
            batch_size = max(1, insert_batch_size_value)
            for batch_start in range(0, len(docs), batch_size):
                batch = docs[batch_start : batch_start + batch_size]
                batch_contents = [doc_content for _, doc_content in batch]
                batch_t0 = time.perf_counter()
                try:
                    graph.insert(batch_contents)
                    inserted += len(batch)
                    print(
                        f"[{batch_start + 1}-{batch_start + len(batch)}/{len(docs)}] Indexed batch ({len(batch)} docs) in {time.perf_counter() - batch_t0:.2f}s"
                    )
                    while inserted >= progress_mark + 10:
                        progress_mark += 10
                        print_progress_usage(usage_stats, progress_mark)
                except Exception as exc:  # noqa: BLE001
                    print(
                        f"[{batch_start + 1}-{batch_start + len(batch)}/{len(docs)}] Batch failed, fallback to per-doc ({exc})"
                    )
                    for idx, (source_path, doc_content) in enumerate(batch, start=batch_start + 1):
                        doc_t0 = time.perf_counter()
                        try:
                            graph.insert(doc_content)
                            inserted += 1
                            print(f"[{idx}/{len(docs)}] Indexed: {source_path} in {time.perf_counter() - doc_t0:.2f}s")
                            while inserted >= progress_mark + 10:
                                progress_mark += 10
                                print_progress_usage(usage_stats, progress_mark)
                        except Exception as inner_exc:  # noqa: BLE001
                            failed += 1
                            print(f"[{idx}/{len(docs)}] Index failed: {source_path} ({inner_exc})")

            print(f"Index summary: success={inserted}, failed={failed}")
            print(f"Index complete. Working directory: {working_dir}")
        else:
            print(f"Skip indexing enabled. Using existing index in: {working_dir}")

        if args.query:
            print(f"\nQuery mode: {args.mode}")
            print(f"Question: {args.query}\n")
            query_t0 = time.perf_counter()
            if args.mode == "custom_graph":
                from hirag._utils import always_get_an_event_loop  # type: ignore

                loop = always_get_an_event_loop()
                answer = loop.run_until_complete(run_custom_strategy_query(args.query))
            else:
                param = QueryParam(
                    mode=args.mode,
                    top_k=args.top_k,
                    top_m=args.top_m,
                    response_type=response_type_value,
                    max_token_for_text_unit=max(500, max_token_for_text_unit_value),
                    max_token_for_local_context=max(500, max_token_for_local_context_value),
                    max_token_for_bridge_knowledge=max(500, max_token_for_bridge_knowledge_value),
                    max_token_for_community_report=max(500, max_token_for_community_report_value),
                    community_single_one=community_single_one_value,
                )
                answer = graph.query(args.query, param=param)
            print(answer)
            print(f"\nQuery total wall time (s): {time.perf_counter() - query_t0:.2f}")
        else:
            print("No query provided. Use --query to run retrieval and generation.")
    finally:
        print_token_usage_summary(usage_stats)


if __name__ == "__main__":
    main()