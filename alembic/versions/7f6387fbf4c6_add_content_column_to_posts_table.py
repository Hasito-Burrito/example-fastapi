"""add content column to posts table

Revision ID: 7f6387fbf4c6
Revises: 635dec191b9b
Create Date: 2023-07-06 12:12:33.143225

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7f6387fbf4c6'
down_revision = '635dec191b9b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
