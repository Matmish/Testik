import uvicorn
from fastapi import FastAPI
from fastapi.routing import APIRouter

from src.api.handlers.carts_handlers import carts_router
from src.api.handlers.products_handlers import products_router
from src.api.handlers.user_handlers import users_router

app = FastAPI(
    title="Shop"
)

main_app_router = APIRouter(prefix="/api/v1")

main_app_router.include_router(products_router, tags=["Products"])
main_app_router.include_router(users_router, tags=["Users"])
main_app_router.include_router(carts_router, tags=["Carts"])
app.include_router(main_app_router)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
