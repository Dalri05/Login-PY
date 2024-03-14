from os import system
from time import sleep
import sys

saldo = 0

def deposito():
    global saldo
    add = int(input("Digite o valor que você deseja adicionar: "))
    saldo += add
    print("Seu saldo é de:", saldo)

def saque():
    global saldo
    try:
        remove = int(input("Digite o valor que você deseja sacar: "))
        if remove <= 0:
            print("Por favor, insira um valor de saque válido.")
            return saldo

        if saldo < remove:
            print("Saldo insuficiente. Seu saldo atual é de:", saldo)
        else:
            saldo -= remove
            print("Saque de", remove, "realizado com sucesso.")
            print("Seu novo saldo é de:", saldo)
        
        return saldo
    except ValueError:
        print("Entrada inválida. Por favor, insira um valor inteiro válido.")
        return saldo
    
def mensagem_saindo():
    for _ in range(5): 
        sys.stdout.write("\rSaindo" + "." * _)
        sys.stdout.flush()
        sleep(1)  
        sys.exit()

def main():
    while True:
        print(""" 
        [1] - Meu saldo
        [2] - Depósito
        [3] - Sacar
        [4] - Mostrar saldo
        [5] - Sair
        """)

        op = int(input(": "))
        
        if op == 1:
            print("Saldo inicial:", saldo)
        elif op == 2:
            deposito()
        elif op == 3:
            saque()
        elif op == 4:
            print("Saldo atual:", saldo)
        elif op == 5:
            mensagem_saindo()
        else:
            print("Opção incorreta")

if __name__ == "__main__":
    main()
