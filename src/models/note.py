from datetime import datetime

from sqlmodel import Field, SQLModel


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

    # TEACHING: Automatic Timestamps
    # 'default_factory=datetime.now' is a powerful feature.
    # Instead of a static value, it calls the function 'datetime.now'
    # every time a new Note object is created, ensuring an accurate timestamp.
    # so what is a factory function?
    time: datetime = Field(default_factory=datetime.now)
