from collections.abc import Sequence
from datetime import datetime

from fastapi import HTTPException
from sqlmodel import Session, select

from src.models.note import Note
from src.schemas.note import NoteCreate, NoteUpdate


class NoteService:
    """
    --- CONCEPT: THE SERVICE LAYER ---
    The Service layer is where the "Business Logic" of oour application lives.
    By moving logic out of the API routes (Controllers) and into Services,
    we make our code reusable and easier to test.
    The Controller handles the HTTP request, while the Service handles the
    actual data processing and database interaction.
    """

    def __init__(self, session: Session) -> None:
        """
        TEACHING: DEPENDENCY INJECTION AGAIN
        We "inject" the database 'Session' into the service. This decouples the
        service from the creation of the connection, making it much easier to
        swap the session for a "Mock" session during unit testing.
        """
        self.session = session

    def create_note(self, note_data: NoteCreate) -> Note:
        """
        NOTE LIFE CYCLE : CREATING DATA
        1. Transform Schema (NoteCreate) into a Model (Note).
        2. 'self.session.add(db_note)': Tell the session to track this object.
        3. 'self.session.commit()': Save the changes to the database file.
        4. 'self.session.refresh(db_note)': Pull the latest data from the DB
           back into ou object to populate generated fields like 'id'.
        """
        db_note = Note(
            title=note_data.title,
            description=note_data.description,
            time=datetime.now(),
        )
        self.session.add(db_note)
        self.session.commit()
        self.session.refresh(db_note)
        return db_note

    def get_notes(self, offset: int = 0, limit: int = 10) -> Sequence[Note]:
        """
        TEACHING: PAGINATION
        Querying thousands of records at once is slow. 'offset' skips records,
        and 'limit' restricts the amount returned, allowing the frontend to
        load data in small "pages" again we can use 3rd but it's ok for now.
        """
        statement = select(Note).offset(offset).limit(limit)
        return self.session.exec(statement).all()

    def get_note_by_id(self, note_id: int) -> Note:
        """
        TEACHING: ERROR HANDLING
        'session.get()' finds a row by Primary Key. If the note doesn't exist,
        we raise an 'HTTPException'. FastAPI catches this and sends a clean
        JSON error message with a 404 status code to the client "SONDOS".
        """
        note = self.session.get(Note, note_id)
        if not note:
            raise HTTPException(status_code=404, detail="Note not found")
        return note

    def update_note(self, note_id: int, note_data: NoteUpdate) -> Note:
        """
        TEACHING: PARTIAL UPDATES (PATCH)
        1. Find the existing note first.
        2. 'model_dump(exclude_unset=True)' only returns the fields the user
           specifically sent. If they only sent a 'title', we only update that.
        3. 'setattr' updates the model attribute dynamically.
        """
        db_note = self.get_note_by_id(note_id)

        # Update only the fields provided in the update schema
        update_dict = note_data.model_dump(exclude_unset=True)
        for key, value in update_dict.items():
            setattr(db_note, key, value)

        # Update the timestamp on modification
        db_note.time = datetime.now()

        self.session.add(db_note)
        self.session.commit()
        self.session.refresh(db_note)
        return db_note

    def delete_note(self, note_id: int) -> dict[str, str]:
        """
        TEACHING: DELETION
        Deleting from a database is a two-step process in SQLModel:
        1. Tell the session to delete the object.
        2. Commit the transaction to make the removal permanent.
        """
        db_note = self.get_note_by_id(note_id)
        self.session.delete(db_note)
        self.session.commit()
        return {
            "status": "success",
            "message": f"Note {note_id} deleted successfully",
        }
