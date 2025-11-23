#!/usr/bin/env python3

import urllib.request
from common import measure_time, urls, logger


@measure_time
def fetch_url(url: str) -> bytes:
    logger.info(f"Fetching: {url}")
    with urllib.request.urlopen(url, timeout=20) as response:
        return response.read()


@measure_time
def main():
    for url in urls:
        fetch_url(url)


if __name__ == "__main__":
    main()
