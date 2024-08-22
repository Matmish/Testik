import datetime
from sqlite3 import Date

from sqlalchemy import BIGINT, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.models.carts import Carts
from src.db.sessions import Base


class Users(Base):
    __tablename__ = 'users'
    __table_args__ = {
        'comment': 'Users'
    }

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True, nullable=False, autoincrement=True)
    name: Mapped[str] = mapped_column(Text, nullable=True, comment='Name')
    surname: Mapped[str] = mapped_column(Text, nullable=True, comment='SurName')
    birth_date = Mapped[datetime] = mapped_column(Date, nullable=True, comment='Date of birth')
    user_cart: Mapped["Carts"] = relationship(back_populates="users")
