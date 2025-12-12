from sqlalchemy.orm import Session
from src.db import models
from src.schema import note as schemas

def get_notes(db: Session):
    return db.query(models.Note).all()

def get_note(db: Session, note_id: int):
    return db.query(models.Note).filter(models.Note.id == note_id).first()

def create_note(db: Session, note_in: schemas.NoteCreate):
    note = models.Note(
        title = note_in.title,
        body = note_in.body,
    )
    
    db.add(note)
    db.commit()
    db.refresh(note)
    return note
