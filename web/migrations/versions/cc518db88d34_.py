"""empty message

Revision ID: cc518db88d34
Revises: ad91e9f8e877
Create Date: 2018-03-11 19:51:49.878215

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cc518db88d34'
down_revision = 'ad91e9f8e877'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('originip', sa.String(length=120), nullable=True))
    op.add_column('users', sa.Column('password', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password')
    op.drop_column('users', 'originip')
    # ### end Alembic commands ###
