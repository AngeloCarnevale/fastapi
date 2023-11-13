from fastapi import APIRouter

from api.v1.endpoints import artigo
from api.v1.endpoints import user
from api.v1.endpoints import github_provider


api_router = APIRouter()

api_router.include_router(artigo.router, prefix='/artigos', tags=['Artigos'])
api_router.include_router(user.router, prefix='/usuarios', tags=['Usuários'])
api_router.include_router(github_provider.router, prefix='/github', tags=['Github Provider'])