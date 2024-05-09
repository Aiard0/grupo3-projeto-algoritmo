from os import system as cmd
from time import sleep as wait
from datetime import datetime as data
from getpass import getpass as passw

# Credenciais
adm = ["Dr. Marcelo Garcia", "Dr. Fernando Pereira", "Dr. Julia Maria", "Dr. João Guilherme"] 
funcionarios = ["Maria Clara", "Fernando", "Julia", "Joaquim Eudes"]
nao_associados = ["Julio", "Joaquim", "Maria Clara", "Fernando"]

# Sistema de Cores para o terminal
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

# Sistema de Data
hoje_data = data.now().strftime("%d/%m/%Y %H:%M")

# BD para Variáveis
select = ""
select2 = ""
loginType = ""
isLogged = False
userType = ""
incorrect = False
login = ""
password = ""

# Boas vindas
def Welcome():
    cmd("clear")
    print(f"{bcolors.OKGREEN}Sistema de Login do " + "Hospital 'Cristo Redentor'" + f"{bcolors.ENDC} - {bcolors.HEADER}Versão 1.0{bcolors.ENDC}\nData: {hoje_data}\n")
    print("[1] - Administrador\n[2] - Funcionário\n[3] - Usuário não associado\n[4] - Sair\n")

def LoginType():
    select = input("Insira o tipo de usuário para se conectar: ")
    global loginType
    loginType = int(select)
    if loginType == 1 or loginType == 2 or loginType == 3:
        LoginCredentials(loginType)
    else:
        cmd("clear")
        print("Saindo...")
        wait(1.5)
        cmd("clear")
        exit()

def LoginCredentials(loginType):
    cmd("clear")
    global login
    global password
    if loginType == 1:
        print("Tipo de conta escolhido: Administrador")
        login = input("Insira o usuário de sua conta: ")
        password = int(passw("Insira a senha de sua conta: "))
        print(password)
    elif loginType == 2:
        print("Tipo de conta escolhido: Funcionário")
        login = input("Insira o usuário de sua conta: ")
        password = int(passw("Insira a senha de sua conta: "))
    elif loginType == 3:
        print("Tipo de conta escolhido: Usuário não associado")
        login = input("Insira o usuário de sua conta: ")
        password = int(passw("Insira a senha de sua conta: "))
    else:
        cmd("clear")
        print("Tipo de conta não encontrado, tente novamente em 3 segundos!")
        wait(3)
        main()

def CheckLogin(login, password):
    global isLogged
    global userType
    global incorrect
    
    # Checagem de credenciais
    if login in adm:
        if password == 94517:
            isLogged = True
            userType = "Administrador"
        else:
            incorrect = True
    elif login in funcionarios:
        if password == 97263:
            isLogged = True
            userType = "Funcionário"
        else:
            incorrect = True
    elif login in nao_associados:
        if password == 54384:
            isLogged = True
            userType = "Não associado"
        else:
            incorrect = True
    else:
        incorrect = True
    
    # Resultado para erros de credenciais
    if incorrect == True:
        wait(1)
        cmd("clear")
        print("Login ou senha incorretos, tente novamente em 3 segundos!")
        wait(3)
        incorrect = False
        main()

def WelcomeLogged(userType, login, hoje_data):
    cmd("clear")
    print(f"Seja bem-vindo ao Sistema Hospitalar 'Cristo Rendentor'!\n\nTipo de Conta: {userType}\nNome: {login}\nData: {hoje_data}\n\nEspere 3 segundos para ser direcionado...\n")
    wait(3)
    print("[1] - Verificar a lista de dados dos pacientes do Hospital\n[2] - Adicionar ficha de paciente\n[3] - Sair\n")
    select2 = int(input("O que deseja fazer? "))
    
    if select2 == 3:
        cmd("clear")
        print("Saindo...")
        wait(1.5)
        main()

# Base para aplicações de funções
def main():
    Welcome()
    LoginType()
    CheckLogin(login, password)
    WelcomeLogged(userType, login, hoje_data)

if __name__ == "__main__":
    main()