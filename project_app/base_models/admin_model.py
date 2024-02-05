from pydantic import BaseModel


class Admin(BaseModel):

    admin_id: int
    users_id: int