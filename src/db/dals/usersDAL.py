from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.models.users import Users


class UsersDAL():
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_user(self, data):
        new_user = Users(
            name=data.name,
            surname=data.surname,
            birth_date=data.date_of_birth
        )
        self.db_session.add(new_user)
        await self.db_session.commit()
        await self.db_session.flush()


    async def get_all_users(self):
        query = (
            select(Users)
        )
        results = await self.db_session.execute(query)
        users = results.scalars().all()
        return users

    async def get_user_by_id(self, user_id):
        query = (
            select(Users)
            .where(Users.id == user_id)
        )
        result = await self.db_session.execute(query)
        return result.scalar_one_or_none()