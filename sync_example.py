#!/usr/bin/env python3

import urllib.request
import time
from functools import wraps
from common import urls, logger


def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        logger.info(f"Start: {func.__name__}")
        result = func(*args, **kwargs)
        elapsed = time.time() - start_time
        logger.info(f"Finish: {func.__name__} took {elapsed:.3f} seconds")
        return result

    return wrapper


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
