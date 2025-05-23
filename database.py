import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base


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