import uuid
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from db.session import get_db
from db import crud
from schema import note as schemas

from core.config import Settings 
from deps import get_settings
from core.logging import logger

router = APIRouter(prefix="/users", tags=['users'])
