from pydantic import BaseModel


class Restaurant(BaseModel):
    name: str
    rating: float
    lan: float
    lon: float

    class Config:
        orm_mode = True