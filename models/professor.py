from sqlalchemy import Column, String, ForeignKey, Integer
from models.usuario import Usuario

class Professor(Usuario):
    __tablename__ = 'professores'

    id = Column(Integer, ForeignKey('usuarios.id'), primary_key=True)
    matricula = Column(String, unique=True, nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'professor',
    }