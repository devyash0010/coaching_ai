import psycopg2


def get_connection():
    return psycopg2.connect(
        host="localhost",
        port="5433",
        database="coaching_ai",
        user="postgres",
        password="Daksh@0310"
    )


if __name__ == "__main__":
    try:
        conn = get_connection()
        print("✅ Database Connected Successfully")
        conn.close()
    except Exception as e:
        print("❌ Database Connection Failed")
        print(e)