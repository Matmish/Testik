from sqlalchemy import BIGINT, Text, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.db.sessions import Base


class CartsProducts(Base):
    __tablename__ = 'carts_products'
    __table_args__ = {
        'comment': 'Relationship between cart and products',
    }

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True,nullable=False, autoincrement=True)
    product_id: Mapped[int] = mapped_column(BIGINT, ForeignKey('products.id'),
                                            nullable=False,comment='some some')
    cart_id: Mapped[int] = mapped_column(BIGINT, ForeignKey('carts.id'),
                                            nullable=False, comment='some some')