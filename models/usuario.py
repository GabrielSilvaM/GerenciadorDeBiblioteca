from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    telefone = Column(String)
    dataCadastro = Column(DateTime, default=datetime.now)

    tipo = Column(String)  
    __mapper_args__ = {
        'polymorphic_identity': 'usuario',
        'polymorphic_on': tipo
    }

    emprestimos = relationship("Emprestimo", back_populates="usuario")