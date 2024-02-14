from pydantic import BaseModel, EmailStr
from typing import Optional

class User(BaseModel):
    username: str
    password: str
    email: EmailStr
    first_name: str
    last_name: str
    address: str
    telephone: int
    profile_picture: Optional[str] = None
    is_company: bool

class UserRegiser(BaseModel):
    username: str
    password: str
    email: EmailStr
    first_name: str
    last_name: str
    address: str
    telephone: str


def object_generator_user(user_info):

    db_object = User(username=user_info.username,
                     password=user_info.password,
                     email=user_info.email,
                     first_name=user_info.first_name,
                     last_name=user_info.last_name,
                     address=user_info.address,
                     telephone=user_info.telephone,
                     is_company=False)
    
    return db_object