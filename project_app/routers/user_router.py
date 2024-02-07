from fastapi import APIRouter, status, HTTPException, Depends
from base_models.user_model import UserRegiser, User
from config.db_engine import engine, db_dependency, read_query, delete_query
from db_models import sqlalchemy_script
from services import user_service
from config.auth import get_current_user
from common.user_information import user_result

user_router = APIRouter(prefix='/users')
sqlalchemy_script.Base.metadata.create_all(bind=engine)

#TODO:
@user_router.put('/', status_code=status.HTTP_200_OK, tags= {'User Section'})

async def edit_your_profile_information(first_name: str,  
                                         db: db_dependency, current_user_payload= Depends(get_current_user)):

    # Needs additional fixing
    # To be continue


    
    db_record = db.query(sqlalchemy_script.User.first_name).filter(sqlalchemy_script.User.first_name == first_name).first()

    if db_record:
        db.delete(db_record)
        db.add(db_record)
        db.commit()
        return ("Edited successfully")


@user_router.delete('/', status_code=status.HTTP_200_OK, tags= {'Admin Section'})

async def ban_a_specific_user(user_id: int, db: db_dependency, current_user_payload= Depends(get_current_user)):

    db_record = db.query(sqlalchemy_script.User).filter(sqlalchemy_script.User.user_id == user_id).first()
    if db_record:
        db.delete(db_record)
        db.commit()
        return {f"User with ID: {user_id} was deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail= 'This user was not found')

@user_router.get('/information', status_code=status.HTTP_200_OK, tags= {'User Section'})

async def personal_information(db: db_dependency, current_user_payload= Depends(get_current_user)):

    username_info = current_user_payload.username
    
    current_property = 'username'
    user_information = read_query(sqlalchemy_script.User, db, username_info, current_property)
    if user_information is None:
        raise HTTPException(status_code=404, detail='Not found!')
    
    return user_result(user_information)

@user_router.get('/name', status_code=status.HTTP_200_OK, tags= {'User Section'})

def find_user_by_name(username: str, db: db_dependency, current_user_payload= Depends(get_current_user)):

    current_property = 'username'
    user = read_query(sqlalchemy_script.User, db, username, current_property)
    if user is None:
        raise HTTPException(status_code=404, detail='Not found!')
    
    return user_result(user)

@user_router.post('/', status_code=status.HTTP_201_CREATED, tags= {'Registration'})

def registration(user: UserRegiser, db: db_dependency):
    
    new_user = user_service.create_user(user, db)

    return new_user

@user_router.get("/",status_code=status.HTTP_200_OK, tags= {'Admin Section'})

async def get_all_users(db: db_dependency, current_user_payload= Depends(get_current_user)):
    users = db.query(sqlalchemy_script.User).all()
    return users

@user_router.get('/{user_id}', status_code=status.HTTP_200_OK, tags= {'User Section'})

async def user_by_id(user_id: int, db: db_dependency, current_user_payload= Depends(get_current_user)):
    current_property = 'user_id'
    user = read_query(sqlalchemy_script.User, db, user_id, current_property)
    if user is None:
        raise HTTPException(status_code=404, detail='Not found!')
    return {
        "Id": user.user_id,
        "Username": user.username,
        "Email": user.email,
        "First Name": user.first_name,
        "Last Name": user.last_name,
        "Address": user.address,
        "Telephone": user.telephone,
    }