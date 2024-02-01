from fastapi import FastAPI
from routers.car_router import car_router
from routers.token_router import token_router
from routers.user_router import user_router

app = FastAPI()
app.include_router(car_router)
app.include_router(token_router)
app.include_router(user_router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run('main:app', host="127.0.0.1", port=8000, reload=True)