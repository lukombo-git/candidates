from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash

db = SQLAlchemy()


def init_app(app):
    db.app = app
    db.init_app(app)

#Creating the candidates model
class Candidates(db.Model):
    id_candidato = db.Column(db.Integer, primary_key=True)
    nome_completo=db.Column(db.String(255))
    data_nascimento=db.Column(db.String(255))
    natural_de=db.Column(db.String(255))
    genero=db.Column(db.String(255))
    n_bilhete = db.Column(db.String(255))
    provincia_residencia=db.Column(db.String(255))
    telemovel_principal=db.Column(db.String(255))
    email = db.Column(db.String(255))
    habilitacoes_academica=db.Column(db.String(255))
    instituicao=db.Column(db.String(255))
    curso = db.Column(db.String(255))
    ano_conclusao =db.Column(db.String(255))
    media_final = db.Column(db.String(255))
    area_candidatura=db.Column(db.String(255))
    ano_experiencia_area = db.Column(db.String(255))
    disponibilidade = db.Column(db.String(255))
    nivel_ingles=db.Column(db.String(255))
    curriculum=db.Column(db.String(255))
    
    def __repr__(self):
        return f'{self.id_candidato}'
    
    def serialize(self):
        return {
            'id_candidato':self.id_candidato,
            'nome_completo':self.nome_completo,
            'genero':self.genero,
            'provincia_residencia':self.provincia_residencia,
            'instituicao':self.instituicao,
            'curso':self.curso,
            'nivel_ingles':self.nivel_ingles,
            'habilitacoes_academica': self.habilitacoes_academica,
            'disponibilidade' :self.disponibilidade,
            'ano_experiencia_area': self.ano_experiencia_area,
            'curriculum' : self.curriculum
        }