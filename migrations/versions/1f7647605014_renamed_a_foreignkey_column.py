"""renamed a foreignkey column

Revision ID: 1f7647605014
Revises: 8e0d2056b871
Create Date: 2020-07-17 12:56:51.362037

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f7647605014'
down_revision = '8e0d2056b871'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('attendees', sa.Column('service_id', sa.Integer(), nullable=True))
    op.drop_constraint('attendees_service_fkey', 'attendees', type_='foreignkey')
    op.create_foreign_key(None, 'attendees', 'churchService', ['service_id'], ['id'])
    op.drop_column('attendees', 'service')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('attendees', sa.Column('service', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'attendees', type_='foreignkey')
    op.create_foreign_key('attendees_service_fkey', 'attendees', 'churchService', ['service'], ['id'])
    op.drop_column('attendees', 'service_id')
    # ### end Alembic commands ###
