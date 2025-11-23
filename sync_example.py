#!/usr/bin/env python3

import urllib.request
import time
from functools import wraps
import logging


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s.%(msecs)03d] %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)


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
def fetch_pokemon(pokemon_id) -> None:
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    logger.info(f"Fetching: {url}")
    with urllib.request.urlopen(url, timeout=20) as response:
        response.read()


@measure_time
def main():
    for pokemon_id in [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]:
        fetch_pokemon(pokemon_id)


if __name__ == "__main__":
    main()
