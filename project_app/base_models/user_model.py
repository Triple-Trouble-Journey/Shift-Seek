from pydantic import BaseModel, EmailStr
from typing import Optional

class User(BaseModel):
    group: str = 'users'
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
    telephone: int
    profile_picture: Optional[str] = None
    is_company: bool

def update_user_info(user_to_update, db, first_name, last_name, address, telephone):
    user_to_update.first_name = first_name or user_to_update.first_name
    user_to_update.last_name = last_name or user_to_update.last_name
    user_to_update.address = address or user_to_update.address
    user_to_update.telephone = telephone or user_to_update.telephone
    db.commit()