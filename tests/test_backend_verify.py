from backend.config import settings
from database.db import get_connection
from rag.retriever import Retriever
from rag.rag_pipeline import RAGPipeline
from llm.ollama_client import generate_response
from analytics.performance import analyze_performance
from fastapi.testclient import TestClient
from backend.main import app


def test_config_and_db_connection():
    assert settings.POSTGRES_HOST == "localhost"
    assert settings.POSTGRES_PORT == 5433
    assert settings.POSTGRES_DB == "coaching_ai"
    assert settings.POSTGRES_USER == "postgres"
    assert bool(settings.POSTGRES_PASSWORD)

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT 1")
    assert cur.fetchone()[0] == 1
    cur.execute("SELECT current_database()")
    assert cur.fetchone()[0] == "coaching_ai"
    cur.close()
    conn.close()


def test_pgvector_and_embeddings_metadata():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT extname, extversion FROM pg_extension WHERE extname = 'vector'")
    row = cur.fetchone()
    assert row is not None
    assert row[0] == "vector"
    assert row[1] == "0.8.5"

    cur.execute("SELECT vector_dims(embedding) FROM embeddings WHERE embedding IS NOT NULL LIMIT 1")
    dim = cur.fetchone()[0]
    assert dim == 768

    cur.execute("SELECT COUNT(*) FROM embeddings")
    count = cur.fetchone()[0]
    assert count == 100
    cur.close()
    conn.close()


def test_retriever_returns_real_context():
    retriever = Retriever(top_k=3)
    rows = retriever.search("Which students are weak in Physics?", top_k=3)
    retriever.close()
    assert isinstance(rows, list)
    assert len(rows) >= 1
    for row in rows:
        assert "source_id" in row
        assert "source_type" in row
        assert "content" in row
        assert "metadata" in row
        assert "similarity" in row


def test_ollama_wrapper_and_rag_pipeline():
    answer = generate_response("Hello from coaching AI")
    assert isinstance(answer, str)
    assert len(answer.strip()) > 0

    pipeline = RAGPipeline()
    ctx = pipeline.build_context("Which students are weak in Physics?", subject=None)
    assert ctx.retrieved_materials
    assert ctx.sources

    answer = pipeline.answer("Which students are weak in Physics?", subject=None)
    assert isinstance(answer, str)
    assert len(answer.strip()) > 0


def test_analytics_and_fastapi_health():
    result = analyze_performance("JEE001")
    assert result["student_id"] == "JEE001"
    assert result["grade"] in {"A+", "A", "B", "C", "D", "F"}

    client = TestClient(app)
    health = client.get("/health")
    assert health.status_code == 200
    assert health.json()["status"] == "ok"

    docs = client.get("/docs")
    assert docs.status_code == 200
