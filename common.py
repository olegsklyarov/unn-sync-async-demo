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

# Список из 25 SQL запросов для выполнения
# Используется pg_sleep() для создания задержки, чтобы продемонстрировать
# разницу в производительности между синхронной и асинхронной версиями
queries = [
    "SELECT pg_sleep(0.5), 1",
    "SELECT pg_sleep(0.5), 2",
    "SELECT pg_sleep(0.5), 3",
    "SELECT pg_sleep(0.5), 4",
    "SELECT pg_sleep(0.5), 5",
    "SELECT pg_sleep(0.5), version()",
    "SELECT pg_sleep(0.5), current_timestamp",
    "SELECT pg_sleep(0.5), current_database()",
    "SELECT pg_sleep(0.5), pg_backend_pid()",
    "SELECT pg_sleep(0.5), 10",
    "SELECT pg_sleep(0.5), 11",
    "SELECT pg_sleep(0.5), 12",
    "SELECT pg_sleep(0.5), 13",
    "SELECT pg_sleep(0.5), 14",
    "SELECT pg_sleep(0.5), 15",
    "SELECT pg_sleep(0.5), 16",
    "SELECT pg_sleep(0.5), 17",
    "SELECT pg_sleep(0.5), 18",
    "SELECT pg_sleep(0.5), 19",
    "SELECT pg_sleep(0.5), 20",
    "SELECT pg_sleep(0.5), 21",
    "SELECT pg_sleep(0.5), 22",
    "SELECT pg_sleep(0.5), 23",
    "SELECT pg_sleep(0.5), 24",
    "SELECT pg_sleep(0.5), 25",
]

# Параметры подключения к PostgreSQL
DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "database": "postgres",
    "user": "postgres",
    "password": "postgres",
}
