import datetime
from typing import Optional, List

from pydantic import BaseModel


class UserRequestSchema(BaseModel):
    name: Optional[str] = None
    surname: Optional[str] = None
    date_of_birth: Optional[datetime.date]= None


class UserResponseSchema(UserRequestSchema):
    id: Optional[int] = None


class UsersResponseSchema(BaseModel):
    users: Optional[List[UserResponseSchema]] = None
