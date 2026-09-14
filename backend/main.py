from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.config import settings
from backend.routes import router

app = FastAPI(
    title="Coaching AI Backend",
    version="1.0",
    docs_url="/docs",
    openapi_url="/openapi.json",
)

origins = [origin.strip()
           for origin in settings.CORS_ORIGINS.split(",") if origin.strip()]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.get("/")
def home():
    return {"message": "Coaching AI Backend Running"}


@app.get("/health")
def health():
    return {"status": "ok", "service": "coaching-ai-backend"}
