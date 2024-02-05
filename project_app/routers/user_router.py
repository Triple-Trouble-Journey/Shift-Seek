from fastapi import APIRouter, status, HTTPException, Depends
from base_models.user_model import UserRegiser
from config.db_engine import engine, db_dependency, read_query
from db_models import sqlalchemy_script
from services import user_service
from config.auth import get_current_user
from services import user_service

user_router = APIRouter(prefix='/user')
sqlalchemy_script.Base.metadata.create_all(bind=engine)


@user_router.patch('/add/admin', status_code=status.HTTP_200_OK, tags={'Admin Section'})
def make_admin(email: str, db: db_dependency, 
               current_user_payload = Depends(get_current_user)):

    return user_service.add_admin(current_user_payload, email, db)

@user_router.get('/name', status_code=status.HTTP_200_OK, tags= {'User Section'})

def find_user_by_name(username: str, db: db_dependency):

    current_property = 'username'
    user = read_query(sqlalchemy_script.User, db, username, current_property)
    if user is None:
        raise HTTPException(status_code=404, detail='Not found!')
    return user

@user_router.post('/', status_code=status.HTTP_201_CREATED, tags= {'User Section'})

def registration(user: UserRegiser, db: db_dependency):
    
    new_user = user_service.create_user(user, db)

    return new_user

@user_router.get("/",status_code=status.HTTP_200_OK, tags= {'Admin Section'})

async def get_all_users(db: db_dependency):
    users = db.query(sqlalchemy_script.User).all()
    return users

@user_router.get('/{user_id}', status_code=status.HTTP_200_OK, tags= {'User Section'})

async def user_by_id(user_id: int, db: db_dependency):
    current_property = 'user_id'
    user = read_query(sqlalchemy_script.User, db, user_id, current_property)
    if user is None:
        raise HTTPException(status_code=404, detail='Not found!')
    return user