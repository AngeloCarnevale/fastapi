from fastapi import FastAPI


app = FastAPI()

cursos = {
    1: {
        "titulo": "Programação para leigos",
        "aulas": 112,
        "horas": 58
    },
    2: {
        "titulo": "Algorítmos e Lógica de Programação",
        "aulas": 87,
        "horas": 67
    }
}

@app.get('/cursos')
async def get_cursos():
    return cursos

@app.get('/')
async def get_cursos():
    return "Home"


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)