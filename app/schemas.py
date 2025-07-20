from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

current_year = datetime.now().year

class BookBase(BaseModel):
    """Base fields for a book."""
    title: str = Field(..., example="Atomic Habits")
    author: str = Field(..., example="James Clear")
    published_year: int = Field(..., ge=1500, le=current_year, example=2018)
    summary: Optional[str] = Field(None, example="A guide to building good habits and breaking bad ones.")

class BookCreate(BookBase):
    """Fields required to create a book."""
    pass

class BookUpdate(BookBase):
    """Fields allowed for updating a book."""
    pass

class BookRead(BookBase):
    """Fields returned when reading a book."""
    id: int

    model_config = {
        "from_attributes": True  # Pydantic v2
    }
   
