from sqlalchemy import BIGINT, Text, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.sessions import Base
from src.db.models.users import Users


class Carts(Base):
    __tablename__ = 'carts'
    __table_args__ = {
        'comment': 'Carts'
    }

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True, nullable=False, autoincrement=True)
    name: Mapped[str] = mapped_column(Text, nullable=True, comment='Name')
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=True, comment='User ID')

    cart_user = relationship(
        "Users",
        back_populates="user_cart"
    )
    cart_product = relationship(
        "Products",
        secondary="carts_products",
        back_populates="product_cart"
    )
