from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.schemas.products_schemas import ProductUpdateSchema
from src.db.models.products import Products


class ProductsDAL:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_products(self, data):
        new_products = Products(
            name=data.name,
            price=data.price
        )
        self.db_session.add(new_products)
        await self.db_session.commit()
        await self.db_session.flush()

    async def update_product(self, product: Products, data: ProductUpdateSchema):
        if data.name is not None:
            product.name = data.name
        if data.description is not None:
            product.description = data.description
        if data.price is not None:
            product.price = data.price
        if data.in_stock is not None:
            product.in_stock = data.in_stock
        self.session.add(product)
        await self.session.commit()
        return product

    # async def update_product(self, data, product_id):
    #     update_product = Products(
    #         id=data.id,
    #         name=data.name,
    #         price=data.price
    #     )
    #     if update_product.id == product_id:
    #         if update_product.name:
    #             update_product.name = data.name
    #         if update_product.price:
    #             update_product.price = data.price

    #     await self.db_session.commit()
    #     return update_product



    async def get_all_products(self):
        query = (
            select(Products)
        )
        results = await self.db_session.execute(query)
        products = results.scalars().all()
        return products

    async def get_product_by_id(self, product_id):
        query = (
            select(Products)
            .where(Products.id == product_id)
        )
        result = await self.db_session.execute(query)
        return result.scalar_one_or_none()
