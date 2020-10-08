"""path -> filename

Revision ID: 2b71feca9f24
Revises: 7b959a514fe1
Create Date: 2020-10-08 16:56:36.725811

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2b71feca9f24'
down_revision = '7b959a514fe1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('images', schema=None) as batch_op:
        batch_op.add_column(sa.Column('filename', sa.String(length=255), nullable=False))
        batch_op.create_unique_constraint(batch_op.f('uq_images_filename'), ['filename'])
        batch_op.drop_constraint('uq_images_path', type_='unique')
        batch_op.drop_column('path')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('images', schema=None) as batch_op:
        batch_op.add_column(sa.Column('path', sa.VARCHAR(length=255), nullable=False))
        batch_op.create_unique_constraint('uq_images_path', ['path'])
        batch_op.drop_constraint(batch_op.f('uq_images_filename'), type_='unique')
        batch_op.drop_column('filename')

    # ### end Alembic commands ###