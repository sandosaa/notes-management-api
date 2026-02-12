from typing import Annotated
from fastapi import Depends
from sqlmodel import Field, Session, SQLModel, create_engine
from datetime import datetime

# -------- Model --------
class Note(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str = Field(min_length=1, max_length=100)
    description: str | None = Field(default=None, max_length=5000)  
    time: datetime = Field(default_factory=datetime.now)

# -------- Database setup --------
database = "sqlite:///database.db"
engine = create_engine(database, connect_args={"check_same_thread": False})

def create_all_eng():
    SQLModel.metadata.create_all(engine)

# -------- Session dependency --------
def start_session():
    with Session(engine) as session:
        try:
            yield session
        finally:
            session.close()

SessionDep = Annotated[Session, Depends(start_session)]
