from model import Note, Session
from schemas import NoteCreate, NoteUpdate
from sqlmodel import select
from fastapi import HTTPException
from datetime import datetime

class NoteManager:
    def __init__(self, session: Session):
        self.session = session

    # ---------------- CREATE ----------------
    def create(self, note_data: NoteCreate) -> Note:
        # Create a new Note from schema data
        note = Note(
            title=note_data.title,
            description=note_data.description,
            time=datetime.now()  # Auto-generate timestamp
        )
        self.session.add(note)
        self.session.commit()
        self.session.refresh(note)
        return note

    # ---------------- READ ALL ----------------
    def get_all(self, offset: int = 0, limit: int = 10):
        statement = select(Note).offset(offset).limit(limit)
        return self.session.exec(statement).all()

    # ---------------- READ BY ID ----------------
    def get_by_id(self, note_id: int) -> Note:
        note = self.session.get(Note, note_id)
        if not note:
            raise HTTPException(status_code=404, detail="Note not found")
        return note

    # ---------------- UPDATE ----------------
    def update(self, note_id: int, note_data: NoteUpdate) -> Note:
        db_note = self.get_by_id(note_id)
        
        # Update only the fields sent in the request
        update_data = note_data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_note, key, value)
        
        # Update the timestamp automatically
        db_note.time = datetime.now()
        
        self.session.add(db_note)
        self.session.commit()
        self.session.refresh(db_note)
        return db_note

    # ---------------- DELETE ----------------
    def delete(self, note_id: int):
        db_note = self.get_by_id(note_id)
        self.session.delete(db_note)
        self.session.commit()
        return {"status": "success", "message": "Note deleted successfully"}
