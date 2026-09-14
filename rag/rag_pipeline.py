from rag.context import RAGContext
from rag.prompt import build_prompt
from rag.retriever import Retriever
from llm.ollama_client import generate_response


class RAGPipeline:
   
    def __init__(self):
        self.retriever = Retriever()

    def ask(self, question: str, subject: str | None = None) -> str:
        retrieved = self.retriever.search(question, subject=subject)
        context = RAGContext(
            retrieved_materials=retrieved,
            sources=[row.get("source_id") for row in retrieved],
        )
        prompt = build_prompt(question, context)
        return generate_response(prompt)

    def answer(self, question: str, subject: str | None = None) -> str:
        return self.ask(question, subject)

    def build_context(self, question: str, subject: str | None = None) -> RAGContext:
        retrieved = self.retriever.search(question, subject=subject)
        return RAGContext(
            retrieved_materials=retrieved,
            sources=[row.get("source_id") for row in retrieved],
        )


def answer_question(question: str):
    pipeline = RAGPipeline()
    return pipeline.ask(question)
