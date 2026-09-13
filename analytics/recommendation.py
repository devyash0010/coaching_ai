''' it is recommendation engine '''

from analytics.attendance import analyze_attendance
from analytics.performance import analyze_performance


def attendance_recommendation(status):
    if status == "Excellent":
        return "Maintain your excellent attendance."

    elif status == "Good":
        return "Try to reach above 90% attendance."

    elif status == "Average":
        return "Attend more classes regularly."

    else:
        return "Attendance is very low. improvement is required."
    

def subject_recommendation(subject):

    recommendations = {
        "Physics":
        "Practice numerical problems and revise formulas.",

        "Chemistry":
        "Focus on NCERT and chemical reactions.",

        "Maths":
        "Solve algebra and calculus problems daily."
    }

    return recommendations.get(subject,"Continue practicing.")

def grade_recommendation(grade):
    if grade == "A+":
        return "Excellent work."

    elif grade == "A":
        return "Very good performance."

    elif grade == "B":
        return "Good, but can improve."

    elif grade == "C":
        return "Need more revision and practice."

    elif grade == "D":
        return "Serious preparation and revision is required."

    else:
        return "do not lose your hope. need to work harder."
    
def performance_recommendation(level):

    if level == "Outstanding":
        return "Prepare for advanced competitive exams."

    elif level == "Excellent":
        return "Keep practicing mock tests."

    elif level == "Good":
        return "Increase daily study hours."

    elif level == "Needs Improvement":
        return "Focus on weak topics."

    return "Meet your faculty mentor immediately."


def generate_recommendation(student_id):

    attendance = analyze_attendance(student_id)

    performance = analyze_performance(student_id)

    if "error" in attendance:
        return attendance

    if "error" in performance:
        return performance

    recommendations = [
        attendance_recommendation(
            attendance["status"]
        ),

        subject_recommendation(
            performance["weak_subject"]
        ),

        grade_recommendation(
            performance["grade"]
        ),

        performance_recommendation(
            performance["performance"]
        )
    ]

    return {
        "student_id": student_id,
        "recommendations": recommendations
    }