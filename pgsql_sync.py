#!/usr/bin/env python3

import pg8000
from common import measure_time, logger, queries, DB_CONFIG


@measure_time
def execute_query(conn: pg8000.Connection, query: str) -> list:
    logger.info(f"Executing: {query}")
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result


@measure_time
def main():
    conn = pg8000.connect(**DB_CONFIG)
    try:
        for query in queries:
            execute_query(conn, query)
    finally:
        conn.close()


if __name__ == "__main__":
    main()

