from dataclasses import dataclass, field
from typing import Any


@dataclass
class RAGContext:
    student: dict[str, Any] | None = None
    analytics: dict[str, Any] | None = None
    retrieved_materials: list[dict[str, Any]] = field(default_factory=list)
    sources: list[str] = field(default_factory=list)
