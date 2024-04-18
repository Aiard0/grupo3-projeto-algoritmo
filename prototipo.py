# Biblioteca para limpar a tela (com apelido "cmd")
from os import system as cmd

# Biblioteca para espera (com apelido "wait")
from time import sleep as wait

# Biblioteca para a data (com apelido "data")
from datetime import datetime as data

# Biblioteca de banco de dados
#import sqlite3

# Cores para o terminal
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Sistema de data atual
hoje_data = data.now().strftime("%d/%m/%Y %H:%M")

# Iniciais para login
parte1 = True
v2 = True
v3 = True

# Base de usuários
parte2 = False

# Nomes e senhas para contas de usuário
adm = ["Dr. Marcelo Garcia", "Dr. Fernando Pereira", "Dr. Julia Maria", "Dr. João Guilherme"] 
funcionarios = ["Maria Clara", "Fernando", "Julia", "Joaquim Eudes"]
nao_associados = ["Julio", "Joaquim", "Maria Clara", "Fernando"]

# Banco de dados para as informações hospitalares
#   conn = sqlite3.connect('pacientes.db')
#   c = conn.cursor()
#   c.execute('CREATE TABLE IF NOT EXISTS login (id INTEGER, username TEXT PRIMARY KEY NOT NULL, password TEXT NOT NULL)')

while parte1 == True:
    while v2 == True:
        # Mensagem de boas vindas do programa
        cmd("clear")
        print(f"{bcolors.OKGREEN}Sistema de Login do " + "Hospital 'Cristo Redentor'" + f"{bcolors.ENDC} - {bcolors.HEADER}Versão 1.0{bcolors.ENDC}\nData: {hoje_data}\n")
        print("[1] - Administrador\n[2] - Funcionário\n[3] - Usuário não associado\n")
        
        # Seleção de conta de acordo com o número
        selecionador_1 = int(input("Insira o tipo de usuário para se conectar: "))
        v2 = False
        if v3 == False:
            v3 = True

    while v3 == True:
        # Seleção de conta de administrador
        if selecionador_1 == 1:
            cmd("clear")
            user = str(input("Insira o nome de sua conta de Administrador: "))
            senha = int(input("Insira a senha de sua conta de Administrador (contém 4 números distintos): "))

        # Seleção de conta de funcionário
        elif selecionador_1 == 2:
            cmd("clear")
            user = str(input("Insira o nome de sua conta de Funcionário: "))
            senha = int(input("Insira a senha de sua conta de Funcionário (contém 4 números distintos): "))

        # Seleção de conta não associada
        elif selecionador_1 == 3:
            cmd("clear")
            user = str(input("Insira o nome de sua conta não associada: "))
            senha = int(input("Insira a senha de sua conta não associada (contém 4 números distintos): "))

        # Falha se o número escolhidor for errado.
        else:
            print("Tipo de conta não encontrada, tente novamente em 5 segundos!")
            wait(5)
            v3 = False
            v2 = True
            break

        # Verificação de senha e nome de usuario
        if user in adm:
            if senha == 9451:
                cmd("clear")
                print(f"Seja bem-vindo ao Sistema Hospitalar 'Cristo Rendentor'!\n\nTipo de Conta: Administrador\nNome: {user}\nData: {hoje_data}\n\nEspere 3 segundos para ser direcionado...\n")
                v3 = False
                v2 = False
                parte1 = False
                parte2 = True
            else:
                cmd("clear")
                print("Senha incorreta, tente novamente em 5 segundos!")
                wait(5)
                v3 = False
                v2 = True
        elif user in funcionarios:
            if senha == 1234:
                cmd("clear")
                print(f"Seja bem-vindo ao Sistema Hospitalar 'Cristo Rendentor'!\n\nTipo de Conta: Funcionário\nNome: {user}\nData: {hoje_data}\n\nEspere 3 segundos para ser direcionado...\n")
                v3 = False
                v2 = False
                parte1 = False
                parte2 = True
            else:
                cmd("clear")
                print("Senha incorreta, tente novamente em 5 segundos!")
                wait(5)
                v3 = False
                v2 = True
        elif user in nao_associados:
            if senha == 1234:
                v2 = False
                cmd("clear")
                print(f"Seja bem-vindo ao Sistema Hospitalar 'Cristo Rendentor'!\n\nTipo de Conta: Usuário não associado\nNome: {user}\nData: {hoje_data}\n\nEspere 3 segundos para ser direcionado...\n")
                v3 = False
                v2 = False
                parte1 = False
                parte2 = True
            else:
                cmd("clear")
                print("Senha incorreta, tente novamente em 5 segundos!")
                wait(5)
                v3 = False
                v2 = True
        else:
            print("Conta não encontrada, tente novamente em 5 segundos!")
            wait(5)
            v3 = False
            v2 = True

# Acessar as opções com base no tipo de usuário
    while parte2 == True:
        wait(3)
        print("[1] - Verificar a lista de dados dos pacientes do Hospital\n[2] - Adicionar ficha de paciente\n[3] - Sair\n")
        selecionador_2 = int(input("Insira a opção desejada: "))
        if selecionador_2 == 3:
            print("Saindo...")
            wait(1.5)
            parte1 = False
            parte2 = False