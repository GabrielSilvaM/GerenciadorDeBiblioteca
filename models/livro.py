from sqlalchemy import Column, String, Integer, Boolean
from .base import Base

class Livro(Base):
    __tablename__ = 'livros'

    isbn = Column(String, primary_key=True, unique=True, nullable=False)
    titulo = Column(String, nullable=False)
    autor = Column(String, nullable=False)
    editora = Column(String, nullable=False)
    anoPublicacao = Column(Integer, nullable=False)
    genero = Column(String, nullable=False)
    disponivel = Column(Boolean, default=True)