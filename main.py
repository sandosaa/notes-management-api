from manager import NoteManager
from model import Note, create_all_eng, SessionDep, Annotated
from fastapi import FastAPI,Depends 
from contextlib import asynccontextmanager


def get_note_manager(session: SessionDep):
    return NoteManager(session)

ManagerDep = Annotated[NoteManager, Depends(get_note_manager)]


@asynccontextmanager  #instead of on_event which makes the code run only one time
async def lifespan(app: FastAPI):
    create_all_eng()
    yield

app = FastAPI(lifespan=lifespan)

# --- Endpoints ---

@app.post("/notes/", response_model=Note)
def create_note(note: Note, manager: ManagerDep):
    return manager.create(note)

@app.get("/notes/", response_model=list[Note])
def read_notes(manager: ManagerDep, offset: int = 0, limit: int = 10):
    return manager.get_all(offset, limit)

@app.get("/notes/{note_id}", response_model=Note)
def read_note(note_id: int, manager: ManagerDep):
    return manager.get_by_id(note_id)

@app.patch("/notes/{note_id}", response_model=Note)
def update_note(note_id: int, note: Note, manager: ManagerDep):
    return manager.update(note_id, note)

@app.delete("/notes/{note_id}")
def delete_note(note_id: int, manager: ManagerDep):
    return manager.delete(note_id)

# to dont show error when we open the root link
@app.get("/")
def read_root():
    return {"message": "Welcome to the Notes API! Go to /docs to test it."}