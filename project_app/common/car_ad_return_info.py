from config.db_engine import read_query
from db_models.sqlalchemy_script import db_users, db_cars, db_locations

def return_info_ads(all_ads, db):

    for ad in all_ads:
        users = read_query(db_users,db, ad.author_id, 'user_id')
        cars = read_query(db_cars, db, ad.car_model_id, 'car_id')
        locations = read_query(db_locations,db,  ad.location_id, 'location_id')
        ad.author_id = users.username
        ad.car_model_id = f'{cars.brand} {cars.model}'
        ad.location_id = locations.city
    return all_ads