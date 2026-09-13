import psycopg2
import os

def get_connection():
    """
    Establishes a connection to the PostgreSQL database using environment variables.
    """
    try:
        connection = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )
        return connection
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        raise