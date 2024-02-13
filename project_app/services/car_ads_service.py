from base_models.carad_model import object_generator_ad, update_car_ad
from fastapi import HTTPException
from config.db_engine import read_query, insert_query, read_query_all_results
from db_models.sqlalchemy_script import db_ads, db_users, db_cars, db_locations
from common.car_ad_return_info import return_info_ads


def create_ad(author_id,input_ad_info, db):

    car_brand_model = input_ad_info.car_model
    car = car_brand_model.split(' ') #['bmw', '320d']
    current_car_db_info = db.query(db_cars).filter(getattr(db_cars, 'brand') == car[0],
                                            getattr(db_cars, 'model') == car[1]
                                            ).first()
    
    #TODO: IF WILL THROW NONETYPE OBJECT TO EXCEPT IT AND TO WORK WITH SOME API.
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
    
    additional_info_ads = return_info_ads(all_ads, db)
    return additional_info_ads

def delete_ad(db, current_user, ad_id):

    ad_exist = read_query(db_ads, db, ad_id, 'ad_id')

    if not ad_exist:
        raise HTTPException(status_code=404, detail='AD not found!')
    
    check_ad_owner = db.query(db_ads).filter(getattr(db_ads, 'author_id') == current_user.user_id,
                                            getattr(db_ads, 'ad_id') == ad_id
                                            ).first()
    
    if not check_ad_owner:
        raise HTTPException(status_code=400, detail='Only the owner of this AD is permitted to remove it!')
    else:
        db.delete(check_ad_owner)
        db.commit()
        raise HTTPException(status_code=200, detail=f'You successfully deleted AD ID: {check_ad_owner.ad_id}')
    
    
def view_my_ads(db, current_user):

    all_ads = read_query_all_results(db_ads, db, current_user.user_id, 'author_id')

    if not all_ads:
        raise HTTPException(status_code=404, detail='No active ADS found!')
    
    additional_info_ads = return_info_ads(all_ads, db)
    return additional_info_ads