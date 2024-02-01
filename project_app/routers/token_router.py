from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from base_models.token_model import Token
from services.authorization_service import authenticate_admin, authenticate_user, create_access_token

token_router = APIRouter(prefix='/token')


@token_router.post('/', response_model=Token, tags=['token'])
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_admin(form_data.username, form_data.password)
    if not user:
        user = authenticate_user(form_data.username, form_data.password)

        if not user:
            raise HTTPException(status_code=401,
                                detail='Incorrect username or password.',
                                headers={'WWW-AUTHENTICATE': 'Bearer'})

    access_token = create_access_token(user)

    return {"access_token": access_token, "token_type": "bearer"}