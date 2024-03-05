from app import *

def Cadastro():
    user = input("Digite seu usuario")
    senha = input(("digite uma senha"))
    confirm_senha=(input("Confirme sua senha"))

    if confirm_senha == senha:
        main()
    else:
        print("as senhas nao coiciden")
        sleep(3)
        system("clear")
        Cadastro()
Cadastro()