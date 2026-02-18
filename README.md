# Notes Management API (MVC EDITION)

A modern, production-ready **Notes Management API** built with **FastAPI** and **SQLModel**, refactored into a clean **MVC (Model-View-Controller)** architecture with built-in readiness for **Semantic AI** integration.

---

## 🏗 Architecture & Design

This project follows a decoupled MVC pattern to ensure scalability and maintainability:

- **Models (`src/models/`)**: Defines the database schema using SQLModel.
- **Views/API (`src/api/`)**: Controllers that handle HTTP requests and routing.
- **Services (`src/services/`)**: Contains business logic, including a dedicated service for future **Semantic AI** features (embeddings, summarization).
- **Schemas (`src/schemas/`)**: Pydantic models for data validation and serialization.
- **Core (`src/core/`)**: Centralized configuration and database session management.
- **Frontend (`frontend/`)**: Dedicated space for static assets and templates "EMAN".

---

## ⚡ Features

- **MVC Structure** – Clean separation of concerns.
- **Semantic AI Ready** – Includes `AIService` placeholders for vector search and LLM integration.
- **Modern Tooling** – Powered by `uv` for blazing-fast dependency management.
- **Strict Type Safety** – Fully type-hinted and verified with `mypy --strict`.
- **Code Quality** – Linted and formatted using `Ruff` and `isort`.
- **Automated Checks** – Integrated `pre-commit` hooks for consistent code quality.
- **Interactive Docs** – Automatic Swagger/OpenAPI documentation at `/docs`.

---

## 🛠 Tech Stack

- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **Database/ORM**: [SQLModel](https://sqlmodel.tiangolo.com/) (SQLmodel + Pydantic)
- **Package Manager**: [uv](https://github.com/astral-sh/uv)
- **Linter/Formatter**: [Ruff](https://github.com/astral-sh/ruff)
- **Static Analysis**: [mypy](https://mypy-lang.org/)
- **Hooks**: [pre-commit](https://pre-commit.com/)
- **uv**:

---

## 📂 Project Structure

```text
notes-management-api/
├── frontend/               # Frontend assets (HTML, CSS, JS)
├── legacy/                 # Previous implementation files
├── src/
│   ├── api/                # API Controllers & Routers
│   │   └── v1/             # Versioned API endpoints
│   ├── core/               # Database & App configuration
│   ├── models/             # Database Models
│   ├── schemas/            # Request/Response Schemas
│   └── services/           # Business Logic (Note & AI Services)
├── main.py                 # Application entry point
├── pyproject.toml          # Tooling & Dependency config
└── README.md
```

---

## 🚀 Getting Started

### 1. Installation

Ensure you have `uv` installed. Then, sync the environment "curl -LsSf https://astral.sh/uv/install.sh | sh":

```bash
uv sync
```

### 2. Run the Application

Start the development server:

```bash
uv run uvicorn main:app --reload

```

or simply run `uv run fastapi run` for local development.

### 3. API Documentation

Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to explore the API. The root URL (`/`) automatically redirects here.

---

## 🤖 Semantic AI Roadmap

The `AIService` is prepared to integrate:

- **Vector Embeddings**: Store note content as vectors for similarity search.
- **Semantic Search**: Find notes based on meaning rather than just keywords.

---

## 🛡 Quality Control

Run all checks before committing or it won't even allow you to commit:

```bash
uv run pre-commit run --all-files
```

## Feature Suggestions for the Notes Management API

### 1. **User Authentication & Authorization**

- **Why:** Allow multiple users to have their own notes, and protect endpoints.
- **How:** Integrate simpleJWT with FastAPI’s security utilities. Add a `User` model and link notes to users.

### 2. **Full-Text Search**

- **Why:** Enable users to search notes by keywords or phrases.
- **How:** Use SQLite’s FTS5 extension or integrate with a search engine like Elasticsearch "discussed before".

#### 3. **Semantic Search (AI-powered)**

- **Why:** Let users find notes by meaning, not just keywords.
- **How:** Use the `AIService` placeholder to generate embeddings and perform vector similarity search after you implement categories.

#### 4. **Note Tagging & Categories**

- **Why:** Help users organize notes by tags or categories.
- **How:** Add a `tags` field (list of strings) to the Note model and support filtering by tag "DOING".

#### 5. **Rich Text & Attachments**

- **Why:** Allow users to format notes (bold, lists, links) and attach files/images.
- **How:** Store notes as Markdown or HTML, and add file upload endpoints with static file serving.

#### 6. **Note Sharing & Collaboration**

- **Why:** Enable users to share notes with others or collaborate in real-time.
- **How:** Add sharing permissions and possibly integrate WebSockets for live updates.

#### 7. **Note Version History**

- **Why:** Let users see and revert to previous versions of a note.
- **How:** Store note edits in a separate `NoteHistory` table with timestamps.

#### 8. **Reminders & Notifications**

- **Why:** Help users remember important notes or deadlines.
- **How:** Add a `reminder_time` field and integrate with an push notification service.

#### 9. **Trash/Recycle Bin**

- **Why:** Prevent accidental data loss by allowing users to restore deleted notes.
- **How:** Add a `deleted` boolean field and filter out trashed notes from normal queries "soft delete".

#### 10. **API Rate Limiting & Monitoring**

- **Why:** Protect the API from abuse and monitor usage.
- **How:** Integrate a rate-limiting middleware and logging/metrics (e.g., Prometheus "advanced").

#### 11. **Frontend Improvements**

- **Why:** Provide a user-friendly interface for managing notes.
- **How:** Build a SPA (Single Page Application) using Reactin the `frontend/` directory, consuming the API.

#### 12. **Export/Import Notes**

- **Why:** Allow users to back up or migrate their notes.
- **How:** Add endpoints to export notes as JSON, CSV, or Markdown, and import them back.

#### 13. **Dark Mode & Accessibility**

- **Why:** Improve usability for all users.
- **How:** Add CSS themes and ensure the frontend meets accessibility standards (WCAG).

#### 14. **Audit Logging**

- **Why:** Track who did what and when for security and debugging.
- **How:** Log all create/update/delete actions with user and timestamp.

#### 15. **Admin Dashboard**

- **Why:** Give admins insight into usage, errors, and user management.
- **How:** Build a protected dashboard with analytics and management tools "ai +backend".
