"""empty message

Revision ID: 4795d662de44
Revises: 6f22f9870549
Create Date: 2025-05-28 10:14:23.757769

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4795d662de44'
down_revision = '6f22f9870549'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('t_users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('updated_at', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('t_users', schema=None) as batch_op:
        batch_op.drop_column('updated_at')
        batch_op.drop_column('created_at')

    # ### end Alembic commands ###
