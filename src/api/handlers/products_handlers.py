from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.schemas.products_schemas import ProductRequestSchema, ProductsResponseSchema, ProductResponseSchema
from src.db.sessions import get_db
from src.services.products_services import _create_product, _get_all_products, _get_product_by_id

products_router = APIRouter(
    prefix="/product",
)


@products_router.post('', )
async def create_product(
        body: ProductRequestSchema,
        session: AsyncSession() = Depends(get_db)
):
    await _create_product(body, session)


@products_router.get('', response_model= ProductsResponseSchema)
async def get_all_products(
        session: AsyncSession() = Depends(get_db)
):
    return await _get_all_products(session)


@products_router.get('/{product_id}', response_model= ProductResponseSchema)
async def get_product_by_id(
        product_id: int,
        session: AsyncSession() = Depends(get_db)
):
    return await _get_product_by_id(product_id, session)