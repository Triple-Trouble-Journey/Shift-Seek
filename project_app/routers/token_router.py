from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from config.db_engine import engine, db_dependency
from db_models import sqlalchemy_script

from base_models.token_model import Token
from services.authorization_service import authenticate_user, create_access_token

token_router = APIRouter(prefix='/token')
sqlalchemy_script.Base.metadata.create_all(bind=engine)


@token_router.post('/', response_model=Token, tags=['token'])
async def login_for_access_token(db: db_dependency,form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password, db)

    if not user:
        raise HTTPException(status_code=401,
                            detail='Incorrect username or password.',
                            headers={'WWW-AUTHENTICATE': 'Bearer'})

    access_token = create_access_token(user)

    return {"access_token": access_token, "token_type": "bearer"}