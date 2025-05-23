import os
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker
from models.base import Base
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
        print("Banco criado com sucesso!")

#Cria o engine 
engine = create_engine('sqlite:///instance/biblioteca.db', echo=False)

#Cria a sessão
Session = sessionmaker(bind=engine)
session = Session()