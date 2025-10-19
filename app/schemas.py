from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class EntryBase(BaseModel):
    title: str
    content: str

class EntryCreate(EntryBase):
    pass

class EntryUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None

class EntryOut(EntryBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
