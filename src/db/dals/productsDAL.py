from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.models.products import Products


class ProductsDAL():
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