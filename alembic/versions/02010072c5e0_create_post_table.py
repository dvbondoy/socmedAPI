"""create post table

Revision ID: 02010072c5e0
Revises: 
Create Date: 2023-01-29 16:13:59.701988

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '02010072c5e0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', 
        sa.Column('id',sa.Integer(), nullable=False,primary_key=True),
        sa.Column('title',sa.String(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
