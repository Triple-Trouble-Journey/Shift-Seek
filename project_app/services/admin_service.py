from base_models.admin_model import Admin
from config.db_engine import insert_query, read_query
from db_models import sqlalchemy_script


def get_user_id_by_username(username: str, db):

    current_property = 'username'
    current_user_info = read_query(sqlalchemy_script.User, db, username, current_property)

    return current_user_info.user_id

def get_admin_id(username, db) -> None | Admin:
    current_id_user = get_user_id_by_username(username, db)
    current_property = 'admin_id'
    admin_id = read_query(sqlalchemy_script.Admin, db, current_id_user, current_property)

    return admin_id
