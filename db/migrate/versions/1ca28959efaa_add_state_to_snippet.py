"""add state to Snippet

Revision ID: 1ca28959efaa
Revises: e4fcd92bbfdb
Create Date: 2018-07-07 20:42:58.219000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1ca28959efaa'
down_revision = 'e4fcd92bbfdb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('snippet', sa.Column('state', sa.String(length=32), nullable=False, server_default='open'))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('snippet', 'state')
    # ### end Alembic commands ###
