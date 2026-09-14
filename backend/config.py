from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


PROJECT_ROOT = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    """Central environment/config object for the application.

    Keep environment variables in one place so backend, database, llm,
    embedding, and RAG modules can share the same values without duplicating
    a second configuration or hardcoded password.
    """

    model_config = SettingsConfigDict(
        env_file=str(PROJECT_ROOT / ".env"),
        env_file_encoding="utf-8",
        extra="ignore",
    )

    DATABASE_URL: str = ""
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5433
    POSTGRES_DB: str = "coaching_ai"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = ""

    OLLAMA_HOST: str = "http://localhost:11434"
    OLLAMA_MODEL: str = "qwen2.5:3b"
    EMBEDDING_MODEL: str = "all-mpnet-base-v2"

    BACKEND_URL: str = "http://localhost:8000"
    FRONTEND_URL: str = "http://localhost:3000"
    CORS_ORIGINS: str = "http://localhost:3000,http://127.0.0.1:3000"

    SECRET_KEY: str = "dev-secret-key-change-me"
    ALGORITHM: str = "HS256"


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
