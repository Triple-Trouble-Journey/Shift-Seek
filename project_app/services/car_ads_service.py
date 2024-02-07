from base_models.carad_model import object_generator_ad, update_car_ad
from fastapi import HTTPException
from config.db_engine import read_query, insert_query
from db_models import sqlalchemy_script


def create_ad(author_id,input_ad_info, db):
    db_model_car = sqlalchemy_script.Car

    car_brand_model = input_ad_info.car_model
    car = car_brand_model.split(' ') #['bmw', '320d']
    current_car_db_info = db.query(db_model_car).filter(getattr(db_model_car, 'brand') == car[0],
                                            getattr(db_model_car, 'model') == car[1]
                                            ).first()
    car_id = current_car_db_info.car_id
    location = input_ad_info.location
    location_info_db = read_query(sqlalchemy_script.Location, db, location, 'city')
    location_id = location_info_db.location_id

    db_object = object_generator_ad(author_id, car_id, location_id, input_ad_info)
    
    insert_query(sqlalchemy_script.CarAd, db, db_object)
    raise HTTPException(status_code=201, detail='Successfully created new Car AD!')


def edit_ad(ad_id, author_id, car_price,engine_type, horsepower, cubic_capacity,
             transmission, car_type, car_color, car_mileage, car_description, db):
    
    db_model_ad = sqlalchemy_script.CarAd

    ad_to_update = db.query(db_model_ad).filter(
        getattr(db_model_ad, 'ad_id') == ad_id,
        getattr(db_model_ad, 'author_id') == author_id    
    ).first()
    
    if ad_to_update:
        update_car_ad(ad_to_update, db, car_price, engine_type, horsepower,
                      cubic_capacity, transmission, car_type, car_color, car_mileage, car_description)
        
        raise HTTPException(status_code=200, detail='You updated your AD!')
    else:
        raise HTTPException(status_code=404, detail='AD not found!')