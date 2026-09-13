'''  Student Analytics Engine  '''


from analytics.attendance import analyze_attendance
from analytics.performance import analyze_performance
from analytics.recommendation import generate_recommendation
from analytics.leaderboard import get_top_students
from analytics.leaderboard import get_student_rank

def analyze_student(student_id):
    attendance = analyze_attendance(student_id)
    performance = analyze_performance(student_id)
    recommendation = generate_recommendation(student_id)
    rank = get_student_rank(student_id)
    if "error" in attendance:
        return attendance

    if "error" in performance:
        return performance
    
    if "error" in recommendation:
        return recommendation
    return {

    "student":{

        "student_id":attendance["student_id"],

        "name":attendance["name"],

        "rank":rank

    },

    "attendance":attendance,

    "performance":performance,

    "recommendation":recommendation["recommendations"]

}