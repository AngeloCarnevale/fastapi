from fastapi import FastAPI

app = FastAPI()

@app.get('/api/v1/students')
async def index():
    return {"hello": 'world'}

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
    