# syntax=docker/dockerfile:1

# ---- Backend image: FastAPI + RAG (sentence-transformers) ----
FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    HF_HOME=/root/.cache/huggingface \
    SENTENCE_TRANSFORMERS_HOME=/root/.cache/huggingface

WORKDIR /app

# Install CPU-only torch first (far smaller than the default CUDA build);
# sentence-transformers will reuse it instead of pulling a large CUDA wheel.
RUN pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu

# Full backend dependency set lives in the root requirements.txt.
COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# NOTE: the sentence-transformers model (all-mpnet-base-v2) is NOT downloaded
# here — doing so stalls on HF rate limits. Instead the host's existing
# HuggingFace cache is bind-mounted at runtime (see docker-compose.yml), so the
# model loads instantly with no internet. If the mount is ever absent, the app
# downloads the model lazily on first use as a fallback.

# Entrypoint resolves the embedding model to a local snapshot in the mounted
# HuggingFace cache before starting the app.
COPY backend/docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

# Application source (backend, database, rag, llm packages are imported
# from the project root, so copy the whole context minus ignored paths).
COPY . .

EXPOSE 8000

ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
