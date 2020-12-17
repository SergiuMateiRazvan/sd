"""Create Users Table

Revision ID: 280a5af04483
Revises: 
Create Date: 2020-12-16 21:14:52.980525

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "280a5af04483"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "users",
        sa.Column("mail", sa.String(), nullable=False),
        sa.Column("password", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("mail"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("users")
    # ### end Alembic commands ###