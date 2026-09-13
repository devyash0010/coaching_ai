from fastapi import APIRouter

from crud import *

from services import *

from schemas import *
from schemas import TeacherLogin, ChatRequest
from crud import (
    get_all_students,
    get_results,
    get_leaderboard,
    get_dashboard_summary,
    get_teacher_profile,
    authenticate_teacher
)

router = APIRouter()


@router.post("/teacher/login")
def teacher_login(login: TeacherLogin):

    success = authenticate_teacher(
        login.email,
        login.password
    )

    if success:
        return {
            "status": "success",
            "message": "Login Successful"
        }

    return {
        "status": "failed",
        "message": "Invalid Email or Password"
    }


@router.post("/teacher/logout")
def teacher_logout():

    return {
        "message": "Logged Out Successfully"
    }


@router.get("/teacher/profile")
def teacher_profile():

    return get_teacher_profile()


@router.get("/teacher/dashboard")
def dashboard():

    return get_dashboard_summary()


@router.get("/teacher/students")
def students():

    return get_all_students()


@router.get("/teacher/results")
def results():

    return get_results()


@router.get("/teacher/leaderboard")
def leaderboard():

    return get_leaderboard()


@router.get("/teacher/analytics")
def analytics():

    return {
        "message": "Analytics will be connected by Member 1"
    }


@router.post("/teacher/chat")
def teacher_chat(chat: ChatRequest):

    question = chat.question

    # Member 1 will connect the AI model here
    answer = "AI response will come from RAG + Ollama."

    return {
        "question": question,
        "answer": answer
    }