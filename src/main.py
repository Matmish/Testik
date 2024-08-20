from fastapi import FastAPI
import uvicorn
from fastapi.routing import APIRouter
from sqlalchemy.sql.functions import user

from src.api.handlers.products_handlers import products_router

app = FastAPI(
    title="Shop"
)


main_app_router = APIRouter(prefix="/api/v1")

main_app_router.include_router(products_router)
app.include_router(main_app_router)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)