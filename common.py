import logging
import time
import inspect
from functools import wraps

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s.%(msecs)03d] %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)


def measure_time(func):
    """
    Универсальный декоратор для замера времени выполнения функции.
    Работает как для синхронных, так и для асинхронных функций.
    """
    is_async = inspect.iscoroutinefunction(func)
    func_name = func.__name__

    def log_timing(start_time):
        elapsed = time.time() - start_time
        logger.info(f"Finish: {func_name} took {elapsed:.3f} seconds")

    @wraps(func)
    def sync_wrapper(*args, **kwargs):
        start_time = time.time()
        logger.info(f"Start: {func_name}")
        result = func(*args, **kwargs)
        log_timing(start_time)
        return result

    @wraps(func)
    async def async_wrapper(*args, **kwargs):
        start_time = time.time()
        logger.info(f"Start: {func_name}")
        result = await func(*args, **kwargs)
        log_timing(start_time)
        return result

    return async_wrapper if is_async else sync_wrapper


urls = [
    "https://jsonplaceholder.typicode.com/users/1",
    "https://jsonplaceholder.typicode.com/users/2",
    "https://jsonplaceholder.typicode.com/users/3",
    "https://jsonplaceholder.typicode.com/users/4",
    "https://jsonplaceholder.typicode.com/users/5",
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/posts/2",
    "https://jsonplaceholder.typicode.com/posts/3",
    "https://jsonplaceholder.typicode.com/posts/4",
    "https://jsonplaceholder.typicode.com/posts/5",
    "https://jsonplaceholder.typicode.com/comments/1",
    "https://jsonplaceholder.typicode.com/comments/2",
    "https://jsonplaceholder.typicode.com/comments/3",
    "https://jsonplaceholder.typicode.com/comments/4",
    "https://jsonplaceholder.typicode.com/comments/5",
    "https://jsonplaceholder.typicode.com/albums/1",
    "https://jsonplaceholder.typicode.com/albums/2",
    "https://jsonplaceholder.typicode.com/albums/3",
    "https://jsonplaceholder.typicode.com/photos/1",
    "https://jsonplaceholder.typicode.com/photos/2",
]
