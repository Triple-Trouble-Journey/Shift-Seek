from base_models.user_model import User
from config.db_engine import read_query, insert_query
from db_models import sqlalchemy_script


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
