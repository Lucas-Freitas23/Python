#Calculadora
print ('Calculadora')
print (('Escolha uma operação, Soma = 1, Subtração = 2, Multiplicação = 3, Divisão = 4, Potência = 5 e Resto da divisão = 6'))
def Calculadora():
    operador = int(input('Escolha o seu operador'))
    num1 = float(input('Escolha o primero Número'))
    num2 = float(input('Escolha o segundo número'))
    if operador == 1:
        return num1 + num2
    elif operador == 2:
        return num1 - num2
    elif operador == 3:
        return num1 * num2
    elif operador == 4:
        return num1 / num2
    elif operador == 5:
        return num1 ** num2
    elif operador == 6:
        return num1 // num2
    else:
        return 'Erro'

#Separação]

print (Calculadora())