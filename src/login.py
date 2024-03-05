from app import *
from cadastro import Cadastro


def inicio():
    print("""
    [1] - Login
    [2] - Cadastro      
""")
    op = int(input("Digite para onde deseja ir: "))
    if op == 1:
        login()
    elif op == 2:
        Cadastro()
    else:
        print("Erro...")
        sleep(5)
        system("clear")
inicio()

def senha():
    senha_digitada = input("Digite sua senha: ")
    senha_correta = "2005"

    if senha_digitada == senha_correta:
        main()
    else:
        print("Senha incorreta")

def login():
    user = input('Digite seu usuário: ')

    if user == "joao":
        senha()
    else:
        print("Usuário incorreto")

if __name__ == "__main__":
    inicio()