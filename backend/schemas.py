from pydantic import BaseModel


class LoginRequest(BaseModel):
    email: str
    password: str


class TeacherLogin(BaseModel):
    email: str
    password: str


class ChatRequest(BaseModel):
    question: str
