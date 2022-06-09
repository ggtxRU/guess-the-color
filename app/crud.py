import logging
from sqlalchemy.orm import Session

import models


log = logging.getLogger("uvicorn")


def get_object(db: Session, number_of_object: int):
    return db.query(models.Object).filter(models.Object.id == number_of_object).first()


def create_object(db: Session, color):
    db_object = models.Object(color=color)
    db.add(db_object)
    db.commit()
    db.refresh(db_object)
    return db_object


def delete_all(db: Session):
    """Delete all from DB"""
    log.info("Initialize clearing Database ...")
    db_object = db.query(models.Object).first()
    while db_object:
        db.delete(db_object)
        db.commit()
        db_object = db.query(models.Object).first()
    log.info("Clearing Database is finish.")
    