from typing import Optional, List

from pydantic import BaseModel



class ProductRequestSchema(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None


class ProductResponseSchema(ProductRequestSchema):
    id: Optional[int] = None


class ProductsResponseSchema(BaseModel):
    products: Optional[List[ProductResponseSchema]] = None