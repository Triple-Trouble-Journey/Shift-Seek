from sqlalchemy import Column, Integer, String, ForeignKey, Date, DateTime, Text, Float, Boolean, LargeBinary
from sqlalchemy.orm import relationship
from config.db_engine import Base

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    address = Column(String(50), nullable=False)
    telephone = Column(String(50), nullable=False)
    profile_picture = Column(LargeBinary, nullable=True)
    is_company = Column(Boolean, nullable=False)

class Car(Base):
    __tablename__ = 'cars'

    car_id = Column(Integer, primary_key=True, autoincrement=True)
    brand = Column(String(100), nullable=False)
    model = Column(String(100), nullable=False)

class Location(Base):
    __tablename__ = 'locations'

    location_id = Column(Integer, primary_key=True, autoincrement=True)
    city = Column(String(50), nullable=False)
    country = Column(String(50), nullable=False)

class CarAd(Base):
    __tablename__ = 'car_ads'

    ad_id = Column(Integer, primary_key=True, autoincrement=True)
    author_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    car_model_id = Column(Integer, ForeignKey('cars.car_id'), nullable=False)
    location_id = Column(Integer, ForeignKey('locations.location_id'), nullable=False)
    car_price = Column(Integer, nullable=False)
    date_manufacture = Column(Date, nullable=False)
    engine_type = Column(String(80), nullable=False)
    horsepower = Column(Integer, nullable=False)
    cubic_capacity = Column(Integer, nullable=False)
    transmission = Column(String(100), nullable=False)
    car_type = Column(String(100), nullable=False)
    car_color = Column(String(50), nullable=False)
    car_mileage = Column(Integer, nullable=False)
    car_description = Column(Text, nullable=False)

    location = relationship('Location')
    car_model = relationship('Car')
    author = relationship('User')

class Admin(Base):
    __tablename__ = 'admins'

    admin_id = Column(Integer, primary_key=True, autoincrement=True)
    users_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)

    user = relationship('User')

class ArchivedAd(Base):
    __tablename__ = 'archived_ads'

    archive_id = Column(Integer, primary_key=True, autoincrement=True)
    ad_id = Column(Integer, ForeignKey('car_ads.ad_id'), nullable=False)

    car_ad = relationship('CarAd')

class Topic(Base):
    __tablename__ = 'topics'

    topic_id = Column(Integer, primary_key=True, autoincrement=True)
    author_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    topic_title = Column(String(80), nullable=False)
    date_creation = Column(DateTime, nullable=False)
    topic_description = Column(Text, nullable=False)
    topic_likes = Column(Integer, nullable=True)

    author = relationship('User')

class Conversation(Base):
    __tablename__ = 'conversations'

    conversation_id = Column(Integer, primary_key=True, autoincrement=True)
    owner_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    conversation_title = Column(String(50), nullable=False)
    conversation_theme = Column(String(50), nullable=True)

    owner = relationship('User')

class Reply(Base):
    __tablename__ = 'replies'

    reply_id = Column(Integer, primary_key=True, autoincrement=True)
    author_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    topic_id = Column(Integer, ForeignKey('topics.topic_id'), nullable=False)
    reply_text = Column(Text, nullable=False)

    author = relationship('User')
    topic = relationship('Topic')

class Message(Base):
    __tablename__ = 'messages'

    message_id = Column(Integer, primary_key=True, autoincrement=True)
    author_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    message_text = Column(Text, nullable=False)

    author = relationship('User')

# Testing script
    
    # class User(Base):
    # __tablename__ = 'users'

    # user_id = Column(Integer, primary_key=True, autoincrement=True)
    # username = Column(String(50), unique=True, nullable=False)
    # password = Column(String(100), nullable=False)
    # email = Column(String(100), unique=True, nullable=False)
    # first_name = Column(String(50), nullable=False)
    # last_name = Column(String(50), nullable=False)
    # address = Column(String(50), nullable=False)
    # telephone = Column(String(50), nullable=False)
    # profile_picture = Column(LargeBinary, nullable=True)
    # is_company = Column(Boolean, nullable=False)class User(Base):
    # __tablename__ = 'users'

    # user_id = Column(Integer, primary_key=True, autoincrement=True)
    # username = Column(String(50), unique=True, nullable=False)
    # password = Column(String(100), nullable=False)
    # email = Column(String(100), unique=True, nullable=False)
    # first_name = Column(String(50), nullable=False)
    # last_name = Column(String(50), nullable=False)
    # address = Column(String(50), nullable=False)
    # telephone = Column(String(50), nullable=False)
    # profile_picture = Column(LargeBinary, nullable=True)
    # is_company = Column(Boolean, nullable=False)

    
db_user_info = User