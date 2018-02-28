"""empty message

Revision ID: be2e7dafed69
Revises: 
Create Date: 2018-02-28 01:55:04.374061

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'be2e7dafed69'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('instances',
    sa.Column('varnishIp', sa.Integer(), nullable=False),
    sa.Column('cpu', sa.String(length=120), nullable=True),
    sa.Column('status', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('varnishIp'),
    sa.UniqueConstraint('cpu')
    )
    op.add_column(u'users', sa.Column('password', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column(u'users', 'password')
    op.drop_table('instances')
    # ### end Alembic commands ###
