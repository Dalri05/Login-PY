import sqlite3
from app import *
from time import sleep
from os import system

def criar_tabela_usuarios():
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user TEXT UNIQUE NOT NULL,
                        senha TEXT
                        saldo INTEGER DEFAULT 0
                    )''')
    conn.commit()
    conn.close()

def cadastrar_usuario():
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()

    usuario = input("Digite seu usuário: ")
    try:
        # Verificar se o usuário já está cadastrado
        cursor.execute('SELECT * FROM usuarios WHERE user = ?', (usuario,))
        if cursor.fetchone():
            print("Usuário já cadastrado. Tente outro nome de usuário.")
            conn.close()
            sleep(3)
            system("clear")
            inicio()
    except sqlite3.IntegrityError as e:
        print("Erro ao verificar usuário:", e)
        conn.close()
        return
    senha = input("Digite sua senha: ")
    confirm_senha = input("Confirme sua senha: ")

    if senha == confirm_senha:
        conn = sqlite3.connect('usuarios.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO usuarios (user, senha) VALUES (?, ?)', (usuario, senha))
        conn.commit()
        conn.close()
        print("Usuário cadastrado com sucesso!")
        sleep(3)
        system("clear")
        inicio()
    else:
        print("As senhas não coincidem.")
        sleep(3)
        system("clear")
        cadastrar_usuario()

def login():
    login_user = input("Digite seu usuário: ")
    login_password = input("Digite sua senha: ")

    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios WHERE user = ? AND senha = ?', (login_user, login_password))
    user = cursor.fetchone()
    conn.close()

    if user:
        print("Login bem-sucedido!")
        sleep(3)
        system("clear")
        main()
    else:
        print("Usuário ou senha incorretos!")
        sleep(3)
        system("clear")
        inicio()

def inicio():
    print("""
    [1] - Login
    [2] - Cadastro      
    """)
    op = int(input("Digite para onde deseja ir: "))
    if op == 1:
        login()
    elif op == 2:
        cadastrar_usuario()
    else:
        print("Erro...")
        sleep(5)
        system("clear")

if __name__ == "__main__":
    criar_tabela_usuarios()
    inicio()
