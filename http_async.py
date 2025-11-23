#!/usr/bin/env python3

import asyncio
import httpx
from common import measure_time, urls, logger


@measure_time
async def fetch_url(client: httpx.AsyncClient, url: str) -> httpx.Response:
    logger.info(f"Fetching: {url}")
    return await client.get(url)


@measure_time
async def main():
    async with httpx.AsyncClient() as client:
        tasks = [fetch_url(client, url) for url in urls]
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
