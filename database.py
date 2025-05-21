from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base

#Cria o engine 
engine = create_engine('sqlite:///instance/biblioteca.db', echo=True)

#Cria a sessão
Session = sessionmaker(bind=engine)
session = Session()