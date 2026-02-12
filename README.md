# Notes Management API

A lightweight and professional **Notes Management API** built with **FastAPI** and **SQLModel**.  
This project provides a clean and simple solution to manage notes with **CRUD functionality**, built-in **validation**, and automatic **timestamps** for tracking changes.

---

## 📝 Project Overview

This API allows users to **create, read, update, and delete notes** efficiently.  
Each note has:
- A **title** (required)
- An optional **description**
- A **timestamp** recording creation or last update

The API is built with **modern Python tools**, ensuring speed, reliability, and maintainability.

---

## ⚡ Features

- **Create Notes** – Add new notes with validation on title and description.
- **Read Notes** – Fetch all notes or a single note by ID.
- **Update Notes** – Update note title or description while tracking modification time.
- **Delete Notes** – Remove notes cleanly.
- **Validation** – Prevent empty titles and enforce max lengths.
- **FastAPI powered** – Provides automatic **interactive API docs** via Swagger UI.
- **Lightweight Database** – Uses SQLite for simplicity, no heavy setup required.

---

## 🛠 Technologies Used

- **Python 3.13+** – Modern, type-safe code
- **FastAPI** – Fast, asynchronous API framework
- **SQLModel** – Combines SQLAlchemy with Pydantic models
- **SQLite** – Simple, serverless database
- **Uvicorn** – ASGI server for running the app

---

## 🚀 How it Works

1. Users interact with endpoints via HTTP requests.
2. Input data is validated automatically against Pydantic schemas.
3. Notes are stored in SQLite using SQLModel models.
4. Responses are returned as JSON objects, fully compatible with frontend or other services.
5. Automatic error handling ensures a smooth user experience (e.g., 404 for missing notes, 422 for invalid input).

---

## 📂 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST   | `/notes/` | Create a new note |
| GET    | `/notes/` | List all notes (supports offset & limit) |
| GET    | `/notes/{note_id}` | Get a single note by ID |
| PATCH  | `/notes/{note_id}` | Update a note by ID |
| DELETE | `/notes/{note_id}` | Delete a note by ID |
| GET    | `/` | Root endpoint with welcome message |

---

## 💡 Example Usage

**Create a Note:**
```json
POST /notes/
{
  "title": "Project Meeting",
  "description": "Discuss milestones and deadlines"
}

Update a Note:

PATCH /notes/1
{
  "title": "Updated Project Meeting"
}


Get All Notes:

GET /notes/?offset=0&limit=10


Delete a Note:

DELETE /notes/1

🔗 Documentation

Interactive API docs are automatically available at:

Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc


📂 Installation & Setup (Optional)

For developers who want to run it locally:

git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
python -m venv .venv
source .venv/bin/activate  # Linux / MacOS
.venv\Scripts\activate     # Windows
pip install -r requirements.txt
uvicorn main:app --reload


Enjoy your Notes API 😍🎀