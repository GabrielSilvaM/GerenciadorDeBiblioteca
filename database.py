import os
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker
from models.base import Base
from models import *
from datetime import date, timedelta
from sqlalchemy.engine import Engine

#Serve pra fazer o SQLite respeitar as FKs, coisa que ele não faz por padrão
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


def inicializarBanco():
    #Verifica se o banco de dados existe e cria ele
    if not os.path.exists("instance/biblioteca.db"):
        os.makedirs("instance", exist_ok=True) 
        Base.metadata.create_all(engine)


        #Dados iniciais para testes da aplicação

        dadosIniciais = []

        dadosIniciais.append(Aluno(nome='Aluno Teste', email='aluno@teste.com', telefone='1536542187', matricula='1352324'))

        dadosIniciais.append(Professor(nome='Professor Teste', email='professor@teste.com', telefone='1535648712', matricula='1548124'))

        dadosIniciais.append(Livro(titulo='Clean Code',autor='Robert C Martin', isbn='8576082675',anoPublicacao = 2009, genero='Computação', editora='Alta Books'))

        #Criando um empréstimo com atraso para teste do filtro
        dadosIniciais.append(Emprestimo(livroISBN= '8576082675', usuarioId=1, dataDevolucao=date.today() - timedelta(days=7)))

        session.add_all(dadosIniciais)
        session.commit()


        print("Banco criado e preenchido com sucesso!")



#Cria o engine 
engine = create_engine('sqlite:///instance/biblioteca.db', echo=False)

#Cria a sessão
Session = sessionmaker(bind=engine)
session = Session()