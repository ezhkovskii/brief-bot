"""message

Revision ID: 970d346b0b3b
Revises: 3bd2455d1aa0
Create Date: 2024-05-05 21:23:58.386100

Doc: https://alembic.sqlalchemy.org/en/latest/tutorial.html#create-a-migration-script
"""
from alembic import op
import sqlalchemy as sa


revision = '970d346b0b3b'
down_revision = '3bd2455d1aa0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('id', sa.Integer(), nullable=False))
    op.drop_column('messages', 'message_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('message_id', sa.INTEGER(), autoincrement=True, nullable=False))
    op.drop_column('messages', 'id')
    # ### end Alembic commands ###
