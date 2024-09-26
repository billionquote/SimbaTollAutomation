"""empty message

Revision ID: 39a888a04ecf
Revises: abbf0a51b153
Create Date: 2024-05-02 20:41:45.675222

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '39a888a04ecf'
down_revision = 'abbf0a51b153'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('summary', schema=None) as batch_op:
        batch_op.alter_column('pickup_date_time',
               existing_type=postgresql.TIMESTAMP(),
               type_=sa.String(),
               existing_nullable=True)
        batch_op.alter_column('dropoff_date_time',
               existing_type=postgresql.TIMESTAMP(),
               type_=sa.String(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('summary', schema=None) as batch_op:
        batch_op.alter_column('dropoff_date_time',
               existing_type=sa.String(),
               type_=postgresql.TIMESTAMP(),
               existing_nullable=True)
        batch_op.alter_column('pickup_date_time',
               existing_type=sa.String(),
               type_=postgresql.TIMESTAMP(),
               existing_nullable=True)

    # ### end Alembic commands ###
