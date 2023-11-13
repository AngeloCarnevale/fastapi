from fastapi import FastAPI
from port.fastapi.router import post as post_router
from tortoise.contrib.fastapi import register_tortoise
from dotenv import load_dotenv
import os

load_dotenv()

def configure_routers(app: FastAPI):
    app.include_router(post_router.router)
    
def configure_tortoise(app: FastAPI):
    register_tortoise(
        app=app,
        generate_schemas=True,
        db_url=os.environ.get("DATABASE_URL"),
        modules={
            'models': [
                'adapter.schemas.post'
            ],
        }
    )