from datetime import datetime, timedelta
from jose import jwt, JWTError
from passlib.context import CryptContext
from base_models.user_model import User
from config.db_engine import read_query
from services import user_service
from fastapi import HTTPException
from db_models.sqlalchemy_script import db_users


_SECRET_KEY = '2d776838352e75a9f95de915c269c8ce45b12de47f720213c5f71c4e25618c25'
_CUSTOM_SECRET_KEY = 'b1b2c3d4e5f6g7890123456789abcdef0123456789194def0123456789e2186a'
_ALGORITHM = 'HS256'
_TOKEN_EXPIRATION_TIME_MINUTES = timedelta(minutes=10000)

pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")


def verify_password(text_password, hashed_password):
    return pwd_context.verify(text_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def _get_pass_by_username(username, db):
    current_property = 'username'
    user_info = read_query(db_users,db,username, current_property)
    hashed_password = user_info.password

    if hashed_password:
        return hashed_password
    else:
        return None



def authenticate_user(username: str, password: str, db) -> bool | User:
    user = user_service.get_user_id(username, db)
    if not user:
        return False
    if not verify_password(password, _get_pass_by_username(username, db)):
        return False

    return user


def create_access_token(user_data, expiration_delta: timedelta = _TOKEN_EXPIRATION_TIME_MINUTES):
    to_encode = {
        "id": user_data.user_id,
        "username": user_data.username,
        "email": user_data.email,
        "expire": (datetime.now() + expiration_delta).isoformat()
    }

    encoded_jwt = jwt.encode(to_encode, _SECRET_KEY, algorithm=_ALGORITHM)
    return encoded_jwt


def is_authenticated(token: str):
    try:
        return jwt.decode(token, _SECRET_KEY, algorithms=[_ALGORITHM])
    except JWTError:
        raise HTTPException(status_code=307, detail='Login to proceed')
    
def is_authenticated_custom(token: str):
    return jwt.decode(token, _CUSTOM_SECRET_KEY, algorithms=[_ALGORITHM])