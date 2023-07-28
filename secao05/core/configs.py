from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'mysql+asyncmy://root:1234@localhost:3307/fastapi'
    
    class Config:
        case_sensitive = True
        
        
settings: Settings = Settings() 
