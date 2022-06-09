import logging
from random import choice

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.status import HTTP_201_CREATED, HTTP_205_RESET_CONTENT, HTTP_200_OK

from ..models import Color
from ..schemas import Color
from .get_db import get_db
from app import crud


route = APIRouter()


log = logging.getLogger("uvicorn")


@route.get("/try", tags=["Trying to guess"], 
                description="Trying to guess the color of the object.", status_code=200)
async def get(number_obj: int, color: Color, db: Session = Depends(get_db)):
    """
    This route takes the ID of the item as input (as a number) and outputs the color of this item.

    The user does not know which number is the color of the object, 
                inside of this trying to guess the color by number.
    """
    db_object = crud.get_object(db, number_of_object=number_obj)
    if db_object is None:
        raise HTTPException(status_code=404, 
                            detail="Sorry, there is no item with this number.")
    if db_object.color == color:
        return f"YES! The item number {db_object.id} is really {db_object.color} color."
    return "Wrong, try again."


@route.post("/fillingdb", tags=["Сreate random items"], 
                description="Let's create a random group of 100 items." )
async def post(db: Session = Depends(get_db)):
    log.info("Initialize create objects for Database ...")
    for i in range(100):
        color = choice(Color.list())
        crud.create_object(db=db, color=color)
    log.info("Create objects for Database finish.")
    return HTTP_201_CREATED


@route.delete("/delete_all/", tags=["Clear"], 
                    description="If 'mix' is True, the objects will be mixed, else\
                                                    the only database cleanup will be performed.")
async def delete(mix: bool, db: Session = Depends(get_db)):
    """
    This route will be only clear database if 'mix' is false, else will be clear database first, and fill new\
                                                                                    random objects next..
    """
    crud.delete_all(db=db)
    if mix:
        log.info("Initialize create objects for Database ...")
        for i in range(100):
            color = choice(Color.list())
            crud.create_object(db=db, color=color)
        log.info("Create objects for Database finish.")
        return HTTP_200_OK
    return HTTP_205_RESET_CONTENT
