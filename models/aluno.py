from sqlalchemy import Column, Integer, ForeignKey
from models.usuario import Usuario

class Aluno(Usuario):
    __tablename__ = 'alunos'

    id = Column(Integer, ForeignKey('usuarios.id'), primary_key=True)
    matricula = Column(Integer, unique=True, nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'aluno',
    }