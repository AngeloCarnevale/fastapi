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


@app.get('/')
async def get_cursos():
    return "Home"

@app.get('/cursos')
async def get_cursos():
    return cursos

@app.get('/cursos/{curso_id}')
async def get_cursos(curso_id: int):
    curso = cursos[curso_id]
    
    return curso


if __name__ == "__main__":
    import uvicorn
    
    
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)