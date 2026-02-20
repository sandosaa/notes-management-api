from enum import Enum
from datetime import datetime
from typing import List
from sqlmodel import Field, SQLModel, Relationship

class CategoryType(str,Enum):
    PERSONAL = 'personal'
    STUDY = "study"
    WORK = "work"
    HOME = "home"
    HEALTH = "health"
    IDEA = 'idea'
    OTHER = "other"

class Category(SQLModel,table=True):
    id: int | None = Field(default=None,primary_key=True,index=True)

    types: CategoryType = Field(default=CategoryType.PERSONAL) # we will make a static database for it now. 
    # maybe in the feature will make the user makes its list of category
    notes: List["Note"] = Relationship(back_populates="category") 


class Note(SQLModel, table=True):
    """
    --- Zatuna: WHATTA THE HELL DATA MODEL ---
    In SQLModel, a class serves two purposes simultaneously:
    1. It is a 'Table Model': Defines how the data looks in the database (SQL).
    2. It is a 'Data Schema': Defines how the data looks in Python (Pydantic).

    By setting 'table=True', we tell SQLModel that this class should correspond
    to a physical table in our SQLite database.
    """

    # CONCEPT: Primary Keys we define
    # The 'id' is our unique identifier for every note.
    # We set it to 'int | None' because when we create a note in Python,
    # it doesn't have an ID yet; the database assigns it automatically.
    id: int | None = Field(default=None, primary_key=True)

    # TEACHING: Field Validation
    # 'min_length=1' ensures we never save an empty title.
    # 'max_length' constraints help optimize database storage and prevent abuse.
    title: str = Field(min_length=1, max_length=100)

    # CONCEPT: Optional Fields
    # By using 'str | None', we allow the description to be empty (null).
    # SHAHD.
    description: str | None = Field(default=None, max_length=5000)

    priority: int = Field(lt=6,gt=0,default=1)

    category_id: int = Field(foreign_key="category.id")

    category: Category = Relationship(back_populates="notes")
    
    # TEACHING: Automatic Timestamps
    # 'default_factory=datetime.now' is a powerful feature.
    # Instead of a static value, it calls the function 'datetime.now'
    # every time a new Note object is created, ensuring an accurate timestamp.
    # so what is a factory function?
    time: datetime = Field(default_factory=datetime.now)
