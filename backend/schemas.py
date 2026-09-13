from pydantic import BaseModel


class LoginRequest(BaseModel):

    email: str

    password: str



from pydantic import BaseModel

class TeacherLogin(BaseModel):
    email: str
    password: str


class ChatRequest(BaseModel):
    question: str



class ChatRequest(BaseModel):

    question:str