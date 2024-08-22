"""3

Revision ID: 1b0ac6e6404f
Revises: 61b8b68fd8d5
Create Date: 2024-08-22 20:20:43.506839

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1b0ac6e6404f'
down_revision: Union[str, None] = '61b8b68fd8d5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('name', sa.Text(), nullable=True, comment='Name'),
    sa.Column('surname', sa.Text(), nullable=True, comment='SurName'),
    sa.Column('birth_date', sa.Date(), nullable=True, comment='Date of birth'),
    sa.PrimaryKeyConstraint('id'),
    comment='Users'
    )
    op.add_column('carts', sa.Column('user_id', sa.BIGINT(), nullable=True, comment='User ID'))
    op.create_foreign_key(None, 'carts', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'carts', type_='foreignkey')
    op.drop_column('carts', 'user_id')
    op.drop_table('users')
    # ### end Alembic commands ###
