from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.schemas.user_schemas import UserRequestSchema, UserResponseSchema, UsersResponseSchema
from src.db.sessions import get_db
from src.services.user_services import _create_user, _get_all_users, _get_user_by_id

products_router = APIRouter(
    prefix="/product",
)


@products_router.post('', )
async def create_user(
        body: UserRequestSchema,
        session: AsyncSession() = Depends(get_db)
):
    await _create_user(body, session)


@products_router.get('', response_model= UsersResponseSchema)
async def get_all_users(
        session: AsyncSession() = Depends(get_db)
):
    return await _get_all_users(session)


@products_router.get('/{user_id}', response_model= UserResponseSchema)
async def get_user_by_id(
        user_id: int,
        session: AsyncSession() = Depends(get_db)
):
    return await _get_user_by_id(user_id, session)