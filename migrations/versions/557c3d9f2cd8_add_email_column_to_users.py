"""add email column to users

Revision ID: 557c3d9f2cd8
Revises: 06766e4ed307
Create Date: 2021-04-21 05:15:40.037738

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '557c3d9f2cd8'
down_revision = '06766e4ed307'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.String(length=255), nullable=True))
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_column('users', 'email')
    # ### end Alembic commands ###
