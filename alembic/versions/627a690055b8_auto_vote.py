"""auto-vote

Revision ID: 627a690055b8
Revises: 80ef81710127
Create Date: 2023-07-07 10:57:41.423151

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '627a690055b8'
down_revision = '80ef81710127'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('votes',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('posts_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['posts_id'], ['posts.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('user_id', 'posts_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('votes')
    # ### end Alembic commands ###
