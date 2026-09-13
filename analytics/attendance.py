'''  Attendance Analysis Module:

This module contains all functions related to student attendance analysis.

'''

from database.db import get_connection
from analytics.utils import calculate_percentage


# function used for attendence status :
def attendance_status(attendance_percentage):
    
    if attendance_percentage >= 90:
        return "Excellent"

    elif attendance_percentage >= 75:
        return "Good"

    elif attendance_percentage >= 60:
        return "Average"

    else:
        return "Poor"
    

# now creating a function to analyse attendence risk :
def attendance_risk(attendance_percentage):
    
    if attendance_percentage >= 75:
        return "Low"

    elif attendance_percentage >= 60:
        return "Medium"

    else:
        return "High"
    

#  function to get attendence from database
def get_student_attendance(student_id):

    conn = get_connection()

    cursor = conn.cursor() #like a database keyboard

    query = """ SELECT student_id, name, attendance FROM students WHERE student_id = %s """

    cursor.execute(query, (student_id,))

    student = cursor.fetchone() # it gives id,name,marks of student

    cursor.close()
    conn.close()

    return student

# analysis of attendence
def analyze_attendance(student_id):

    student = get_student_attendance(student_id)

    if student is None:
        return {
            "error": "Student not found in database"
        }

    student_id, name, attendance = student

    status = attendance_status(attendance)

    risk = attendance_risk(attendance)


    return {
        "student_id": student_id,
        "name": name,
        "attendance": attendance,
        "status": status,
        "risk": risk
    }