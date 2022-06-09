from enum import Enum as Enum_
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .db import Base

class Enum(Enum_):
    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))


class Color(str, Enum):
    Blue1 = "Blue"
    Blue2 = "Blue"
    Blue3 = "Blue"
    Blue4 = "Blue"
    Blue5 = "Blue"
    Blue6 = "Blue"
    Green1 = "Green"
    Red1 = "Red"
    Red2 = "Red"
    Red3 = "Red"

class Object(Base):
    __tablename__ = "Objects"

    id = Column(Integer, primary_key=True, index=True)
    color = Column(String, default="Blue") 
    
