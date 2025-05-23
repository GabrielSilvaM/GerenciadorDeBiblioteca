import os
from models import *
from database import session
from tabulate import tabulate

def cadastrarUsuarios(nome,email,telefone,tipo, matricula):
    
    if tipo == 1:
        novoUsuario = Professor(nome=nome, email=email, telefone=telefone, matricula=matricula)
    elif tipo == 2:
        novoUsuario = Aluno(nome=nome, email=email, telefone=telefone, matricula=matricula)

    session.add(novoUsuario)
    try:
        session.commit()
        os.system('cls')
        print(f"Usuário '{nome}' cadastrado com sucesso")
    except Exception as e:
        session.rollback()
        os.system('cls')
        print(f"Falha ao cadastrar usuário: {e}")

def removerUsuarios(id):

        usuario = session.query(Usuario).filter(Usuario.id==id).first()
        if usuario:
            session.delete(usuario)
            try:
                session.commit()
                os.system('cls')
                print(f"Usuario {Usuario.nome} removido com sucesso!")
            except Exception as e:
                session.rollback()
                os.system('cls')
                print(f"Erro ao remover usuário do banco: {e}")
        else:
            print("Usuário não encontrado, verifique o ID")

def consultarUsuarios():

    usuarios = session.query(Usuario).all()

    if not usuarios:
        os.system('cls')
        print("Nenhum usuário cadastrado.")
        return

    #Configurando dados e header pro tabulate
    data = [[usuario.id, usuario.nome, usuario.email, usuario.telefone, usuario.dataCadastro, usuario.tipo, usuario.matricula] for usuario in usuarios]
    
    headers = ["ID", "Nome", "Email", "Telefone", "Data de Cadastro", "Tipo", "Matrícula"]
    
    print(tabulate(data, headers=headers, tablefmt="grid"))


