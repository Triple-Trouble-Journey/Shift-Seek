from pydantic import BaseModel
from datetime import date

class InputCarAD(BaseModel):

    car_model: str
    location: str
    car_price: int
    date_manufacture: date
    engine_type: str
    horsepower: int
    cubic_capacity: int
    transmission: str
    car_type: str
    car_color: str
    car_mileage: int
    car_description: str

class CarAD_DB(BaseModel):

    author_id: int
    car_model_id: int
    location_id: int
    car_price: int
    date_manufacture: date
    engine_type: str
    horsepower: int
    cubic_capacity: int
    transmission: str
    car_type: str
    car_color: str
    car_mileage: int
    car_description: str

def object_generator_ad(author_id,car_id, location_id, input_ad_info):
    new_add_obj = CarAD_DB(
        author_id=author_id,
        car_model_id=car_id,
        location_id=location_id,
        car_price=input_ad_info.car_price,
        date_manufacture=input_ad_info.date_manufacture,
        engine_type=input_ad_info.engine_type,
        horsepower=input_ad_info.horsepower,
        cubic_capacity=input_ad_info.cubic_capacity,
        transmission=input_ad_info.transmission,
        car_type=input_ad_info.car_type,
        car_color=input_ad_info.car_color,
        car_mileage=input_ad_info.car_mileage,
        car_description=input_ad_info.car_description
    )
    return new_add_obj

def update_car_ad(ad_to_update, db, car_price, engine_type, horsepower, cubic_capacity, transmission, car_type, car_color, car_mileage, car_description):
    ad_to_update.car_price = car_price or ad_to_update.car_price
    ad_to_update.engine_type = engine_type or ad_to_update.engine_type
    ad_to_update.horsepower = horsepower or ad_to_update.horsepower
    ad_to_update.cubic_capacity = cubic_capacity or ad_to_update.cubic_capacity
    ad_to_update.transmission = transmission or ad_to_update.transmission
    ad_to_update.car_type = car_type or ad_to_update.car_type
    ad_to_update.car_color = car_color or ad_to_update.car_color
    ad_to_update.car_mileage = car_mileage or ad_to_update.car_mileage
    ad_to_update.car_description = car_description or ad_to_update.car_description
    db.commit()