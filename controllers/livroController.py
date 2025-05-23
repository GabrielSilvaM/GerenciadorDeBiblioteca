import os
from models import *
from database import session
from tabulate import tabulate

def cadastrarLivros(titulo,autor,isbn,anoPublicacao, genero,editora): 
        novoLivro = Livro(  titulo=titulo, autor=autor, isbn=isbn,
                            anoPublicacao = anoPublicacao, genero=genero, editora=editora)

        session.add(novoLivro)
        try:
            session.commit()
            os.system('cls')
            print(f"Livro '{titulo}' cadastrado com sucesso.")
        except Exception as e:
            session.rollback()
            os.system('cls')
            print(f"Falha ao salvar livro no banco: {e}")

def removerLivros(isbn):
    livro = session.query(Livro).filter(Livro.isbn==isbn).first()
    if livro:
        session.delete(livro)
        try:
            session.commit()
            os.system('cls')
            print(f"Livro '{livro.titulo}' removido com sucesso!")
        except Exception as e:
            session.rollback()
            os.system('cls')
            print(f"Erro ao remover livro do banco: {e}")
    else:
        print("Livro não encontrado, verifique o ISBN")

def consultarLivros():

    livros = session.query(Livro).all()

    if not livros:
        os.system('cls')
        print("Nenhum livro cadastrado.")
        return

    #Configurando dados e header pro tabulate
    data = [[livro.isbn, livro.titulo, livro.autor, livro.editora, livro.anoPublicacao, livro.genero, livro.disponivel] for livro in livros]
    
    headers = ["ISBN", "Título", "Autor", "Editora", "Ano de Publicação", "Gênero", "Disponibilidade"]
    
    print(tabulate(data, headers=headers, tablefmt="grid"))


