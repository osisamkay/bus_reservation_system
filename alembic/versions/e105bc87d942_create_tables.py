"""Create tables

Revision ID: e105bc87d942
Revises: 6ba5fe2fd37e
Create Date: 2024-03-31 23:35:40.239568

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e105bc87d942'
down_revision: Union[str, None] = '6ba5fe2fd37e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('buses', 'id',
               existing_type=sa.NUMERIC(),
               type_=sa.UUID(),
               existing_nullable=False)
    op.alter_column('prices', 'id',
               existing_type=sa.NUMERIC(),
               type_=sa.UUID(),
               existing_nullable=False)
    op.alter_column('prices', 'route_id',
               existing_type=sa.NUMERIC(),
               type_=sa.UUID(),
               existing_nullable=True)
    op.alter_column('reservations', 'id',
               existing_type=sa.NUMERIC(),
               type_=sa.UUID(),
               existing_nullable=False)
    op.alter_column('reservations', 'user_id',
               existing_type=sa.NUMERIC(),
               type_=sa.UUID(),
               existing_nullable=True)
    op.alter_column('reservations', 'bus_id',
               existing_type=sa.NUMERIC(),
               type_=sa.UUID(),
               existing_nullable=True)
    op.alter_column('routes', 'id',
               existing_type=sa.NUMERIC(),
               type_=sa.UUID(),
               existing_nullable=False)
    op.alter_column('users', 'id',
               existing_type=sa.NUMERIC(),
               type_=sa.UUID(),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'id',
               existing_type=sa.UUID(),
               type_=sa.NUMERIC(),
               existing_nullable=False)
    op.alter_column('routes', 'id',
               existing_type=sa.UUID(),
               type_=sa.NUMERIC(),
               existing_nullable=False)
    op.alter_column('reservations', 'bus_id',
               existing_type=sa.UUID(),
               type_=sa.NUMERIC(),
               existing_nullable=True)
    op.alter_column('reservations', 'user_id',
               existing_type=sa.UUID(),
               type_=sa.NUMERIC(),
               existing_nullable=True)
    op.alter_column('reservations', 'id',
               existing_type=sa.UUID(),
               type_=sa.NUMERIC(),
               existing_nullable=False)
    op.alter_column('prices', 'route_id',
               existing_type=sa.UUID(),
               type_=sa.NUMERIC(),
               existing_nullable=True)
    op.alter_column('prices', 'id',
               existing_type=sa.UUID(),
               type_=sa.NUMERIC(),
               existing_nullable=False)
    op.alter_column('buses', 'id',
               existing_type=sa.UUID(),
               type_=sa.NUMERIC(),
               existing_nullable=False)
    # ### end Alembic commands ###