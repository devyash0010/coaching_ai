import logging

import ollama

from backend.config import settings

logger = logging.getLogger(__name__)


class OllamaClient:
    def __init__(self, host: str | None = None, model: str | None = None):
        self.host = host or settings.OLLAMA_HOST
        self.model = model or settings.OLLAMA_MODEL

    def generate_response(self, prompt: str) -> str:
        try:
            if not prompt or not prompt.strip():
                return ""

            client = ollama.Client(host=self.host)
            response = client.chat(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
            )

            if hasattr(response, "message") and response.message:
                return str(response.message.content).strip()
            if hasattr(response, "content"):
                return str(response.content).strip()
            if isinstance(response, dict):
                if "message" in response:
                    return str(response["message"]["content"]).strip()
                if "content" in response:
                    return str(response["content"]).strip()
            return ""
        except Exception as exc:
            logger.warning("Ollama generation failed: %s", exc)
            return "Ollama response generation failed. Please verify Ollama is running and the configured model is available."


client = OllamaClient()


def generate_response(prompt: str) -> str:
    return client.generate_response(prompt)
