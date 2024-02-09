from base_models.carad_model import object_generator_ad, update_car_ad
from fastapi import HTTPException
from config.db_engine import read_query, insert_query
from db_models.sqlalchemy_script import db_ads, db_users, db_cars, db_locations


def create_ad(author_id,input_ad_info, db):

    car_brand_model = input_ad_info.car_model
    car = car_brand_model.split(' ') #['bmw', '320d']
    current_car_db_info = db.query(db_cars).filter(getattr(db_cars, 'brand') == car[0],
                                            getattr(db_cars, 'model') == car[1]
                                            ).first()
    car_id = current_car_db_info.car_id
    location = input_ad_info.location
    location_info_db = read_query(db_locations, db, location, 'city')
    location_id = location_info_db.location_id

    db_object = object_generator_ad(author_id, car_id, location_id, input_ad_info)
    
    insert_query(db_ads, db, db_object)
    raise HTTPException(status_code=201, detail='Successfully created new Car AD!')


def edit_ad(ad_id, author_id, car_price,engine_type, horsepower, cubic_capacity,
             transmission, car_type, car_color, car_mileage, car_description, db):

    ad_to_update = db.query(db_ads).filter(
        getattr(db_ads, 'ad_id') == ad_id,
        getattr(db_ads, 'author_id') == author_id    
    ).first()
    
    if ad_to_update:
        update_car_ad(ad_to_update, db, car_price, engine_type, horsepower,
                      cubic_capacity, transmission, car_type, car_color, car_mileage, car_description)
        
        raise HTTPException(status_code=200, detail='You updated your AD!')
    else:
        raise HTTPException(status_code=404, detail='AD not found!')
    

def view_ads(db):
    all_ads = db.query(db_ads).all()
    
    for ad in all_ads:
        users = read_query(db_users,db, ad.author_id, 'user_id')
        cars = read_query(db_cars, db, ad.car_model_id, 'car_id')
        locations = read_query(db_locations,db,  ad.location_id, 'location_id')
        ad.author_id = users.username
        ad.car_model_id = f'{cars.brand} {cars.model}'
        ad.location_id = locations.city
    return all_ads