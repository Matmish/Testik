from sqlalchemy import BIGINT, Text, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.sessions import Base


class Carts(Base):
    __tablename__ = 'carts'
    __table_args__ = {
        'comment': 'Carts'
    }

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True,nullable=False, autoincrement=True)
    name: Mapped[str] = mapped_column(Text, nullable=True, comment='Name')

    cart_product = relationship(
        "Products",
        secondary="cart_product",
        back_populates="product_cart"
    )