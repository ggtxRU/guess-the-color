from pydantic import BaseModel

from .models import Enum


class Obj(BaseModel):
    color : str


class Color(str, Enum):
    Blue = "Blue"
    Red = "Red"
    Green = "Green"
