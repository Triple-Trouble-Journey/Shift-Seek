from base_models.user_model import User
from config.db_engine import read_query, insert_query, delete_query
from db_models import sqlalchemy_script
from db_models.sqlalchemy_script import db_user_info
from fastapi import HTTPException
from base_models.user_model import update_user_info


def get_user_id_by_username(username: str, db):

    current_property = 'username'
    current_user_info = read_query(sqlalchemy_script.User, db, username, current_property)

    if current_user_info:

        return current_user_info.user_id
    else:
        return None


def get_user_id(username, db) -> None | User:
    current_id_user = get_user_id_by_username(username, db)
    current_property = 'user_id'
    user_info = read_query(sqlalchemy_script.User, db, current_id_user, current_property)

    if user_info:
        return user_info
    else:
        return None


def create_user(user_info, db):

    from services.authorization_service import get_password_hash

    hashed_pass = get_password_hash(user_info.password)
    user_info.password = hashed_pass
    insert_query(sqlalchemy_script.User, db, user_info)

def edit_user_info(user_id, first_name,  last_name, address, telephone, db):

    updating_user = db.query(sqlalchemy_script.User).filter(
        getattr(sqlalchemy_script.User, 'user_id') == user_id,
        getattr(sqlalchemy_script.User, 'first_name') == first_name,
        getattr(sqlalchemy_script.User, 'last_name') == last_name,
        getattr(sqlalchemy_script.User, 'address') == address,
        getattr(sqlalchemy_script.User, 'telephone') == telephone,   
    ).first()
    
    if updating_user:
        update_user_info(user_id, first_name, last_name, address, telephone, db)
        
        raise HTTPException(status_code=200, detail='You have updated your personal information!')
    