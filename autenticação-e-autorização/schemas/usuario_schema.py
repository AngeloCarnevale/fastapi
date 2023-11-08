from typing import Optional, List

from pydantic import BaseModel, EmailStr

from schemas.artigo_schema import ArtigoSchema


class UsuarioSchemaBase(BaseModel):
    id: Optional[int]
    nome: str 
    sobrenome: str
    email: EmailStr
    is_admin: bool = False
    
    class Config:
        from_attributes = True
        

class UsuarioSchemaCreate(UsuarioSchemaBase):
    senha: str
    
class UsuarioSchemaArtigos(UsuarioSchemaBase):
    artigos: Optional[List[ArtigoSchema]]
    
class UsuarioSchemaUp(UsuarioSchemaBase):
    nome: Optional[str]
    sobrenome: Optional[str]
    email: Optional[EmailStr]
    senha: Optional[str]
    is_admin: Optional[bool]