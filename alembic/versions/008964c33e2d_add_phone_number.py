"""add phone number

Revision ID: 008964c33e2d
Revises: a14abadd7a65
Create Date: 2023-01-30 17:12:57.161132

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '008964c33e2d'
down_revision = 'a14abadd7a65'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'phone_number')
    # ### end Alembic commands ###
