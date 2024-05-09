from os import system as cmd
import criptacao

users = [['admin','12890509451', 'admin'],
         ['funcionario','128','Alguma coisa']]
pacientes = []
i = 0

option = 0

def acessarDocumentos():
    codigo = input("Digite o CPF do paciente: ")
    
    if isLoggedTrue: 
        for i in range(len(pacientes)):
            if codigo == pacientes[i][1]:
                print(pacientes[i])
    else:
        for i in range(len(pacientes)):
            if codigo == pacientes[i][1]:
                print(criptacao.Encriptar(pacientes[i][1]))

def cadastroPaciente():
    paciente = []
    perguntas = ['o nome: ', 'o CPF: ', 'o SUS: ', 'a idade: ', 'o número do telefone: '] 
    
    print("Sistema de Cadastramento: ")
    
    for i in range(len(perguntas)):
        paciente.append(input("Insira " + perguntas[i]))

    pacientes.insert(i, paciente)
    i += 1

def sistemaAdm():
    cond = 0
    cmd('clear')
    
    while cond != 3:
        print("Bem vindo ao sistema de administradores do sistema hospitalar\nEscolha a operação que deseja fazer\n1)Cadastrar Pacientes\n2)Acessar Documentos\n3)Retornar a Tela Inicial")     
        cond = int(input())
        
        cmd('clear')
        if cond == 1:
           cadastroPaciente()
        elif cond == 2:
            acessarDocumentos()

def sistemaFuncionario():
    print("Sistema de funcionários")

while option != 2:
    cmd('clear')
    print("Bem vindo ao Sistema de Cadastramento Hospitalar\nQual operação Deseja fazer?\n1)Login\n2)Fechar Aplicação")
    option = int(input())
    
    #Quando option for igual a 1 ele irá realizar a operação de login
    if option == 1:
        isLogged = False
        cpf = ''
        senha = ''
        
        #Sistema de Login onde vai ser verificado se o usuário está ou não logado certo
        while isLogged != True:
            cpf = input("Insira seu CPF: ")
            senha = input("Insira sua senha: ")
    
            #Vai verificar na lista de usuários do sistema se as informações inseridas está dentro
            for i in range(len(users)):  
                if cpf == users[i][1] and senha == users[i][2]:
                    isLoggedTrue = True
                    
                    #Caso o usuário seja ADM ele será executado uma operação diferente da de funcionários
                    if users[i][0] == 'admin':
                        sistemaAdm()
                    elif users[i][0] == 'funcionario':
                        sistemaFuncionario()
                
                elif i+1 == len(users): 
                    print("Informações incorretas, tente novamente")
    #Caso o usuario digite outro número sem ser 1 ou 2 o programa irá imprimir uma mensagem e repetir a aplicação
    elif option != 2:
        cmd('clear')
        print("Opção escolhida inexistente, por favor escolha uma das 2 disponiveis\n")
