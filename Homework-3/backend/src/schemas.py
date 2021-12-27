from typing import Optional
from pydantic import BaseModel


class Restaurant(BaseModel):
    id_: Optional[int]
    name: str
    rating: float
    lat: float
    lon: float

    class Config:
        orm_mode = True
