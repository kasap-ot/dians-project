from typing import Optional
from pydantic import BaseModel


class BaseRestaurant(BaseModel):
    name: str
    rating: float
    lat: float
    lon: float

    class Config:
        orm_mode = True


class ReadRestaurant(BaseRestaurant):
    id_: int


class CreateRestaurant(BaseRestaurant):
    ...
