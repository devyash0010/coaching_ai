from sentence_transformers import SentenceTransformer
from pgvector.psycopg2 import register_vector

from backend.config import settings
from database.db import get_connection

# Load embedding model once, centralize through one environment variable.
model = SentenceTransformer(settings.EMBEDDING_MODEL)


class Retriever:
    def __init__(self, top_k: int = 5):
        self.top_k = top_k
        self.conn = get_connection()
        register_vector(self.conn)
        self.cur = self.conn.cursor()

    def search(self, question: str, top_k: int | None = None, subject: str | None = None):
        """Return a clean structure with semantic context only.

        This file is responsible for retrieval only. It should not generate
        answers, and it should not contain analytics/business logic.
        """
        top_k = top_k or self.top_k
        query_embedding = model.encode(question).tolist()

        if subject:
            sql = """
                SELECT
                    source_id,
                    source_type,
                    chunk_text,
                    metadata,
                    1 - (embedding <=> %s::vector) AS similarity
                FROM embeddings
                WHERE metadata->>'subject' = %s
                ORDER BY embedding <=> %s::vector
                LIMIT %s;
            """
            self.cur.execute(
                sql, (query_embedding, subject, query_embedding, top_k))
        else:
            sql = """
                SELECT
                    source_id,
                    source_type,
                    chunk_text,
                    metadata,
                    1 - (embedding <=> %s::vector) AS similarity
                FROM embeddings
                ORDER BY embedding <=> %s::vector
                LIMIT %s;
            """
            self.cur.execute(sql, (query_embedding, query_embedding, top_k))

        rows = self.cur.fetchall()
        return [
            {
                "source_id": row[0],
                "source_type": row[1],
                "content": row[2],
                "metadata": row[3],
                "similarity": float(row[4]),
            }
            for row in rows
        ]

    def close(self):
        self.cur.close()
        self.conn.close()


if __name__ == "__main__":
    retriever = Retriever()
    question = input("Ask: ")
    results = retriever.search(question)
    print("\nTop Results:\n")
    for row in results:
        print("-" * 50)
        print(f"Student ID : {row['source_id']}")
        print(f"Type       : {row['source_type']}")
        print(f"Similarity : {row['similarity']:.4f}")
        print(row["content"])
    retriever.close()