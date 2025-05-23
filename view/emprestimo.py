import os
from controllers.emprestimoController import *

def menuEmprestimos():
    while True:
        print("--- GERENCIAMENTO DE EMPRÉSTIMOS ---")
        print("1. Registrar Empréstimo")
        print("2. Registrar Devolução")
        print("3. Consultar Empréstimos")
        print("4. Voltar")
        #Laço para validar entrada de números
        while True:
            try:
                opcao = int(input("Escolha uma opção: "))
                break
            except ValueError:
                print("A opção deve ser um número!")

        if opcao == 1:
            menuRegistrarEmprestimos()
            
        elif opcao == 2:
            menuRegistrarDevolucao()
            
        elif opcao == 3:
            menuConsultarEmprestimos()
            
        elif opcao == 4:
            os.system('cls')
            break

        else:
            print("Opção inválida")



def menuRegistrarEmprestimos():
    print("--- REGISTRAR EMPRÉSTIMO ---")
    isbn = input("ISBN: ")
    #Laço para validar entrada de números
    while True:
        try:
            usuarioId = int(input("ID do usuário: "))
            if usuarioId > 0:
                break
            else:
                print("ID inválido")
        except ValueError:
            print("ID deve ser um número!")

    registrarEmprestimo(isbn, usuarioId)


def menuRegistrarDevolucao():
    print("--- REGISTRAR DEVOLUÇÃO ---")
    isbn = input("ISBN: ")
    #Laço para validar entrada de números
    while True:
        try:
            usuarioId = int(input("ID do usuário: "))
            if usuarioId > 0:
                break
            else:
                print("ID inválido")
        except ValueError:
            print("ID deve ser um número!")

    registrarDevolucao(isbn, usuarioId)

def menuConsultarEmprestimos():
    print("--- CONSULTAR EMPRÉSTIMOS ---")
    consultarEmprestimos()
    