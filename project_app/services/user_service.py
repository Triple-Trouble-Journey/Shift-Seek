from base_models.user_model import User
from base_models.admin_model import Admin
from fastapi import HTTPException
from config.db_engine import read_query, insert_query, read_query_all_results
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

def add_admin(logged_user, email: str, db):

    is_admin = read_query(sqlalchemy_script.Admin, db, logged_user.user_id, 'users_id')
    if not is_admin:
        raise HTTPException(status_code=400, detail='You are not admin to do this!')

    current_user_info = read_query(sqlalchemy_script.User, db, email, 'email')
    if not current_user_info:
        raise HTTPException(status_code=404, detail='Email not found!')
    
    check_already_exist = read_query(sqlalchemy_script.Admin, db, current_user_info.user_id, 'users_id')
    admin_count = read_query_all_results(sqlalchemy_script.Admin, db, current_user_info.user_id, 'users_id')
    if admin_count is None:
        admin_count = 0

    if not check_already_exist:
        user_db = Admin(admin_id=admin_count, users_id=current_user_info.user_id)
        insert_query(sqlalchemy_script.Admin, db, user_db)
        raise HTTPException(status_code=200, detail=f'You successfully added {current_user_info.email} to admins!')
    else:
        raise HTTPException(status_code=400, detail='This user is already admin!')