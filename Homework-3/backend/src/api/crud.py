from typing import List
from fastapi import APIRouter
from fastapi_sqlalchemy import db
from src.db import connection
from src.models import Restaurant as RestaurantModel
from src.schemas import ReadRestaurant as ReadRestaurantSchema
from src.schemas import CreateRestaurant as CreateRestaurantSchema


router = APIRouter(prefix="/crud", tags=["crud"])


@router.get("/restaurants", response_model=List[ReadRestaurantSchema])
def get_all():
    return db.session                   \
            .query(RestaurantModel)     \
            .all()


@router.get("/restaurants/{id_}", response_model=ReadRestaurantSchema)
def get_by_id(id_: int):
    return db.session                               \
            .query(RestaurantModel)                 \
            .get(id_)


@router.post("/restaurants", response_model=ReadRestaurantSchema)
def create(restaurant_schema: CreateRestaurantSchema):
    restaurant_dict = restaurant_schema.dict()
    restaurant_model = RestaurantModel(**restaurant_dict)
    db.session.add(restaurant_model)
    db.session.commit()
    return restaurant_schema



@router.delete("/restaurants/{id_}", response_model=ReadRestaurantSchema)
def delete(id_: int):
    restaurant_model = db.session.query(RestaurantModel).get(id_)
    db.session.delete(restaurant_model)
    db.session.commit()
    return restaurant_model
