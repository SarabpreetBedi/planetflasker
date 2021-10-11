"""added password field

Revision ID: 6095914ee3c9
Revises: 23d4b2b6d9ad
Create Date: 2021-10-07 20:05:53.347340

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6095914ee3c9'
down_revision = '23d4b2b6d9ad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_hash', sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password_hash')
    # ### end Alembic commands ###
