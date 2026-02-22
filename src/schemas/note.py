from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class NoteBase(BaseModel):
    """
    --- CONCEPT: THE BASE SCHEMA ---
    This is a 'Base' schema using Pydantic. Schemas (or DTOs - Data Transfer Objects "VIP CONCEPT)
    are different from Models because they define what data we accept from! or
    send to the client!, rather than how data is stored in the database.

    Using a Base class allows us to share common fields between 'Create',
    'Update', and 'Response' schemas to keep our code DRY (Don't Repeat Yourself).
    """

    title: str = Field(..., min_length=1, max_length=100)
    description: str | None = Field(None, max_length=5000)
    priority: int = Field(lt=6,gt=0,default=1)
    category_id: int 

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "Grocery List",
                "description": "Buy milk, eggs, and bread",
                "priority": 3,
                "category_id": 1,
            }
        }
    }


class NoteCreate(NoteBase):
    """
    --- TEACHING: CREATION SCHEMA ---
    When a user creates a note, they only send the title and description.
    We inherit from NoteBase to get those fields.
    We don't include 'id' or 'time' here because those are generated
    automatically by the system/database, and we don't want the user to provide them.
    """

    pass


class NoteUpdate(BaseModel):
    """
    --- TEACHING: UPDATE SCHEMA ---
    For updates, we typically want all fields to be optional.
    This allows 'Partial Updates' (PATCH), where a user can change just the
    title without having to resend the description, and vice versa.
    """

    title: str | None = Field(None, min_length=1, max_length=100)
    description: str | None = Field(None, max_length=5000)
    priority: int | None = Field(None,lt=6,gt=0,default=1)
    category_id: int | None = None


    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "Updated Grocery List",
                "description": "Buy milk, eggs, bread, and butter",
                "priority": 3,
                "category_id": 1,
            }
        }
    }


class NoteResponse(NoteBase):
    """
    --- TEACHING: RESPONSE SCHEMA ---
    This schema defines exactly what the API returns to the user.
    It includes the 'id' and 'time' which weren't in the creation schema.

    SECURITY TIP: Never return your internal Database Model directly SONDODS+YEHIA.
    Using a Response Schema ensures you don't accidentally leak sensitive
    internal fields (like password hashes or internal metadata).
    """

    id: int
    time: datetime

    # easypeasy: from_attributes (formerly orm_mode)
    # This setting allows Pydantic to read data from database objects
    # (like SQLModel instances) and convert them into JSON-compatible
    # dictionaries automatically.
    model_config = ConfigDict(from_attributes=True)
