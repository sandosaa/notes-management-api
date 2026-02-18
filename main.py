from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

from src.api.v1.router import api_router
from src.core.database import init_db


# --- TEACHING: THE LIFESPAN EVENT HANDLER ---
# In modern FastAPI, we use a 'lifespan' context manager to handle logic that
# should run when the application starts up and shuts down.
# This is where we perform expensive operations like connecting to a database
# or loading machine learning models.
@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """
    Handles application startup and shutdown events.
    """
    # --- TIP: DATABASE REGISTRATION ---
    # SQLModel requires models to be imported before calling 'create_all'.
    # We import the Note model here to ensure it is registered with the
    # SQLModel metadata, allowing 'init_db' to create the table.
    from src.models.note import Note  # noqa: F401

    # Initialize database tables
    init_db()

    # The 'yield' statement separates startup logic from shutdown logic.
    # Everything before 'yield' runs on STARTUP.
    # Everything after 'yield' runs on SHUTDOWN.
    yield


# --- ZATUNA: THE FASTAPI INSTANCE ---
# This is the heart of your application.
# We provide a title and description which will automatically appear in
# our interactive Swagger/OpenAPI documentation.
app = FastAPI(
    title="Notes Management API",
    description=("A professionally KAFRAWI Notes API."),
    version="0.0.1",
    lifespan=lifespan,
)

# --- TEACHING: STATIC FILES ---
# Mounting a directory allows us to serve non-Python files like CSS or images.
# Files inside 'frontend/static' can now be accessed via '/static/filename'.
# This is useful when you want to bundle a simple UI with your API like the one eman working on.
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")

# --- TEACHING: VERSIONED ROUTING ---
# We include our v1 router under the '/api/v1' prefix.
# API versioning is a "Best Practice" because it allows you to update your
# API in the future (creating v2) without breaking older clients.
app.include_router(api_router, prefix="/api/v1")


# --- TEACHING: ROOT REDIRECT ---
# Instead of showing a "blank page" at '/', we redirect users to '/docs'.
# This improves the "Developer Experience" (DX) by immediately showing
# the interactive documentation when they open the server URL.
@app.get("/", include_in_schema=False)
async def root() -> RedirectResponse:
    """
    Redirects the root URL to the interactive API documentation.
    """
    return RedirectResponse(url="/docs")


# --- TEACHING: LOCAL DEVELOPMENT ---
# This block allows you to run the file directly using 'python main.py'.
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
# but what it takes to build a protected dashboard with analytics and management tools "RESEARCH"
