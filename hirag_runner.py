import argparse
import asyncio
import logging
from some_openai_library import AsyncOpenAI

# Global semaphore for managing inflight requests
semaphore_embeddings = asyncio.Semaphore(10)  # Default limit
semaphore_chat = asyncio.Semaphore(10)  # Default limit

async def create_embeddings_with_retry(...):
    # implementation with retry logic and backoff
    pass

async def create_chat_with_retry(...):
    # implementation with retry logic and backoff
    pass

async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--openai-max-inflight-embeddings', type=int, default=10, help='Max inflight embeddings requests')
    parser.add_argument('--openai-max-inflight-chat', type=int, default=10, help='Max inflight chat requests')
    parser.add_argument('--custom-entity-scan-limit', type=int, default=500, help='Limit of candidates for custom graph seeding')
    parser.add_argument('--custom-max-relations', type=int, default=200, help='Max relations to include')
    parser.add_argument('--custom-max-source-chunks', type=int, default=40, help='Max source chunks to include')
    args = parser.parse_args()

    # Set max inflight limits
    semaphore_embeddings = asyncio.Semaphore(args.openai_max_inflight_embeddings)
    semaphore_chat = asyncio.Semaphore(args.openai_max_inflight_chat)

    # Main logic here

if __name__ == '__main__':
    asyncio.run(main())
