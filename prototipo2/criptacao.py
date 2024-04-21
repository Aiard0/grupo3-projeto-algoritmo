alphabet = 'abcdefghijklmnopqrstuvwxyz'
jumps = 3
modo = ''

text = ''
cripto = ''
decripto = ''

print("Sistema de cadastro hospitalar")

cond = 0

def Encriptar(cripto):
    text = input("insira a frase a ser encriptada: ")

    for i in text.lower():
        posicion = alphabet.find(i)
        posicion += jumps 

        if posicion >= len(alphabet):
            posicion = posicion - len(alphabet)
            
        if i == ' ':
            cripto += ' '
        else:
            cripto += alphabet[posicion]   
    
    return cripto

def Decriptar(decripto):
    decripto = ''
    for i in cripto.lower():
        posicion = alphabet.find(i)
        posicion -= jumps

        if posicion < 0:
            posicion = len(alphabet) - abs(posicion)
        
        if i == ' ':
            decripto += ' '
        else:
            decripto += alphabet[posicion]   

    return decripto

while cond != 3:
    modo = input()

    if modo == 'E':
        cripto = Encriptar(cripto)
        print(cripto)

    elif modo == 'D':
        decripto = Decriptar(decripto)
        print(decripto)
