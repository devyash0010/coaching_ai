# Coaching AI

**An AI-powered coaching institute management platform** — manage students, tests, attendance and performance analytics, and ask questions in plain English to a **grounded RAG assistant** that answers from *your* actual student data.

Built with **FastAPI + PostgreSQL (pgvector) + Ollama (qwen2.5:3b)** on the backend and a **React + Vite** teacher workspace on the frontend.

---

## 📸 Demo

Real screenshots from a running instance (live data: 100 students, real RAG answer):

### Dashboard — cohort KPIs at a glance

![Dashboard](docs/screenshots/dashboard.png)

### Students — full student directory

![Students](docs/screenshots/students.png)

### AI Assistant — grounded RAG answer over student data

Ask _"Which students are weak in Physics?"_ and get an answer **retrieved from the database**, not hallucinated:

![AI Assistant](docs/screenshots/ai-assistant.png)

### Leaderboard — ranked by average score

![Leaderboard](docs/screenshots/leaderboard.png)

### Performance — subject-level trends

![Performance](docs/screenshots/performance.png)

### Analytics — attendance, scores & AI signals

![Analytics](docs/screenshots/analytics.png)

---

## ✨ Features

| Area | What you get |
|---|---|
| **Dashboard** | Total students, average score, attendance, top performer, academic trend chart, subject averages, weak-area priorities, top students |
| **Student Management** | Directory of all students, individual profiles with test history |
| **Tests** | Test list, per-test detail with subject-wise breakdown |
| **Leaderboard** | Cohort ranking by average score |
| **Performance & Analytics** | Mark trends, subject comparison, attendance vs. scores, insight signals |
| **Study Material** | Batch/class study resources |
| **AI Assistant (RAG)** | Natural-language questions answered from live student data with pgvector retrieval + local LLM |
| **Auth-ready backend** | Teacher login/logout/profile endpoints (JWT) alongside analytics routes |

## 🧠 How the RAG assistant works

```
  Teacher question
        │
        ▼
┌───────────────────┐   embed with sentence-transformers
│  FastAPI /teacher │──────────────────────────────────┐
│     /chat         │                                  │
└───────────────────┘                                  ▼
                                          ┌────────────────────────┐
                                          │  PostgreSQL + pgvector │
                                          │  cosine similarity     │
                                          │  top-k retrieval       │
                                          └───────────┬────────────┘
                                                      │ retrieved student
                                                      │ records (context)
                                                      ▼
                                          ┌────────────────────────┐
                                          │  Ollama · qwen2.5:3b   │
                                          │  grounded generation   │
                                          └───────────┬────────────┘
                                                      │
                                                      ▼
                                             cited, data-grounded
                                                    answer
```

1. The question is embedded with `all-mpnet-base-v2` (`sentence-transformers`).
2. The embedding is matched against student/test rows in **pgvector** via cosine similarity.
3. The top matching records become the **context** of a strict grounding prompt (`rag/prompt.py`).
4. **Ollama (`qwen2.5:3b`)** — running locally — answers *only* from that context; if the data doesn't contain the answer, it says so.

## 🏗️ Architecture

```
┌──────────────────────┐        ┌───────────────────────────────┐
│  React + Vite (3000) │───────▶│  FastAPI backend (8000)       │
│  Teacher Workspace   │  REST  │  backend/routes.py            │
│  frontend/src/pages  │        │  backend/services.py  (JWT)   │
└──────────────────────┘        └───────┬───────────────┬───────┘
                                        │               │
                        ┌───────────────▼───┐   ┌───────▼────────────┐
                        │ PostgreSQL 17     │   │ Ollama             │
                        │ + pgvector (5433) │   │ qwen2.5:3b         │
                        │ students, results,│   │ localhost:11434    │
                        │ tests, embeddings │   └────────────────────┘
                        └───────────────────┘
```

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | React 19, Vite, react-router-dom, Recharts, lucide-react, date-fns |
| Backend | FastAPI, Uvicorn, Pydantic, python-jose (JWT), passlib (bcrypt) |
| Database | PostgreSQL 17 + **pgvector** (Docker), psycopg2, SQLAlchemy |
| AI / RAG | Ollama (`qwen2.5:3b`), sentence-transformers (`all-mpnet-base-v2`), pgvector cosine search |
| Tooling | concurrently (one-command dev), verification tests |

## 📂 Project Structure

```
Coaching_ai/
├── backend/            # FastAPI app, routes, services, auth, config
│   ├── main.py         # app entry + CORS + health
│   ├── routes.py       # /teacher/* endpoints
│   ├── services.py     # analytics & chat business logic
│   └── auth.py         # JWT
├── rag/                # RAG pipeline: retriever, prompt, context, pipeline
├── llm/                # Ollama client
├── database/           # schema.sql, db.py, embedding.py, CSV importer
│   └── schema.sql      # tables + pgvector extension
├── data/               # seed CSVs (students, results, tests, ...)
├── frontend/           # React + Vite teacher workspace
│   └── src/pages/      # Dashboard, Students, AI Assistant, ...
├── docs/               # API.md + screenshots/
├── scripts/            # demo screenshot capture
├── tests/              # backend verification tests
└── .env                # your local configuration (not committed)
```

## 🚀 Quick Start

### Prerequisites

- **Docker** (for the PostgreSQL + pgvector container)
- **Python 3.10+**
- **Node.js 18+**
- **Ollama** installed and running — <https://ollama.com>

### 1. Start the vector database (existing container)

If the container already exists (this project uses one named `coaching-vector-db`):

```bash
docker start coaching-vector-db
```

Or create a fresh one:

```bash
docker run -d --name coaching-vector-db \
  -e POSTGRES_PASSWORD=yourpassword \
  -e POSTGRES_DB=coaching_ai \
  -p 5433:5432 \
  pgvector/pgvector:pg17
```

Then apply the schema and (optionally) load the sample dataset:

```bash
# create tables + pgvector extension
psql "postgresql://postgres:yourpassword@localhost:5433/coaching_ai" -f database/schema.sql

# import the 100-student sample dataset from data/*.csv
python -m database.import_all
```

### 2. Configure the environment

Create `.env` in the project root (full contract in [docs/API.md](docs/API.md)):

```env
DATABASE_URL=postgresql://postgres:yourpassword@localhost:5433/coaching_ai
POSTGRES_HOST=localhost
POSTGRES_PORT=5433
POSTGRES_DB=coaching_ai
POSTGRES_USER=postgres
POSTGRES_PASSWORD=yourpassword

OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL=qwen2.5:3b
EMBEDDING_MODEL=all-mpnet-base-v2

BACKEND_URL=http://localhost:8000
FRONTEND_URL=http://localhost:3000
CORS_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
SECRET_KEY=change-me
ALGORITHM=HS256
```

> `.env` is gitignored — never commit real credentials.

### 3. Pull the LLM model

```bash
ollama pull qwen2.5:3b
```

### 4. Install dependencies

```bash
# Python backend
python -m venv .venv
.venv\Scripts\activate          # Windows — use: source .venv/bin/activate on macOS/Linux
pip install -r requirements.txt

# JavaScript (root runner + frontend)
npm install
npm --prefix frontend install
```

### 5. Run everything

**One command** (backend on **:8000** + frontend on **:3000**):

```bash
npm run dev
```

Or manually in two terminals:

```bash
# Terminal 1 — backend
python -m uvicorn backend.main:app --host 0.0.0.0 --port 8000

# Terminal 2 — frontend (point it at the backend)
# frontend/vite.config.js reads VITE_API_BASE_URL
set VITE_API_BASE_URL=http://localhost:8000      # cmd — or $env:... on PowerShell
npm --prefix frontend run dev
```

Open **<http://localhost:3000>** — interactive API docs are at **<http://localhost:8000/docs>**.

> **Port tips:** if port 8000/3000 is taken by another app, run uvicorn on any free port (e.g. `--port 8010`) and set `VITE_API_BASE_URL=http://localhost:8010` to match. If the DB port differs, update `POSTGRES_PORT` / `DATABASE_URL` accordingly.

## 🔌 API

All backend routes live in `backend/routes.py` — full request/response contract in **[docs/API.md](docs/API.md)**.

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/health` | Service health |
| POST | `/teacher/login` · `/teacher/logout` | JWT auth |
| GET | `/teacher/profile` | Current teacher |
| GET | `/teacher/dashboard` | KPI summary (students, avg score, attendance) |
| GET | `/teacher/students` | Student directory |
| GET | `/teacher/results` | Test results |
| GET | `/teacher/leaderboard` | Ranked students |
| GET | `/teacher/analytics` | Performance analytics |
| POST | `/teacher/chat` | **RAG assistant** (question → grounded answer) |

## ✅ Tests

```bash
python -m pytest tests/
```

## 📸 Regenerating the demo screenshots

The screenshots in `docs/screenshots/` were captured from a live instance:

```bash
# static pages (headless Chrome)
chrome --headless=new --screenshot=docs/screenshots/dashboard.png http://localhost:3000/

# AI assistant with a real RAG answer (requires backend + Ollama running)
python scripts/capture_ai_demo.py
```

---

<p align="center">Made for coaching institutes that want <b>data + AI</b> in one workspace.</p>

