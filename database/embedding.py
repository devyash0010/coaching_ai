# from sentence_transformers import SentenceTransformer
# from db import get_connection

# model = SentenceTransformer("all-mpnet-base-v2")

# conn = get_connection()
# cur = conn.cursor()

# print("Database Connected")
# # print("Embedding Model Loaded")
import json
from sentence_transformers import SentenceTransformer
from pgvector.psycopg2 import register_vector

from db import get_connection


print("Loading embedding model...")
model = SentenceTransformer("all-mpnet-base-v2")
print("✅ Embedding model loaded")

# Database connection
conn = get_connection()
register_vector(conn)

cur = conn.cursor()


def get_students():
    """
    Fetch student details with latest result.
    """

    query = """
    SELECT
        s.student_id,
        s.name,
        s.batch,
        s.attendance,
        r.physics,
        r.chemistry,
        r.maths,
        r.total,
        r.rank
    FROM students s
    LEFT JOIN results r
    ON s.student_id = r.student_id;
    """

    cur.execute(query)

    return cur.fetchall()


def build_text(student):
    """
    Convert database row into meaningful text.
    """

    return f"""
Student ID: {student[0]}
Name: {student[1]}
Batch: {student[2]}
Attendance: {student[3]}

Physics Marks: {student[4]}
Chemistry Marks: {student[5]}
Maths Marks: {student[6]}

Total Marks: {student[7]}
Rank: {student[8]}
"""


def embedding_exists(student_id):

    cur.execute(
        """
        SELECT id
        FROM embeddings
        WHERE source_id=%s
        """,
        (student_id,)
    )

    return cur.fetchone() is not None


def save_embedding(student_id, text, embedding):

    metadata = {
        "student_id": student_id
    }

    cur.execute(
        """
        INSERT INTO embeddings
        (
            source_type,
            source_id,
            chunk_text,
            embedding,
            metadata
        )

        VALUES (%s,%s,%s,%s,%s)
        """,

        (
            "student",
            student_id,
            text,
            embedding,
            json.dumps(metadata)
        )
    )


def main():

    students = get_students()

    print(f"\nFound {len(students)} students\n")

    inserted = 0
    skipped = 0

    for student in students:

        student_id = student[0]

        if embedding_exists(student_id):
            skipped += 1
            continue

        text = build_text(student)

        embedding = model.encode(text).tolist()

        save_embedding(
            student_id,
            text,
            embedding
        )

        inserted += 1

        print(f"✅ Embedded {student_id}")

    conn.commit()

    print("\n-----------------------------")
    print(f"Inserted : {inserted}")
    print(f"Skipped  : {skipped}")
    print("-----------------------------")


if __name__ == "__main__":

    main()

    cur.close()
    conn.close()