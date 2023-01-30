"""add content column to posts table

Revision ID: 8efcd3e4a55b
Revises: 02010072c5e0
Create Date: 2023-01-29 16:24:30.600265

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8efcd3e4a55b'
down_revision = '02010072c5e0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
