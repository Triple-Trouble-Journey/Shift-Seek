from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi import Depends
from sqlalchemy.ext.declarative import declarative_base
from db_details import password, username, host
from typing import Annotated
from sqlalchemy.orm import Session


DATABASE_URL = f'mysql+pymysql://{username}:{password}@{host}/shift_seek'

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]


def insert_query(model, db, object):

    db_car = model(**object.dict())
    db.add(db_car)
    db.commit()

#ONLY ONE RESULT car: {audi a5}
def read_query(model, db, param, property):

    result  = db.query(model).filter(getattr(model, property) == param).first()
    if result:
        return result
    else:
        return None

#ALL RESULTS FOR THE PARAM example: cars: {audi a5, audi a6, audi a8}
def read_query_all_results(model, db, param, property):

    result  = db.query(model).filter(getattr(model, property) == param).all()
    if result:
        return result
    else:
        return None