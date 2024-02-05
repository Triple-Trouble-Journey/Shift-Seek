from fastapi import APIRouter, status, HTTPException, Depends
from base_models.car_model import Car
from config.auth import get_current_user
from config.db_engine import engine, db_dependency, insert_query, read_query
from db_models import sqlalchemy_script

car_ads_router = APIRouter(prefix='/car_ads')

@car_ads_router.post('/', status_code=status.HTTP_200_OK, tags= {'Car Ads Section'})

async def create_new_ad(db: db_dependency, current_user_payload= Depends(get_current_user)):

    username_info = current_user_payload.username
    

    #to be continued (use insert query)

    # current_property = 'username'
    # user_information = read_query(sqlalchemy_script.Car, db, username_info, current_property)
    # if user_information is None:
    #     raise HTTPException(status_code=404, detail='Not found!')
    
    # return user_information