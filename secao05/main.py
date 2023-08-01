from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware
from core.configs import settings
from api.v1.api import api_router


app: FastAPI = FastAPI(title='Users API - FastAPI ASQL Model')
app.include_router(api_router, prefix=settings.API_V1_STR)

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run("main:app", host='0.0.0.0', port=8000, reload=True, log_level="info")