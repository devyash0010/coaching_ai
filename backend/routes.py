from fastapi import APIRouter

from backend.auth import authenticate_teacher
from backend.schemas import ChatRequest, TeacherLogin
from backend.services import (
    get_all_students,
    get_dashboard_summary,
    get_leaderboard,
    get_results,
    get_teacher_profile,
)
from rag.rag_pipeline import RAGPipeline

router = APIRouter()


@router.post("/teacher/login")
def teacher_login(login: TeacherLogin):
    success = authenticate_teacher(login.email, login.password)
    if success:
        return {"status": "success", "message": "Login Successful"}
    return {"status": "failed", "message": "Invalid Email or Password"}


@router.post("/teacher/logout")
def teacher_logout():
    return {"message": "Logged Out Successfully"}


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
    return {"message": "Analytics will be connected by the consolidated backend service layer."}


@router.post("/teacher/chat")
def teacher_chat(chat: ChatRequest):
    question = chat.question
    pipeline = RAGPipeline()
    answer = pipeline.ask(question)
    return {"question": question, "answer": answer}


@router.get("/health")
def health_check():
    return {"status": "ok"}
