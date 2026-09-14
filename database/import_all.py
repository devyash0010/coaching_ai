from pathlib import Path
import pandas as pd

from database.db import get_connection


# ==========================================================
# PROJECT PATH
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent.parent
CSV_FOLDER = BASE_DIR / "data"

# ==========================================================
# DATABASE
# ==========================================================

conn = get_connection()
cur = conn.cursor()


# ==========================================================
# Generic CSV Import Function
# ==========================================================

def import_csv(file_name, query, columns, table_name):

    try:

        file_path = CSV_FOLDER / file_name

        df = pd.read_csv(file_path)

        for _, row in df.iterrows():

            values = tuple(row[col] for col in columns)

            cur.execute(query, values)

        conn.commit()

        print(f"✅ {table_name} Imported ({len(df)} Records)")

    except Exception as e:

        conn.rollback()

        print(f"❌ {table_name}: {e}")


# ==========================================================
# STUDENTS
# ==========================================================

import_csv(

    "Students.csv",

    """
    INSERT INTO students
    (
        student_id,
        name,
        phone,
        email,
        batch,
        joining_date,
        fees,
        paid,
        remaining,
        attendance
    )

    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)

    ON CONFLICT (student_id) DO NOTHING;
    """,

    [
        "StudentID",
        "Name",
        "Phone",
        "Email",
        "Batch",
        "JoiningDate",
        "Fees",
        "Paid",
        "Remaining",
        "Attendance"
    ],

    "Students"
)

# ==========================================================
# FACULTY
# ==========================================================

import_csv(

    "Faculty.csv",

    """
    INSERT INTO faculty
    (
        faculty_id,
        name,
        subject,
        experience_years
    )

    VALUES (%s,%s,%s,%s)

    ON CONFLICT (faculty_id) DO NOTHING;
    """,

    [
        "FacultyID",
        "Name",
        "Subject",
        "ExperienceYears"
    ],

    "Faculty"
)

# ==========================================================
# TESTS
# ==========================================================

import_csv(

    "tests.csv",

    """
    INSERT INTO tests
    (
        test_id,
        test_name,
        subject,
        max_marks,
        test_date
    )

    VALUES (%s,%s,%s,%s,%s)

    ON CONFLICT (test_id) DO NOTHING;
    """,

    [
        "TestID",
        "TestName",
        "Subject",
        "MaxMarks",
        "TestDate"
    ],

    "Tests"
)

# ==========================================================
# RESULTS
# ==========================================================

import_csv(

    "results.csv",

    """
    INSERT INTO results
    (
        student_id,
        test_id,
        physics,
        chemistry,
        maths,
        total,
        rank
    )

    VALUES (%s,%s,%s,%s,%s,%s,%s);
    """,

    [
        "StudentID",
        "TestID",
        "Physics",
        "Chemistry",
        "Maths",
        "Total",
        "Rank"
    ],

    "Results"
)

# ==========================================================
# STUDY MATERIAL
# ==========================================================

import_csv(

    "study_material.csv",

    """
    INSERT INTO study_material
    (
        material_id,
        subject,
        chapter,
        pdf_name
    )

    VALUES (%s,%s,%s,%s)

    ON CONFLICT (material_id) DO NOTHING;
    """,

    [
        "MaterialID",
        "Subject",
        "Chapter",
        "PDFName"
    ],

    "Study Material"
)

# ==========================================================
# LEADERBOARD
# ==========================================================

import_csv(

    "leaderboard.csv",

    """
    INSERT INTO leaderboard
    (
        rank,
        student_id,
        name,
        batch,
        average_score
    )

    VALUES (%s,%s,%s,%s,%s);
    """,

    [
        "Rank",
        "StudentID",
        "Name",
        "Batch",
        "AverageScore"
    ],

    "Leaderboard"
)

# ==========================================================
# CLOSE CONNECTION
# ==========================================================

cur.close()
conn.close()

print("\n🎉 ALL IMPORTS COMPLETED SUCCESSFULLY")