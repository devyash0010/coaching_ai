# API Contract

The frontend reads from the canonical backend routes in `backend/routes.py` and `backend/services.py`.

## Base URL

http://127.0.0.1:8000

## Endpoints

### GET /health
Returns service health.

Response:
```json
{"status": "ok"}
```

### GET /teacher/dashboard
Returns dashboard summary.

Response:
```json
{
  "total_students": 100,
  "average_score": 185.1,
  "average_attendance": 84.33
}
```

### GET /teacher/students
Returns an array of student summary rows.

Response:
```json
[
  {
    "student_id": "JEE001",
    "name": "Aarav Sharma",
    "batch": "JEE-2025-A",
    "attendance": 87,
    "performance": 178
  }
]
```

### GET /teacher/results
Returns assessment result rows.

Response:
```json
[
  {
    "student_id": "JEE001",
    "test_id": "T001",
    "physics": 72,
    "chemistry": 56,
    "maths": 88,
    "total": 216,
    "rank": 1
  }
]
```

### GET /teacher/leaderboard
Returns school leaderboard rows.

Response:
```json
[
  {
    "student_id": "JEE074",
    "name": "Advika Subramanian",
    "batch": "JEE-2025-A",
    "rank": 1,
    "average_score": 250
  }
]
```

### POST /teacher/chat
Accepts a question and returns an answer string from the RAG pipeline.

Request:
```json
{"question": "Which students are weak in Physics?"}
```

Response:
```json
{"answer": "..."}
```
