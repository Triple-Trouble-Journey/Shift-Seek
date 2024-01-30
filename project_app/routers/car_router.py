from fastapi import APIRouter, status, HTTPException
from base_models.car_model import Car
from config.database import engine, db_dependency, insert_query, read_query
from db_models import models

car_router = APIRouter(prefix='/car')
models.Base.metadata.create_all(bind=engine)


@car_router.post('/add', status_code=status.HTTP_201_CREATED)
async def add_car(car: Car, db: db_dependency):
    insert_query(models.Car, db, car)

@car_router.get('/{car_id}', status_code=status.HTTP_200_OK)
async def all_cars(car_id: int, db: db_dependency):
    car = read_query(models.Car, db, car_id)
    if car is None:
        raise HTTPException(status_code=404, detail='Not found!')
    return car