from database.db import get_connection


def format_students(data):
    students = []
    for row in data:
        students.append({"data": row})
    return students


def calculate_average(marks):
    return sum(marks) / len(marks) if marks else 0


def dashboard_summary():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM students")
    student_count = cur.fetchone()[0]
    cur.execute("SELECT ROUND(AVG(average_score), 2) FROM leaderboard")
    avg_score = cur.fetchone()[0]
    cur.execute("SELECT ROUND(AVG(attendance), 2) FROM students")
    avg_attendance = cur.fetchone()[0]
    cur.close()
    conn.close()
    return {
        "total_students": student_count,
        "average_score": avg_score,
        "average_attendance": avg_attendance,
    }


def analytics():
    return dashboard_summary()


def get_dashboard_summary():
    return dashboard_summary()


def get_teacher_profile():
    return {"name": "Teacher", "role": "admin"}


def get_all_students():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT student_id, name, batch, attendance FROM students ORDER BY student_id")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [
        {"student_id": row[0], "name": row[1],
            "batch": row[2], "attendance": row[3]}
        for row in rows
    ]


def get_results():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT student_id, test_id, physics, chemistry, maths, total, rank FROM results ORDER BY student_id")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [
        {
            "student_id": row[0],
            "test_id": row[1],
            "physics": row[2],
            "chemistry": row[3],
            "maths": row[4],
            "total": row[5],
            "rank": row[6],
        }
        for row in rows
    ]


def get_leaderboard():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT rank, student_id, name, batch, average_score FROM leaderboard ORDER BY rank")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [
        {"rank": row[0], "student_id": row[1], "name": row[2],
            "batch": row[3], "average_score": row[4]}
        for row in rows
    ]


def get_teacher_by_email(email: str):
    return None


# Keep authentication in auth.py as requested; service layer wires it.
def authenticate_teacher(email: str, password: str):
    from backend.auth import authenticate_teacher as auth_authenticate_teacher
    return auth_authenticate_teacher(email, password)
