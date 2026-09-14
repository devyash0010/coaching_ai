from dataclasses import dataclass, field
from typing import Any


@dataclass
class OllamaChatRequest:
    prompt: str
    model: str = "qwen2.5:3b"


@dataclass
class OllamaChatResponse:
    answer: str
    model: str = "qwen2.5:3b"
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class RAGQueryContext:
    student: dict[str, Any] | None = None
    analytics: dict[str, Any] | None = None
    retrieved_materials: list[dict[str, Any]] = field(default_factory=list)
    sources: list[str] = field(default_factory=list)


@dataclass
class Student:
    student_id: str
    name: str
    batch: str
    attendance: int | None = None
    physics: int | None = None
    chemistry: int | None = None
    maths: int | None = None
    total: int | None = None
    rank: int | None = None
