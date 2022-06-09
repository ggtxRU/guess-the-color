import logging

from fastapi import FastAPI


from . import models
from .db import engine
from .api.object import route


log = logging.getLogger("uvicorn")


def include_route(app) -> None:
    app.include_router(route)
 

def create_tables() -> None:
    models.Base.metadata.create_all(bind=engine)


def start_app() -> FastAPI:
    app = FastAPI(
        title="GuessTheColor",
        version="0.0.1",
        description="Developer: Kulakov Kirill i.e. ggtx."
    )
    include_route(app)
    create_tables()
    return app


log.info("Initializing service")
app  = start_app()
log.info("Service finished initializing")
