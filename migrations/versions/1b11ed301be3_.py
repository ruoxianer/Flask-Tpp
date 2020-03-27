"""empty message

Revision ID: 1b11ed301be3
Revises: af618a29c4d2
Create Date: 2020-03-13 21:12:14.101090

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1b11ed301be3'
down_revision = 'af618a29c4d2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('movies',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('showname', sa.String(length=128), nullable=True),
    sa.Column('shownameen', sa.String(length=128), nullable=True),
    sa.Column('director', sa.String(length=64), nullable=True),
    sa.Column('leadingRole', sa.String(length=256), nullable=True),
    sa.Column('type', sa.String(length=64), nullable=True),
    sa.Column('country', sa.String(length=64), nullable=True),
    sa.Column('lanuage', sa.String(length=64), nullable=True),
    sa.Column('duration', sa.Integer(), nullable=True),
    sa.Column('screen', sa.String(length=32), nullable=True),
    sa.Column('openday', sa.DateTime(), nullable=True),
    sa.Column('backgroundpicture', sa.String(length=256), nullable=True),
    sa.Column('flag', sa.Boolean(), nullable=True),
    sa.Column('is_delete', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('movies')
    # ### end Alembic commands ###