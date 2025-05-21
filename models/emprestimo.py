from sqlalchemy import Column, Integer, ForeignKey, DateTime, String
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base

class Emprestimo(Base):
    __tablename__ = 'emprestimos'

    id = Column(Integer, primary_key=True)
    livroISBN = Column(String, ForeignKey('livros.isbn'), nullable=False)
    usuarioId = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    dataEmprestimo = Column(DateTime, default=datetime.utcnow)
    dataDevolucao = Column(DateTime, nullable=True)
    status = Column(String, default='ativo')  # ou 'devolvido'

    livro = relationship("Livro")
    usuario = relationship("Usuario", back_populates="emprestimos")