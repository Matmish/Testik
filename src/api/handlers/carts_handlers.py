from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.schemas.carts_schemas import CartRequestSchema, CartsResponseSchema
from src.api.schemas.user_schemas import UserRequestSchema, UserResponseSchema, UsersResponseSchema
from src.db.sessions import get_db
from src.services.carts_service import _create_cart, _get_all_carts
from src.services.user_services import _create_user, _get_all_users, _get_user_by_id

carts_router = APIRouter(
    prefix="/cart",
)


@carts_router.post('', )
async def create_cart(
        body: CartRequestSchema,
        session: AsyncSession = Depends(get_db)
):
    await _create_cart(body, session)


@carts_router.get('', response_model= CartsResponseSchema)
async def get_all_carts(
        session: AsyncSession = Depends(get_db)
):
    return await _get_all_carts(session)
