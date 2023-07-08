"""add last few columns to posts table

Revision ID: 80ef81710127
Revises: ac54b8376391
Create Date: 2023-07-07 10:36:44.188194

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '80ef81710127'
down_revision = 'ac54b8376391'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass