import os
from dotenv import load_dotenv

load_dotenv()


DATABASE_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": os.getenv("DB_PORT", "5433"),
    "database": os.getenv("DB_NAME", "coaching_ai"),
    "user": os.getenv("DB_USER", "postgres"),
    "password": os.getenv("DB_PASSWORD", "")
}


SECRET_KEY = "coaching_ai_secret_key"

ALGORITHM = "HS256"