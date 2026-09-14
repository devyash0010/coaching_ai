from __future__ import annotations

from rag.context import RAGContext


SYSTEM_PROMPT = """
You answer only from the supplied context.
Never invent student data, marks, attendance, study material, or topics.
Distinguish facts from recommendations.
Be concise, grounded, actionable, and mention the relevant student or topic clearly.
"""


def build_prompt(question: str, context: RAGContext) -> str:
    """Create a simple prompt from the RAG context contract.

    The prompt builder is intentionally lightweight here and should be
    expanded later in Phase 7 to support routing and source attribution.
    """
    facts = []
    if context.student:
        facts.append("Student context: " + str(context.student))
    if context.analytics:
        facts.append("Analytics context: " + str(context.analytics))
    if context.retrieved_materials:
        facts.append("Retrieved materials: " +
                     str(context.retrieved_materials))
    if context.sources:
        facts.append("Sources: " + ", ".join(context.sources))

    return SYSTEM_PROMPT + "\n\nQuestion: " + question + "\n\nContext:\n" + "\n".join(facts)
