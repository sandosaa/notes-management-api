from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager
from typing import Annotated

from manager import NoteManager
from model import create_all_eng, SessionDep
from schemas import NoteCreate, NoteUpdate, NoteResponse


# ---------------- Dependencies ----------------
def get_note_manager(session: SessionDep):
    return NoteManager(session)

ManagerDep = Annotated[NoteManager, Depends(get_note_manager)]


# ---------------- Lifespan ----------------
@asynccontextmanager
async def lifespan(app: FastAPI):
    create_all_eng()  # create tables if not exist
    yield


app = FastAPI(lifespan=lifespan)


# ---------------- Endpoints ----------------

# Create Note
@app.post("/notes/", response_model=NoteResponse)
def create_note(note: NoteCreate, manager: ManagerDep):
    return manager.create(note)


# Read Notes (list)
@app.get("/notes/", response_model=list[NoteResponse])
def read_notes(manager: ManagerDep, offset: int = 0, limit: int = 10):
    return manager.get_all(offset, limit)


# Read Note (single)
@app.get("/notes/{note_id}", response_model=NoteResponse)
def read_note(note_id: int, manager: ManagerDep):
    return manager.get_by_id(note_id)


# Update Note
@app.patch("/notes/{note_id}", response_model=NoteResponse)
def update_note(note_id: int, note: NoteUpdate, manager: ManagerDep):
    return manager.update(note_id, note)


# Delete Note
@app.delete("/notes/{note_id}")
def delete_note(note_id: int, manager: ManagerDep):
    return manager.delete(note_id)


# Root
@app.get("/")
def read_root():
    return {"message": "Welcome to the Notes API! Go to /docs to test it."}
