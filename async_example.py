#!/usr/bin/env python3

import asyncio
import httpx
from functools import wraps
import time

from common import urls, logger


def measure_time_async(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start_time = time.time()
        logger.info(f"Start: {func.__name__}")
        result = await func(*args, **kwargs)
        elapsed = time.time() - start_time
        logger.info(f"Finish: {func.__name__} took {elapsed:.3f} seconds")
        return result

    return wrapper


@measure_time_async
async def fetch_url(client: httpx.AsyncClient, url: str) -> httpx.Response:
    logger.info(f"Fetching: {url}")
    return await client.get(url)


@measure_time_async
async def main():
    async with httpx.AsyncClient() as client:
        tasks = [fetch_url(client, url) for url in urls]
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
