from typing import List
from fastapi import APIRouter
from fastapi_sqlalchemy import db
from src.db import connection
from src.models import Restaurant as RestaurantModel
from src.schemas import Restaurant as RestaurantSchema, UpdateRestaurant


router = APIRouter(prefix="/crud", tags=["crud"])


@router.get("/restaurants", response_model=List[RestaurantSchema])
def get_all():
    return db.session                   \
            .query(RestaurantModel)     \
            .all()


@router.get("/restaurants/{id_}", response_model=RestaurantSchema)
def get_by_id(id_: int):
    return db.session                               \
            .query(RestaurantModel)                 \
            .get(id_)


@router.post("/restaurants", response_model=RestaurantSchema)
def create(restaurant_schema: RestaurantSchema):
    restaurant_dict = restaurant_schema.dict()
    restaurant_model = RestaurantModel(**restaurant_dict)
    db.session.add(restaurant_model)
    db.session.commit()
    return restaurant_schema



@router.delete("/restaurants/{id_}")
def delete(id_: int):
    restaurant_model = db.session.query(RestaurantModel).get(id_)
    db.session.delete(restaurant_model)
    db.session.commit()
    return restaurant_model
