import os
from models import *
from database import session
from tabulate import tabulate
from datetime import date

def cadastrarUsuarios(nome,email,telefone,tipo, matricula):
    os.system('cls')
    if tipo == 1:
        novoUsuario = Professor(nome=nome, email=email, telefone=telefone, matricula=matricula)
    elif tipo == 2:
        novoUsuario = Aluno(nome=nome, email=email, telefone=telefone, matricula=matricula)

    session.add(novoUsuario)
    try:
        session.commit()
        print(f"Usuário '{nome}' cadastrado com sucesso")
    except Exception as e:
        session.rollback()
        print(f"Falha ao cadastrar usuário: {e}")

def removerUsuarios(id):
    os.system('cls')
    
    usuario = session.query(Usuario).filter(Usuario.id==id).first()
    if usuario:

        #Impede a remoção de usuário com empréstimos ativos
        if session.query(Emprestimo).filter(Emprestimo.usuarioId==id, Emprestimo.devolvido==False).first():
            print("Não é possível remover usuários com empréstimos ativos!")
            return


        session.delete(usuario)
        try:
            session.commit()
            print(f"Usuario {usuario.nome} removido com sucesso!")
        except Exception as e:
            session.rollback()
            print(f"Erro ao remover usuário do banco: {e}")
    else:
        print("Usuário não encontrado, verifique o ID")

def consultarUsuarios(filtrarAtrasos=False):
    os.system('cls')

    #Filtra os usuários com empréstimos atrasados
    #Faz join das duas tabelas e filtra os não devolvidos e com data de devolução menor que o dia de hoje
    if filtrarAtrasos:
        usuarios = session.query(Usuario).join(Emprestimo).filter(
        Emprestimo.devolvido == False,
        Emprestimo.dataDevolucao < date.today()).all()
        
    #Ou busca todos os usuários
    else:
        usuarios = session.query(Usuario).all()

    if not usuarios:
        
        print("Nenhum usuário encontrado.")
        return

    #Configurando dados e header pro tabulate
    data = [[usuario.id, usuario.nome, usuario.email, usuario.telefone, usuario.dataCadastro.strftime('%d/%m/%Y'), usuario.tipo, usuario.matricula] for usuario in usuarios]
    
    headers = ["ID", "Nome", "Email", "Telefone", "Data de Cadastro", "Tipo", "Matrícula"]
    
    print(tabulate(data, headers=headers, tablefmt="grid"))


