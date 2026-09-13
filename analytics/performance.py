'''  This  is performance analysis file'''

from database.db import get_connection

# this takes student marks from database
def get_student_marks(student_id):

    conn = get_connection()

    cursor = conn.cursor()

    query = """
    SELECT
        s.student_id,
        s.name,
        r.physics,
        r.chemistry,
        r.maths
    FROM students s
    JOIN results r
    ON s.student_id = r.student_id
    WHERE s.student_id = %s
    """

    cursor.execute(query, (student_id,))

    student = cursor.fetchone()

    cursor.close()
    conn.close()

    return student

def calculate_average(physics, chemistry, maths):
    total = physics + chemistry + maths

    average = total / 3

    return round(average,2)


def best_subject(physics, chemistry, maths):

    subjects = {
        "Physics": physics,
        "Chemistry": chemistry,
        "Maths": maths
    }

    return max(subjects, key=subjects.get)

def weak_subject(physics, chemistry, maths):

    subjects = {
        "Physics": physics,
        "Chemistry": chemistry,
        "Maths": maths
    }

    return min(subjects, key=subjects.get)

def calculate_grade(average):

    if average >= 90:
        return "A+"

    elif average >= 80:
        return "A"

    elif average >= 70:
        return "B"

    elif average >= 60:
        return "C"

    elif average >= 50:
        return "D"

    return "F"

def performance_level(average):

    if average >= 90:
        return "Outstanding"

    elif average >= 75:
        return "Excellent"

    elif average >= 60:
        return "Good"

    elif average >= 40:
        return "Needs Improvement"

    return "Poor"


def analyze_performance(student_id):

    student = get_student_marks(student_id)

    if student is None:

        return {
            "error":"Student Not Found"
        }

    student_id, name, physics, chemistry, maths = student

    average = calculate_average(
        physics,
        chemistry,
        maths
    )

    return {

        "student_id":student_id,
        "name":name,
        "physics":physics,
        "chemistry":chemistry,
        "maths":maths,
        "average":average,
        "grade":calculate_grade(average),
        "performance":performance_level(average),
        "best_subject":best_subject(
            physics,
            chemistry,
            maths
        ),

        "weak_subject":weak_subject(
            physics,
            chemistry,
            maths
        )
    }