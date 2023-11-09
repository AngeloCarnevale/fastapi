from fastapi import FastAPI

from port.fastapi.config import configure_routers, configure_tortoise

def create_app() -> FastAPI:
    app = FastAPI()
    
    configure_routers(app)
    configure_tortoise(app)
    
    return app

core_module = create_app()