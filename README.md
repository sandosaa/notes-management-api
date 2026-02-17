# Notes Management API

A lightweight **Notes Management API** built with **FastAPI** and **SQLModel**.
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
- **Simple & Secure** – Built with security best practices in mind.
- **UV** – Modern fast project manager written in rust .

---

## 🛠 Technologies Used

- **Python 3.13+** – Modern, type-safe code
- **FastAPI** – Fast, asynchronous API framework
- **SQLModel** – Combines SQLAlchemy with Pydantic models
- **SQLite** – Simple, serverless database
- **uv** - Modern fast project manager written in rust .
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

| Method | Endpoint           | Description                              |
| ------ | ------------------ | ---------------------------------------- |
| POST   | `/notes/`          | Create a new note                        |
| GET    | `/notes/`          | List all notes (supports offset & limit) |
| GET    | `/notes/{note_id}` | Get a single note by ID                  |
| PATCH  | `/notes/{note_id}` | Update a note by ID                      |
| DELETE | `/notes/{note_id}` | Delete a note by ID                      |
| GET    | `/docs`            | Documentation for the API                |

---

## 🔗 Documentation

Interactive API docs are automatically available at:

Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc

---

## Expcetions for update & upgrade

- Add more layouts for the webpage
- Add tasks features
- Frontend features soon..
- Implement ML models

##### stay turnd on for more updates!

---

## Enjoy your Notes API
