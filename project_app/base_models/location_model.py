from pydantic import BaseModel

class Location(BaseModel):

    location_id: int
    city: str
    country: str