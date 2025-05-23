from controllers.livroController import *

def menuLivros():
    while True:
        print("--- GERENCIAMENTO DE LIVROS ---")
        print("1. Cadastrar Livro")
        print("2. Remover Livro")
        print("3. Consultar Livros")
        print("4. Voltar")
        #Laço para validar entrada de números
        while True:
            try:
                opcao = int(input("Escolha uma opção: "))
                break
            except ValueError:
                print("A opção deve ser um número!")

        if opcao == 1:
            menuCadastrarLivro()
            
        elif opcao == 2:
            menuRemoverLivro()
            
        elif opcao == 3:
            consultarLivros()
            
        elif opcao == 4:
            break

        else:
            print("Opção inválida")

def menuCadastrarLivro():
    print("--- CADASTRAR LIVRO ---")
    titulo = input("Título: ")
    autor = input("Autor: ")
    isbn = input("ISBN: ")
    #Pegando valor do ano com validação de entrada
    while True:
        try:
            anoPublicacao = int(input("Ano de publicação: "))
            break
        except ValueError:
            print("Ano inválido! Tente novamente.")

    genero = input("Gênero: ")
    editora = input("Editora: ")

    cadastrarLivros(titulo, autor, isbn, anoPublicacao, genero, editora)



def menuRemoverLivro():
    print("--- REMOVER LIVRO ---")
    print("Insira o ISBN do livro que deseja remover ou 1 para voltar")
    isbn = input()

    if isbn == '1':
        os.system('cls')
        return
    
    removerLivros(isbn)
  