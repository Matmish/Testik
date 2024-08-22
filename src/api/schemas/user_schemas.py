from typing import Optional, List

from pydantic import BaseModel



class UserRequestSchema(BaseModel):
    name: Optional[str] = None
    surname: Optional[str] = None
    date_of_birth: Optional[str] = None

class UserResponseSchema(UserRequestSchema):
    id: Optional[int] = None


class UsersResponseSchema(BaseModel):
    products: Optional[List[UserResponseSchema]] = None