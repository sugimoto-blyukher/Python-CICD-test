from datetime import datetime
from pydantic import BaseModel

class NoteBase(BaseModel):
    title: str
    body: str | None = None

class NoteCreate(NoteBase):
    pass

class NoteUpdate(BaseModel):
    title: str | None = None
    body: str | None = None
    
class NoteOut(NoteBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True