from src.api.schemas.products_schemas import ProductResponseSchema, ProductsResponseSchema
from src.db.dals.productsDAL import ProductsDAL


async def _create_product(data, session):
    products_dal = ProductsDAL(session)
    await products_dal.create_products(data)

async def _get_all_products(session):
    products_dal = ProductsDAL(session)
    products= await products_dal.get_all_products()
    if products:
        products_result = []
        for product in products:
            products_result.append(
                ProductResponseSchema(
                    id=product.id,
                    name=product.name,
                    price=product.price,
                )
            )
        return ProductsResponseSchema(products= products_result)
async def _get_product_by_id(proauct_id, session):
    products_dal = ProductsDAL(session)
    product = await products_dal.get_product_by_id(proauct_id)
    return ProductResponseSchema(
                    id=product.id,
                    name=product.name,
                    price=product.price,
    )