import os
from view.livro import menuLivros
from view.usuario import menuUsuarios
from view.emprestimo import menuEmprestimos

def menuPrincipal():
    while True:
        print("--- GERENCIADOR DE BIBLIOTECA ---")
        print("1. Gerenciar Livros")
        print("2. Gerenciar Usuários")
        print("3. Gerenciar Empréstimos")
        print("4. Sair")
        #Tratar erros de a opção nao ser um numero
        try:
            opcao = int(input("Escolha um opção: "))
        except ValueError:
            print("Opção deve ser um número")
            opcao = 0
        if opcao == 1:
            os.system('cls')
            menuLivros()
        elif opcao == 2:
            os.system('cls')
            menuUsuarios()
        elif opcao == 3:
            os.system('cls')
            menuEmprestimos()
        elif opcao == 4:
            print("Finalizando programa")
            return
        else:
            os.system('cls')
            print("Opção inválida")
            menuPrincipal()





def menuEmprestimos():
    pass



