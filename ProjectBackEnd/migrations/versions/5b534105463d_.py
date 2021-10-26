"""empty message

Revision ID: 5b534105463d
Revises: 5729f8d9c785
Create Date: 2021-10-25 23:54:07.186293

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5b534105463d'
down_revision = '5729f8d9c785'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('home', 'image',
               existing_type=sa.VARCHAR(length=20),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('home', 'image',
               existing_type=sa.VARCHAR(length=20),
               nullable=True)
    # ### end Alembic commands ###