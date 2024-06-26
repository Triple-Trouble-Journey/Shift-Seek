from fastapi import APIRouter, status, HTTPException, Depends
from base_models.car_model import Car
from config.auth import get_current_user
from config.db_engine import engine, db_dependency, insert_query, read_query
from db_models import sqlalchemy_script


car_router = APIRouter(prefix='/car')
sqlalchemy_script.Base.metadata.create_all(bind=engine)

@car_router.get("/brand", status_code=status.HTTP_200_OK, tags= {'Car Section'})

def find_car_by_brand(brand: str, db: db_dependency, current_user_payload=Depends(get_current_user)):
    current_property = 'brand'
    car = read_query(sqlalchemy_script.Car, db, brand, current_property)
    if car is None:
        raise HTTPException(status_code=404, detail='Not found!')
    return car

@car_router.post('/add', status_code=status.HTTP_201_CREATED, tags= {'Car Section'})

async def add_car(car: Car, db: db_dependency, current_user_payload=Depends(get_current_user)):
    insert_query(sqlalchemy_script.Car, db, car)

@car_router.get('/{car_id}', status_code=status.HTTP_200_OK, tags= {'Car Section'})

async def car_by_id(car_id: int, db: db_dependency, current_user_payload=Depends(get_current_user)):
    current_property = 'car_id'
    car = read_query(sqlalchemy_script.Car, db, car_id, current_property)
    if car is None:
        raise HTTPException(status_code=404, detail='Not found!')
    return car

@car_router.get("/", status_code=status.HTTP_200_OK, tags= {'Car Section'})

async def all_cars(db: db_dependency, current_user_payload=Depends(get_current_user)):
    car = db.query(sqlalchemy_script.Car).all()
    return car
