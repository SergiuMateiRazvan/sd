"""Add more user details

Revision ID: 79838f5eae50
Revises: 408a8b98a25d
Create Date: 2021-01-09 12:40:43.194728

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "79838f5eae50"
down_revision = "408a8b98a25d"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("user_details", sa.Column("description", sa.String(), nullable=True))
    op.add_column("user_details", sa.Column("name", sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("user_details", "name")
    op.drop_column("user_details", "description")
    # ### end Alembic commands ###
