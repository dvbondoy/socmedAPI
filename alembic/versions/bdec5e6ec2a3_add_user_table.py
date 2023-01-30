"""add user table

Revision ID: bdec5e6ec2a3
Revises: 8efcd3e4a55b
Create Date: 2023-01-29 16:30:01.471304

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bdec5e6ec2a3'
down_revision = '8efcd3e4a55b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users', 
    sa.Column('id',sa.Integer(),nullable=False),
    sa.Column('email', sa.String(),nullable=False),
    sa.Column('password',sa.String(),nullable=False),
    sa.Column('created_at',sa.TIMESTAMP(timezone=True),server_default=sa.text('now()'),nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
