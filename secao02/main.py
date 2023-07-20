from fastapi import FastAPI


app = FastAPI()

@app.get('/')
async def raiz():
    return {"msg": "random message"}

@app.get('/hello')
async def raiz():
    return {"msg": "hello world"}


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
    