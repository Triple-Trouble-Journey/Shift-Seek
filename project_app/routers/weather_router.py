from fastapi import APIRouter
from config.db_engine import engine
from db_models import sqlalchemy_script
from common.weather_api import get_city_weather

weather_router = APIRouter(prefix='/weather')
sqlalchemy_script.Base.metadata.create_all(bind=engine)


@weather_router.get('/{city}', tags=['Weather Section'])
async def get_weather(city: str):

    return get_city_weather(city)