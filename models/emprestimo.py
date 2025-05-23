from sqlalchemy import Column, Integer, ForeignKey, DateTime, String, Boolean
from sqlalchemy.orm import relationship
from datetime import date, timedelta
from .base import Base

class Emprestimo(Base):
    __tablename__ = 'emprestimos'

    id = Column(Integer, primary_key=True)
    livroISBN = Column(String, ForeignKey('livros.isbn', ondelete='SET NULL'), nullable=True)
    usuarioId = Column(Integer, ForeignKey('usuarios.id', ondelete='SET NULL'), nullable=True, )
    dataEmprestimo = Column(DateTime, default=lambda: date.today())
    dataDevolucao = Column(DateTime, default= lambda: date.today() + timedelta(days=30))
    devolvido = Column(Boolean, default=False) 

    livro = relationship("Livro", back_populates="emprestimo", passive_deletes=True)
    usuario = relationship("Usuario", back_populates="emprestimo", passive_deletes=True)