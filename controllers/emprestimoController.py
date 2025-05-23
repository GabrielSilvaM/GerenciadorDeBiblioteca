import os
from models import *
from database import session
from tabulate import tabulate


def registrarEmprestimo(isbn, usuarioId):
    os.system('cls')
    #Checa se o usuário está correto
    if not session.query(Usuario).filter(Usuario.id==usuarioId).first():
        print("Usuário não encontrado")
        return
    
    #Checa se o isbn está correto e o livro está disponível
    if not session.query(Livro).filter(Livro.isbn==isbn, Livro.disponivel==True).first():
        print("Livro não encontrado ou indisponível")
        return

    
    novoEmprestimo = Emprestimo(livroISBN= isbn, usuarioId=usuarioId)
    session.add(novoEmprestimo)
    try:
        session.commit()
        print("Empréstimo registrado com sucesso")

    except Exception as e:
        session.rollback()
        
        print(f"Falha ao registrar empréstimo: {e}")


def registrarDevolucao(isbn, usuarioId):
    os.system('cls')
    emprestimo = session.query(Emprestimo).filter(Emprestimo.livroISBN == isbn, Emprestimo.usuarioId==usuarioId).first()

    if emprestimo:

        try:
            emprestimo.devolvido = True
            session.commit()
            print(f"Devolução do livro '{emprestimo.livro.titulo}' registrada com sucesso")

        except Exception as e:
            session.rollback()
            print(f"Falha ao registrar devolução: {e}")

    else:
        print('Empréstimo não encontrado')



def consultarEmprestimos():
    os.system('cls')
    emprestimos = session.query(Emprestimo).filter(Emprestimo.devolvido==False).all()

    if not emprestimos:
        print("Nenhum empréstimo ativo.")
        return

    #Configurando dados e header pro tabulate
    data = [[emprestimo.id, emprestimo.livroISBN, emprestimo.usuarioId,emprestimo.usuario.nome, emprestimo.dataEmprestimo.strftime('%d/%m/%Y'), emprestimo.dataDevolucao.strftime('%d/%m/%Y')] for emprestimo in emprestimos]
    
    headers = ["ID", "ISBN Livro", "ID Usuário","Nome do Usuário" , "Data de Empréstimo", "Data de Devolução"]
    
    print(tabulate(data, headers=headers, tablefmt="grid"))