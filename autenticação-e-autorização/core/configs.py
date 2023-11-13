from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.decl_api import DeclarativeMeta
from dotenv import load_dotenv
import os

load_dotenv()


class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = os.environ.get('DB_URL') 
    DB_BASE_MODEL: DeclarativeMeta = declarative_base()
    
    JWT_SECRET: str = 'tFQKIFuyPmSjCFax1gph83uioRs3BGeUsut8nFkMfJc'
    
    ALGORITHM: str = 'HS256'
    
    ACESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7
    
    class Config:
        case_sesitive = True
        

settings: Settings = Settings()