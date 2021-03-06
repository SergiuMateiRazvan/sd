"""

Revision ID: 88bead6966d0
Revises: 0ea564192726
Create Date: 2020-12-17 11:53:40.214046

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "88bead6966d0"
down_revision = "0ea564192726"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "user_details",
        sa.Column("user_mail", sa.String(), nullable=False),
        sa.Column("phone", sa.String(), nullable=True),
        sa.Column("education", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.ForeignKeyConstraint(
            ["user_mail"],
            ["users.mail"],
        ),
        sa.PrimaryKeyConstraint("user_mail"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("user_details")
    # ### end Alembic commands ###
