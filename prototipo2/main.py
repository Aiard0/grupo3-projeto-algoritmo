from os import system as cmd

users = [['admin','12890509451', 'admin'],
         ['funcionario','128','Alguma coisa']]
option = 0

def sistemaAdm():
    print("Está logado")

while option != 2:
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
                    isLogged = True
                    
                    #Caso o usuário seja ADM ele será executado uma operação diferente da de funcionários
                    if users[i][0] == 'admin':
                        sistemaAdm()

    #Caso o usuario digite outro número sem ser 1 ou 2 o programa irá imprimir uma mensagem e repetir a aplicação
    elif option != 2:
        cmd('clear')
        print("Opção escolhida inexistente, por favor escolha uma das 2 disponiveis\n")
