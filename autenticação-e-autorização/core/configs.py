from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.decl_api import DeclarativeMeta


class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'mysql+asyncmy://root:1234@localhost:3307/fastapi'
    DB_BASE_MODEL: DeclarativeMeta = declarative_base()
    
    JWT_SECRET: str = 'tFQKIFuyPmSjCFax1gph83uioRs3BGeUsut8nFkMfJc'
    
    ALGORITHM: str = 'HS256'
    # 60 minutos * 24 horas * 7 dias => 1 semana
    ACESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7
    
    class Config:
        case_sesitive = True
        

settings: Settings = Settings()