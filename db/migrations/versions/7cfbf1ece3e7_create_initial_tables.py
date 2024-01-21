"""create initial tables

Revision ID: 7cfbf1ece3e7
Revises: 
Create Date: 2024-01-21 12:02:19.435666

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7cfbf1ece3e7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
	with open("7cfbf1ece3e7_upgrades.sql") as file_:
		for statement in file_.read().split(";\n"):  # or however we want to split
		    op.execute(statement)


def downgrade():
	with open("7cfbf1ece3e7_downgrades.sql") as file_:
		for statement in file_.read().split(";\n"):  # or however we want to split
		    op.execute(statement)
