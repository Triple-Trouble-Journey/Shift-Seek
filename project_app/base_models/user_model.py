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