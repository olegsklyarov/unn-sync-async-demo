#!/usr/bin/env python3

import asyncio
import aiohttp
from common import measure_time, urls, logger


@measure_time
async def fetch_url(session: aiohttp.ClientSession, url: str) -> aiohttp.ClientResponse:
    logger.info(f"Fetching: {url}")
    async with session.get(url) as response:
        await response.read()
        return response


@measure_time
async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
