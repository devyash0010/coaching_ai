from sentence_transformers import SentenceTransformer
from pgvector.psycopg2 import register_vector
from database.db import get_connection

# Load embedding model once
model = SentenceTransformer("all-mpnet-base-v2")


class Retriever:

    def __init__(self):
        self.conn = get_connection()
        register_vector(self.conn)
        self.cur = self.conn.cursor()

    def search(self, question, top_k=5):
        # Convert question to embedding
        query_embedding = model.encode(question).tolist()

        # Search similar records
        self.cur.execute("""
            SELECT
                source_id,
                source_type,
                chunk_text,
                embedding <=> %s::vector AS distance
            FROM embeddings
            ORDER BY embedding <=> %s::vector
            LIMIT %s;
        """, (query_embedding, query_embedding, top_k))

        return self.cur.fetchall()

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
        print(f"Student ID : {row[0]}")
        print(f"Type       : {row[1]}")
        print(f"Distance   : {row[3]:.4f}")
        print(row[2])

    retriever.close()