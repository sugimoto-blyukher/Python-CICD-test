from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.db.session import get_db
from src.db import crud
from src.schema import note as schemas

from src.core.config import Setting
from src.deps import get_settings
from src.core.logging import logger

router = APIRouter()

@router.get("/", response_model=list[schemas.NoteOut])
def list_notes(db: Session = Depends(get_db)):
    return crud.get_notes(db)

@router.post(
    "/",
    response_model=schemas.NoteOut,
    status_code=status.HTTP_201_CREATED
)
def create_note(
    note_in: schemas.NoteCreate,
    db: Session = Depends(get_db),
):
    return crud.create_note(db, note_in)

@router.get("/{note_id}", response_model=schemas.NoteOut)
def get_note(note_id: int, db: Session = Depends(get_db)):
    note = crud.get_note(db, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

@router.get("/debug")
def debug_config(cfg: Setting = Depends(get_settings)):
    return {"app": cfg.app_name}

@router.get("/{note_id}")
def get_note(note_id: int, db: Session = Depends(get_db)):
    logger.info(f"GET /note/{note_id}")
    note = crud.get_note(db, note_id)
    if not note:
        logger.warning(f"Note not found: {note_id}")
        raise HTTPException(status_code=404,detail="Note not found")
    return note