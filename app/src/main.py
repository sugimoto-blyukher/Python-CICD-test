from fastapi import FastAPI
from app.src.api import note, users

def create_app() -> FastAPI:
    app = FastAPI(title="Memo API")
    
    app.include_router(note.router, prefix="/note", tags=["note"])
    app.include_router(users.router, prefix="/users", tags=["users"])
    
    return app

app = create_app()