from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.schemas.products_schemas import ProductRequestSchema, ProductsResponseSchema, ProductResponseSchema, \
    ProductUpdateSchema
from src.db.sessions import get_db
from src.services.products_services import _create_product, _get_all_products, _get_product_by_id, _update_product

products_router = APIRouter(
    prefix="/product",
)


@products_router.post('', )
async def create_product(
        body: ProductRequestSchema,
        session: AsyncSession = Depends(get_db)
):
    await _create_product(body, session)


@products_router.get('', response_model=ProductsResponseSchema)
async def get_all_products(
        session: AsyncSession = Depends(get_db)
):
    return await _get_all_products(session)


@products_router.get('/{product_id}', response_model=ProductResponseSchema)
async def get_product_by_id(
        product_id: int,
        session: AsyncSession = Depends(get_db)
):
    return await _get_product_by_id(product_id, session)


# @products_router.put('/updateProduct/{product_id}')
# async def update_product(
#         product_id: int,
#         body: ProductResponseSchema,
#         session: AsyncSession = Depends(get_db)
# ):
#     await _update_product(product_id, body, session)


@products_router.put('/products/{product_id}', response_model=ProductResponseSchema)
async def update_product(
        product_id: int,
        session: AsyncSession = Depends(get_db)

):
    return await _update_product(product_id, session)

# @products_router.delete('/{product_id}')
# async def delete_product( course_id: int = Path(description="Course ID"),
#         body: ProductResponseSchema,
#         session: AsyncSession = Depends(get_db)
# ):
#     await _delete_product(body, session)
