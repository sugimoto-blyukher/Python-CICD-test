from pydantic_settings import BaseSettings

class Setting(BaseSettings):
    app_name: str = "Memo API"
    secret_key: str = "CHANGE_ME"
    
    class Config:
        env_file = ".env"
        
settings = Setting()

