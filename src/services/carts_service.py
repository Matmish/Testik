from src.api.schemas.carts_schemas import CartsResponseSchema, CartResponseSchema
from src.api.schemas.products_schemas import ProductResponseSchema
from src.api.schemas.user_schemas import UserResponseSchema
from src.db.dals.cartsDAL import CartsDAL


async def _create_cart(data, session):
    carts_dal = CartsDAL(session)
    await carts_dal.create_cart(data)


async def _add_product_to_cart(data, session):
    carts_dal = CartsDAL(session)
    if data.products_ids:
        for product_id in data.products_ids:
           await carts_dal.add_product(data.cart_id, product_id)


async def _get_all_carts(session):
    carts_dal = CartsDAL(session)
    carts_data = await carts_dal.get_all_carts()
    if carts_data:
        carts = []
        for cart in carts_data:
            user = UserResponseSchema(
                id=cart.cart_user.id,
                name=cart.cart_user.name,
                surname=cart.cart_user.surname,
                date_of_birth=cart.cart_user.birth_date,
            )
            products = []
            if cart.cart_product:
                for product in cart.cart_product:
                    products.append(
                        ProductResponseSchema(
                            id=product.id,
                            name=product.name,
                            price=product.price,
                        )
                    )
            carts.append(
                CartResponseSchema(
                    id=cart.id,
                    name=cart.name,
                    products=products,
                    user=user,
                )
            )
        return CartsResponseSchema(carts=carts)
