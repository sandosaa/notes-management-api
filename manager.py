from model import Note,SessionDep
from sqlmodel import select, Session
from fastapi import HTTPException
from datetime import datetime   

class NoteManager:
    def __init__(self, session: Session):
        self.session = session

    def create(self, note: Note) -> Note:
        self.session.add(note)
        self.session.commit()
        self.session.refresh(note)
        return note

    def get_all(self, offset: int, limit: int):
        statement = select(Note).offset(offset).limit(limit)
        return self.session.exec(statement).all()

    def get_by_id(self, note_id: int) -> Note:
        note = self.session.get(Note, note_id)
        if not note:
            # Raise exception if ID is not found
            raise HTTPException(status_code=404, detail="Note not found")
        return note

    def update(self, note_id: int, note_data: Note) -> Note:
        db_note = self.get_by_id(note_id) # Reuse search logic
        
        # Convert input to dict and update fields
        data = note_data.model_dump(exclude_unset=True)
        for key, value in data.items():
            setattr(db_note, key, value)
        
        # Update timestamp on modification
        db_note.time = datetime.now()
        
        self.session.add(db_note)
        self.session.commit()
        self.session.refresh(db_note)
        return db_note

    def delete(self, note_id: int):
        db_note = self.get_by_id(note_id)
        self.session.delete(db_note)
        self.session.commit()
        return {"status": "success", "message": "Note deleted successfully"}