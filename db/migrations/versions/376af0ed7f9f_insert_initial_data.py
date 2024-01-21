"""insert initial data

Revision ID: 376af0ed7f9f
Revises: 7cfbf1ece3e7
Create Date: 2024-01-21 12:35:08.630211

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '376af0ed7f9f'
down_revision = '7cfbf1ece3e7'
branch_labels = None
depends_on = None


def upgrade():
	with open("376af0ed7f9f_upgrades.sql") as file_:
		for statement in file_.read().split(";\n"):  # or however we want to split
		    op.execute(statement)


def downgrade():
	with open("376af0ed7f9f_downgrades.sql") as file_:
		for statement in file_.read().split(";\n"):  # or however we want to split
		    op.execute(statement)
