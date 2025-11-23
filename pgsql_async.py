#!/usr/bin/env python3

import asyncio
import asyncpg
from common import measure_time, logger, queries, DB_CONFIG


@measure_time
async def execute_query(pool: asyncpg.Pool, query: str) -> list:
    logger.info(f"Executing: {query}")
    async with pool.acquire() as conn:
        return await conn.fetch(query)


@measure_time
async def main():
    pool = await asyncpg.create_pool(**DB_CONFIG, min_size=1, max_size=15)
    try:
        tasks = [execute_query(pool, query) for query in queries]
        await asyncio.gather(*tasks)
    finally:
        await pool.close()


if __name__ == "__main__":
    asyncio.run(main())

