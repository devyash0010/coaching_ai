

from database.db import get_connection

def get_top_students(limit=10):

    conn = get_connection()

    cursor = conn.cursor()

    query = """
    SELECT
        student_id,
        name,
        batch,
        average_score
    FROM leaderboard
    ORDER BY average_score DESC
    LIMIT %s
    # """

    cursor.execute(query, (limit,))

    students = cursor.fetchall()

    cursor.close()
    conn.close()

    return students


def get_batch_topper(batch_name):

    conn = get_connection()

    cursor = conn.cursor()

    query = """
    SELECT
        student_id,
        name,
        average_score
    FROM leaderboard
    WHERE batch=%s
    ORDER BY average_score DESC
    LIMIT 1
    """

    cursor.execute(query, (batch_name,))

    topper = cursor.fetchone()

    cursor.close()
    conn.close()

    return topper



def class_average():

    conn = get_connection()

    cursor = conn.cursor()

    query = """
    SELECT
        ROUND(AVG(average_score),2)
    FROM leaderboard
    """

    cursor.execute(query)

    average = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return average


def excellent_students():

    conn = get_connection()

    cursor = conn.cursor()

    query = """
    SELECT
        student_id,
        name,
        average_score
    FROM leaderboard
    WHERE average_score>=90
    """

    cursor.execute(query)

    students = cursor.fetchall()

    cursor.close()
    conn.close()

    return students

def weak_students():

    conn = get_connection()

    cursor = conn.cursor()

    query = """
    SELECT
        student_id,
        name,
        average_score
    FROM leaderboard
    WHERE average_score<50
    """

    cursor.execute(query)

    students = cursor.fetchall()

    cursor.close()
    conn.close()

    return students


def batch_statistics(batch_name):

    conn = get_connection()

    cursor = conn.cursor()

    query = """
    SELECT

        COUNT(*),
        ROUND(AVG(average_score),2),
        MAX(average_score),
        MIN(average_score)

    FROM leaderboard

    WHERE batch=%s
    """

    cursor.execute(query,(batch_name,))
    stats = cursor.fetchone()
    cursor.close()
    conn.close()

    return {

        "total_students":stats[0],
        "average_score":stats[1],
        "highest_score":stats[2],
        "lowest_score":stats[3]

    }


def get_student_rank(student_id):

    conn = get_connection()

    cursor = conn.cursor()

    query = """
    SELECT rank
    FROM leaderboard
    WHERE student_id=%s
    """

    cursor.execute(query,(student_id,))

    result = cursor.fetchone()

    cursor.close()

    conn.close()

    if result:
        return result[0]

    return None