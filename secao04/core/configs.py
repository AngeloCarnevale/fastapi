from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    """
    Configurações gerais usadas na aplicação
    """
    API_V1_STR: str = '/api/v1'
    DB_URL: str = "mysql+asyncmy://root:1234@localhost:3307/fastapi"
    DBBaseModel = declarative_base()
    
    class Config:
        case_sensitive = True
        
settings = Settings()
    