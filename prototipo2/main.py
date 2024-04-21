cond = 0
isLogged = False
adms = [['41','Davi', 1234],
        ['51', 'Roberto', 1235]]
funcs = [['José', '1234']]

def Login():
    tipe = input("Qual o tipo da conta?[ADM/Funcionário]: ")
        
    if tipe == 'ADM':
        user = input("Insira seu CPF: ")
        senha = int(input("Insira sua senha: "))
        
        for i in range(len(adms)):
            if user in adms[i] and senha in adms[i]:
                print("Login com suceso")
                isLogged = True
                ChecarFichas()
            elif i == len(adms)-1 and isLogged == False:
                print("Login feito com não sucesso")
    
    elif tipe == 'Funcionário':
        user = input("Insira seu CPF: ")
        senha = int(input("Insira sua senha: "))

def ChecarFichas():
    cond = 1
    while cond != 2:
        print("Qual operação gostaria de fazer?\n")
        cond = int(input("1)Ver fichas dos pacientes\n2)Sair"))

while cond != 3:
    print("Bem vindo ao sistema de login do hospital tal\n")
    cond = int(input("Qual operação deseja fazer?\n1)Login\n2)Cadastramento\n3)Sair\n"))

    if cond == 1:
        Login() 
