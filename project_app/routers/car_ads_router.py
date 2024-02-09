from fastapi import APIRouter, status, Depends, Query
from base_models.carad_model import InputCarAD
from config.auth import get_current_user
from config.db_engine import engine, db_dependency
from db_models import sqlalchemy_script
from services import car_ads_service

car_ads_router = APIRouter(prefix='/car_ads')
sqlalchemy_script.Base.metadata.create_all(bind=engine)

@car_ads_router.get('/all', status_code = status.HTTP_200_OK, tags = {'Car Ads Section'})

async def all_ads(db: db_dependency):

    return car_ads_service.view_ads(db)

@car_ads_router.post('/new', status_code=status.HTTP_200_OK, tags= {'Car Ads Section'})

async def create_new_ad(car_ad: InputCarAD, db: db_dependency, 
                        current_user_payload= Depends(get_current_user)):

    author_id = current_user_payload.user_id
    return car_ads_service.create_ad(author_id, car_ad, db)

@car_ads_router.put('/edit', status_code=status.HTTP_200_OK, tags= {'Car Ads Section'})

async def edit_ad(db: db_dependency,
               ad_id: int, 
               car_price: int = Query(None), 
               engine_type: str = Query(None),
               horsepowers: int = Query(None),
               cubic_capacity: int = Query(None),
               transmission: str = Query(None),
               car_type: str = Query(None),
               car_color: str = Query(None),
               car_mileage: int = Query(None),
               car_description: str = Query(None), 
              current_user_payload= Depends(get_current_user)):
    
    author_id = current_user_payload.user_id

    return car_ads_service.edit_ad(ad_id, author_id, car_price,engine_type, horsepowers,cubic_capacity
                                   ,transmission, car_type, car_color, car_mileage, car_description, db)