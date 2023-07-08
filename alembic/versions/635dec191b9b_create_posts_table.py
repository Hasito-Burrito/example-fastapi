"""create posts table

Revision ID: 635dec191b9b
Revises: 
Create Date: 2023-07-06 10:56:10.531430

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '635dec191b9b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
