import os
from models import *
from database import session
from tabulate import tabulate

def cadastrarLivros(titulo,autor,isbn,anoPublicacao, genero,editora): 
    os.system('cls')
    novoLivro = Livro(  titulo=titulo, autor=autor, isbn=isbn,
                        anoPublicacao = anoPublicacao, genero=genero, editora=editora)

    session.add(novoLivro)
    try:
        session.commit()
        print(f"Livro '{titulo}' cadastrado com sucesso.")
    except Exception as e:
        session.rollback()
        print(f"Falha ao salvar livro no banco: {e}")

def removerLivros(isbn):
    os.system('cls')
    livro = session.query(Livro).filter(Livro.isbn==isbn).first()
    if livro:

        #Impede a remoção de livro com empréstimos ativos
        if session.query(Emprestimo).filter(Emprestimo.livroISBN==isbn, Emprestimo.devolvido==False).first():
            print("Não é possível remover livros com empréstimos ativos!")
            return


        session.delete(livro)
        try:
            session.commit()
            print(f"Livro '{livro.titulo}' removido com sucesso!")
        except Exception as e:
            session.rollback()
            print(f"Erro ao remover livro do banco: {e}")
    else:
        print("Livro não encontrado, verifique o ISBN")

def consultarLivros(autor='', genero=''):
    os.system('cls')
    if autor:
        livros = session.query(Livro).filter(Livro.disponivel==True, Livro.autor == autor).all()

    elif genero:
        livros = session.query(Livro).filter(Livro.disponivel==True, Livro.genero == genero).all()

    else:
        livros = session.query(Livro).filter(Livro.disponivel==True).all()

    if not livros:
        print("Nenhum livro encontrado.")
        return

    #Configurando dados e header pro tabulate
    data = [[livro.isbn, livro.titulo, livro.autor, livro.editora, livro.anoPublicacao, livro.genero, livro.disponivel] for livro in livros]
    
    headers = ["ISBN", "Título", "Autor", "Editora", "Ano de Publicação", "Gênero", "Disponível"]
    
    print(tabulate(data, headers=headers, tablefmt="grid"))


