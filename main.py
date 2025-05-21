import os
from database import engine
from models.base import Base
from view.menus import *

#Verifica se o banco de dados existe e cria ele
if not os.path.exists("instance/biblioteca.db"):
    os.makedirs("instance", exist_ok=True) 
    Base.metadata.create_all(engine)
    print("Tudo na paz meu amigo")


#Loop principal da aplicação
while True:
    opcao = menuPrincipal()
    if opcao == '1':
        os.system('cls')
        print("Livros")
    elif opcao == '2':
        os.system('cls')
        print("Usuários")
    elif opcao == '3':
        os.system('cls')
        print("Empréstimos")
    elif opcao == '4':
        break
    else:
        os.system('cls')
        print("Opção inválida")