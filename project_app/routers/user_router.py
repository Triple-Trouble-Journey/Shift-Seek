from fastapi import APIRouter, status, HTTPException
from base_models.user_model import UserRegiser
from config.db_engine import engine, db_dependency, read_query
from db_models import sqlalchemy_script
from services import user_service

user_router = APIRouter(prefix='/user')
sqlalchemy_script.Base.metadata.create_all(bind=engine)


@user_router.get('/', status_code=status.HTTP_200_OK)
def get_user(username: str, db: db_dependency):
    current_property = 'username'
    user = read_query(sqlalchemy_script.User, db, username, current_property)
    if user is None:
        raise HTTPException(status_code=404, detail='Not found!')
    return user

@user_router.post('/', status_code=status.HTTP_201_CREATED)
def add_user(user: UserRegiser, db: db_dependency):
    

    new_user = user_service.create_user(user, db)

    return new_user