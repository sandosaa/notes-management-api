from fastapi import FastAPI, Depends
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from contextlib import asynccontextmanager
from typing import Annotated

from manager import NoteManager
from model import create_all_eng, SessionDep
from schemas import NoteCreate, NoteUpdate, NoteResponse

# ---------------- Simple frontend ----------------
template = Jinja2Templates(directory="template")



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
@app.post("/notes/", response_model=NoteResponse,description="Add a new note here")
def create_note(note: NoteCreate, manager: ManagerDep):
    return manager.create(note)


# Read Notes (list)
@app.get("/notes/", response_model=list[NoteResponse],description="View NO. of notes")
def read_notes(manager: ManagerDep, offset: int = 0, limit: int = 10):
    return manager.get_all(offset, limit)


# Read Note (single)
@app.get("/notes/{note_id}", response_model=NoteResponse, description="View a single note by its ID")
def read_note(note_id: int, manager: ManagerDep):
    return manager.get_by_id(note_id)


# Update Note
@app.patch("/notes/{note_id}", response_model=NoteResponse,description="Update a previous note by its ID")
def update_note(note_id: int, note: NoteUpdate, manager: ManagerDep):
    return manager.update(note_id, note)


# Delete Note
@app.delete("/notes/{note_id}",description="Delete a note by its ID")
def delete_note(note_id: int, manager: ManagerDep):
    return manager.delete(note_id)


# Root
@app.get("/",include_in_schema=False) #we don't want to show it.
def read_root(request:Request):
    return template.TemplateResponse(request,"home.html")
    return {"message": "Welcome to the Notes API! Go to /docs to test it."}
