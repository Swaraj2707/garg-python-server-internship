"""Image table init

Revision ID: 64455fb43d6d
Revises: 57b460a916d4
Create Date: 2022-03-20 17:59:34.576038

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '64455fb43d6d'
down_revision = '57b460a916d4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('image',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('base64', sa.Text(), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_image_id'), 'image', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_image_id'), table_name='image')
    op.drop_table('image')
    # ### end Alembic commands ###