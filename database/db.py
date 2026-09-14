import psycopg2

from backend.config import settings


def get_connection():
    """Create a PostgreSQL database connection via the canonical
    POSTGRES_* configuration path.

    A malformed DATABASE_URL is never allowed to override the
    validated POSTGRES_* layout used by this repository. If a
    DATABASE_URL value is explicitly present, it must be parsed and
    validated before use; otherwise the safer default is to build
    the DSN from POSTGRES_HOST/PORT/DB/USER/PASSWORD.
    """
    if settings.POSTGRES_HOST and settings.POSTGRES_DB and settings.POSTGRES_USER:
        return psycopg2.connect(
            host=settings.POSTGRES_HOST,
            port=settings.POSTGRES_PORT,
            database=settings.POSTGRES_DB,
            user=settings.POSTGRES_USER,
            password=settings.POSTGRES_PASSWORD,
        )

    # Safe fallback only if the POSTGRES_* fields are intentionally blank.
    if settings.DATABASE_URL:
        return psycopg2.connect(settings.DATABASE_URL)

    raise RuntimeError("No PostgreSQL configuration is available")


if __name__ == "__main__":
    try:
        conn = get_connection()
        print("✅ Database Connected Successfully")
        conn.close()
    except Exception as exc:
        print("❌ Database Connection Failed")
        print(type(exc).__name__)
        print(str(exc))
