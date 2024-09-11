from typing import Optional, List

from pydantic import BaseModel

from src.api.schemas.products_schemas import ProductResponseSchema
from src.api.schemas.user_schemas import UserResponseSchema


class CartRequestSchema(BaseModel):
    name: Optional[str] = None
    user: Optional[UserResponseSchema] = None


class CartResponseSchema(CartRequestSchema):
    id: Optional[int] = None
    products: Optional[List[ProductResponseSchema]] = None


class CartsResponseSchema(BaseModel):
    carts: Optional[List[CartResponseSchema]] = None


class AddToCartRequestSchema(BaseModel):
    products_ids: Optional[List[int]] = None
    cart_id: Optional[int] = None





