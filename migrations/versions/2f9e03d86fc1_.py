"""empty message

Revision ID: 2f9e03d86fc1
Revises: 
Create Date: 2022-03-09 02:13:13.291088

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2f9e03d86fc1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employees',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('address', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_employees'))
    )
    op.create_table('enclosures',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('area_sq', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_enclosures'))
    )
    op.create_table('animals',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('species_name', sa.String(length=50), nullable=False),
    sa.Column('common_name', sa.String(length=50), nullable=False),
    sa.Column('time_fed', sa.DateTime(), nullable=True),
    sa.Column('check_up', sa.DateTime(), nullable=True),
    sa.Column('Employee_id', sa.Integer(), nullable=False),
    sa.Column('Enclosure_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['Employee_id'], ['employees.id'], name=op.f('fk_animals_Employee_id_employees')),
    sa.ForeignKeyConstraint(['Enclosure_id'], ['enclosures.id'], name=op.f('fk_animals_Enclosure_id_enclosures')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_animals'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('animals')
    op.drop_table('enclosures')
    op.drop_table('employees')
    # ### end Alembic commands ###