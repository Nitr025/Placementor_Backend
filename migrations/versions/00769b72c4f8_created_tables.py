"""Created tables

Revision ID: 00769b72c4f8
Revises: 
Create Date: 2021-04-05 15:04:32.237945

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '00769b72c4f8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=128), nullable=True),
    sa.Column('hash_password', sa.String(length=128), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('type', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_table('alumni',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('degree', sa.String(length=64), nullable=True),
    sa.Column('dept', sa.String(length=64), nullable=True),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('instiadmin',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('message',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('date_time', sa.Integer(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('recipient_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['recipient_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('recruiter',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('gen_id', sa.String(length=64), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('gen_id')
    )
    op.create_table('student',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('roll_num', sa.String(length=64), nullable=True),
    sa.Column('cgpa', sa.Float(), nullable=True),
    sa.Column('degree', sa.String(length=64), nullable=True),
    sa.Column('dept', sa.String(length=64), nullable=True),
    sa.Column('resume_link', sa.String(length=256), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('roll_num')
    )
    op.create_table('toberead',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('type', sa.String(length=64), nullable=True),
    sa.Column('entity_id', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('notice',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_time', sa.Integer(), nullable=True),
    sa.Column('subject', sa.String(length=64), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['instiadmin.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('profile',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('profileName', sa.String(length=64), nullable=True),
    sa.Column('companyName', sa.String(length=64), nullable=True),
    sa.Column('ctc', sa.Float(), nullable=True),
    sa.Column('createDate', sa.Integer(), nullable=True),
    sa.Column('releaseDate', sa.Integer(), nullable=True),
    sa.Column('deadline', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(length=128), nullable=True),
    sa.Column('degree', sa.String(length=128), nullable=True),
    sa.Column('dept', sa.String(length=128), nullable=True),
    sa.Column('recruiter_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['recruiter_id'], ['recruiter.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('application',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_time', sa.Integer(), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('content', sa.String(length=128), nullable=True),
    sa.Column('profile_id', sa.Integer(), nullable=True),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['profile_id'], ['profile.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['student.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('feedback',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_time', sa.Integer(), nullable=True),
    sa.Column('subject', sa.String(length=64), nullable=True),
    sa.Column('content', sa.String(length=128), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('profile_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['alumni.id'], ),
    sa.ForeignKeyConstraint(['profile_id'], ['profile.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('feedback')
    op.drop_table('application')
    op.drop_table('profile')
    op.drop_table('notice')
    op.drop_table('toberead')
    op.drop_table('student')
    op.drop_table('recruiter')
    op.drop_table('message')
    op.drop_table('instiadmin')
    op.drop_table('alumni')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
