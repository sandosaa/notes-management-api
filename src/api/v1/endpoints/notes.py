from collections.abc import Sequence
from typing import Annotated

from fastapi import APIRouter, Depends, Query
from sqlmodel import Session

from src.core.database import get_session
from src.models.note import Note
from src.schemas.note import NoteCreate, NoteResponse, NoteUpdate
from src.services.note_service import NoteService

# --- concept: THE API ROUTER ---
# An APIRouter allows uus to split our application into multiple files.
# Instead of putting 150 endpoints in main.py, we group related logic here
# (in this case, everything related to 'Notes').
router = APIRouter()


# --- Zatuna: DEPENDENCY PROVISION and please research too ---
# This function is a helper that FastAPI uses to provide an instance of
# our Service to the endpoints. By requiring 'get_session', we ensure that
# the Service always has a fresh database connection hmmm why?.
def get_note_service(session: Annotated[Session, Depends(get_session)]) -> NoteService:
    """
    Provides a NoteService instance injected with a database session.
    """
    return NoteService(session)


# --- TEACHING: TYPE ANNOTATIONS ---
# We use 'Annotated' to create a reusable dependency type.
# Now, any endpoint can simply request 'service: NoteServiceDep' to get
# a fully functional NoteService without repeating the Depends() logic.
# please if you don't understand, go research research too
NoteServiceDep = Annotated[NoteService, Depends(get_note_service)]


# --- TEACHING: POST (CREATE) ---
# We use status_code=201 (Created) because it is the standard HTTP response
# for successfully creating a new resource.
# hmm wans't it 200?, research.
@router.post("/", response_model=NoteResponse, status_code=201)
def create_note(note_data: NoteCreate, service: NoteServiceDep) -> Note:
    """
    TIP: CONTROLLER RESPONSIBILITY
    The controller's only job is to receive the request, hand the data
    to the service, and return the result. It doesn't know HOW the note
    is saved; it only knows that the Service will handle it.
    At this point, the controller is done. The service will handle the rest.
    so if you don't understand, go research research too
    """
    return service.create_note(note_data)


# --- TEACHING: GET (READ LIST) ---
# We use Query parameters for 'offset' and 'limit' to handle pagination.
# 'ge=0' (greater than or equal to 0) and 'le=100' (less than or equal to 100)
# are validation rules that FastAPI enforces automatically.
# Native Pagination available in cleaner manners in 3rd party libraries but it's not always the best choice or our focus now.
@router.get("/", response_model=Sequence[NoteResponse])
def read_notes(
    service: NoteServiceDep,
    offset: int = Query(default=0, ge=0),
    limit: int = Query(default=10, le=100),
) -> Sequence[Note]:
    """
    TEACHING: RESPONSE MODELS
    Notice we return a 'Sequence[Note]' (the database models), but FastAPI
    automatically filters them through 'NoteResponse' (the schema) before
    sending the JSON to the client hmm so what is the purpose of this?
    """
    return service.get_notes(offset=offset, limit=limit)


# --- TEACHING: GET (READ ONE) ---
# The '{note_id}' in the path is a variable. FastAPI extracts it from the
# URL and passes it to our function as an argument.
@router.get("/{note_id}", response_model=NoteResponse)
def read_note(note_id: int, service: NoteServiceDep) -> Note:
    """
    Retrieve detailed information about a specific note by its ID.
    """
    return service.get_note_by_id(note_id)


# --- TEACHING: PATCH (UPDATE) ---
# PATCH is used for partial updates (changing only some fields) so it's technically more efficient than PUT but it's a put.
# so what the hell is the protocol do we use to differentiate between PATCH and PUT?
# PUT would typically be used for replacing the entire resource.
@router.patch("/{note_id}", response_model=NoteResponse)
def update_note(note_id: int, note_data: NoteUpdate, service: NoteServiceDep) -> Note:
    """
    Update specific fields of an existing note really?.
    """
    return service.update_note(note_id, note_data)


# --- TEACHING: DELETE ---
# Deletion endpoints often return a simple success message or 204 No Content.
@router.delete("/{note_id}")
def delete_note(note_id: int, service: NoteServiceDep) -> dict[str, str]:
    """
    Remove a note from the system permanently.
    """
    return service.delete_note(note_id)
