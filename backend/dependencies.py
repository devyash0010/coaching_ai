from collections.abc import Generator

from database.db import get_connection


def get_db() -> Generator:
    """Reusable database dependency for FastAPI.

    Returns a PostgreSQL cursor/connection-style provider that can be
    used by FastAPI routes and services until the full service layer is
    replaced by richer route-specific dependencies.
    """
    conn = get_connection()
    try:
        yield conn
    finally:
        conn.close()
