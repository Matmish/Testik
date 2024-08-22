from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload, selectinload

from src.db.models.carts import Carts
from src.db.models.products import Products
from src.db.models.users import Users


class CartsDAL:

    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_cart(self, data):
        new_cart = Carts(
            name=data.name,
            user_id=data.user.id
        )
        self.db_session.add(new_cart)
        await self.db_session.commit()
        await self.db_session.flush()

    async def get_all_carts(self):
        query = (
            select(Carts)
            .options(
                joinedload(Carts.cart_user),
                selectinload(Carts.cart_product)
            )
        )
        results = await self.db_session.execute(query)
        carts = results.scalars().all()
        return carts
