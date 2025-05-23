from controllers.usuarioController import *

def menuUsuarios():
    while True:
        print("--- GERENCIAMENTO DE USUÁRIOS ---")
        print("1. Cadastrar Usuário")
        print("2. Remover Usuário")
        print("3. Consultar Usuário")
        print("4. Voltar")
        #Laço para validar entrada de números
        while True:
            try:
                opcao = int(input("Escolha uma opção: "))
                break
            except ValueError:
                print("A opção deve ser um número!")
        if opcao == 1:
            os.system('cls')
            menuCadastrarUsuarios()  
        elif opcao == 2:
            os.system('cls')
            menuRemoverUsuarios()
        elif opcao == 3:
            os.system('cls')
            menuConsultarUsuarios()
        elif opcao == 4:
            os.system('cls')
            break
        else:
            print("Opção inválida")

        
def menuCadastrarUsuarios():
    print("--- CADASTRAR USUÁRIO ---")
    nome = input("Nome: ")
    email = input("Email: ")
    telefone = input("Telefone: ")
    while True:
        try:
            tipo = int(input("1. Cadastrar Professor\n2. Cadastrar Aluno \n"))
            if tipo >= 1 and tipo <= 2:
                break
            else:
                print("Opção inválida")
        except ValueError:
            print("Opção deve ser um número")
    matricula = input("Matrícula: ")
    cadastrarUsuarios(nome,email,telefone,tipo, matricula)


def menuRemoverUsuarios():
    print("--- REMOVER USUÁRIO ---")
    while True:
        print("Insira o ID do usuário que deseja remover ou 0 para voltar")
        try:
            id = int(input())
            break
        except ValueError:
            print("O ID deve ser um número")



    if id == 0:
        os.system('cls')
        return

    removerUsuarios(id)

def menuConsultarUsuarios():
    print("--- CONSULTAR USUÁRIO ---")
    print("1. Todos os usuários")
    print("2. Usuários com atraso")
    print("3. Voltar")

    while True:
        try:
            opcao = int(input())
            if opcao >= 1 and opcao <= 4:
                break
        except ValueError:
            print("Opção inválida")
    
    if opcao == 1:
        consultarUsuarios()
    elif opcao == 2:
        consultarUsuarios(filtrarAtrasos=True)


    