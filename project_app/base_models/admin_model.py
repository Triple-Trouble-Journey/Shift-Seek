from typing import Optional
from pydantic import BaseModel, EmailStr

class Admin(BaseModel):
    admin_id: Optional[int] = None
    group: str = 'admins'
    username: str
    password: str
    email: EmailStr
    first_name: str
    last_name: str
    address: str
    telephone: int
    profile_picture: Optional[str] = None