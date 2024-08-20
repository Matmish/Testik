from sqlalchemy import BIGINT, Text, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.sessions import Base
from src.db.models.carts import Carts
from src.db.models.carts_products import CartsProducts


class Products(Base):
    __tablename__ = 'products'
    __table_args__ = {
        'comment': 'Products'
    }

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True,nullable=False, autoincrement=True)
    name: Mapped[str] = mapped_column(Text, nullable=True, comment='Product Name')
    price: Mapped[float] = mapped_column(Float, nullable=True, comment='Price')

    product_cart = relationship(
        "Carts",
        secondary="cart_product",
        back_populates="cart_product"
    )