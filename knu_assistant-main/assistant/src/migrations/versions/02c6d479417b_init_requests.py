"""init requests

Revision ID: 02c6d479417b
Revises: b27b7aeb8ee6
Create Date: 2021-02-07 21:53:49.496948

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '02c6d479417b'
down_revision = 'b27b7aeb8ee6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('requests',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('students_group_id', sa.Integer(), nullable=False),
    sa.Column('initiator_id', sa.Integer(), nullable=False),
    sa.Column('moderator_id', sa.Integer(), nullable=False),
    sa.Column('message', sa.Text(), nullable=False),
    sa.Column('accept_callback', sa.Text(), nullable=False),
    sa.Column('reject_callback', sa.Text(), nullable=False),
    sa.Column('meta', postgresql.JSONB(astext_type=sa.Text()), nullable=False),
    sa.ForeignKeyConstraint(['initiator_id'], ['users.tg_id'], ),
    sa.ForeignKeyConstraint(['moderator_id'], ['users.tg_id'], ),
    sa.ForeignKeyConstraint(['students_group_id'], ['students_groups.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('requests')
    # ### end Alembic commands ###
