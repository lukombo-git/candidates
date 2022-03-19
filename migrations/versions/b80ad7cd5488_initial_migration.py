"""Initial migration.

Revision ID: b80ad7cd5488
Revises: 
Create Date: 2022-03-06 07:21:34.637347

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b80ad7cd5488'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('candidates',
    sa.Column('id_candidato', sa.Integer(), nullable=False),
    sa.Column('nome_completo', sa.String(length=255), nullable=True),
    sa.Column('data_nascimento', sa.String(length=255), nullable=True),
    sa.Column('natural_de', sa.String(length=255), nullable=True),
    sa.Column('genero', sa.String(length=255), nullable=True),
    sa.Column('n_bilhete', sa.String(length=255), nullable=True),
    sa.Column('provincia_residencia', sa.String(length=255), nullable=True),
    sa.Column('telemovel_principal', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('habilitacoes_academica', sa.String(length=255), nullable=True),
    sa.Column('instituicao', sa.String(length=255), nullable=True),
    sa.Column('curso', sa.String(length=255), nullable=True),
    sa.Column('ano_conclusao', sa.String(length=255), nullable=True),
    sa.Column('media_final', sa.String(length=255), nullable=True),
    sa.Column('area_candidatura', sa.String(length=255), nullable=True),
    sa.Column('ano_experiencia_area', sa.String(length=255), nullable=True),
    sa.Column('disponibilidade', sa.String(length=255), nullable=True),
    sa.Column('nivel_ingles', sa.String(length=255), nullable=True),
    sa.Column('curriculum', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id_candidato')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('candidates')
    # ### end Alembic commands ###