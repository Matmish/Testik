from src.api.schemas.user_schemas import UserResponseSchema, UsersResponseSchema
from src.db.dals.usersDAL import UsersDAL


async def _create_user(data, session):
    users_dal = UsersDAL(session)
    await users_dal.create_user(data)

async def _get_all_users(session):
    users_dal = UsersDAL(session)
    users= await users_dal.get_all_users()
    if users:
        users_result = []
        for user in users:
            users_result.append(
                UsersResponseSchema(
                    id=user.id,
                    name=user.name,
                    date_of_birth=user.date_of_birth,
                )
            )
        return UserResponseSchema(products= users_result)
async def _get_user_by_id(user_id, session):
    users_dal = UsersDAL(session)
    user = await users_dal.get_user_by_id(user_id)
    return ProductResponseSchema(
                    id=user.id,
                    name=user.name,
                    price=user.price,
    )