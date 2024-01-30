from pydantic import BaseModel

class Car(BaseModel):

    car_id: int
    brand: str
    model: str