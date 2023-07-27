from fastapi import FastAPI

from routes import curso_router
from routes import user_router


app = FastAPI()

app.include_router(curso_router.router, tags=['Cursos'])
app.include_router(user_router.router, tags=['Usuários'])

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
    