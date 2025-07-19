def Contador_de_letras():
    Palavra = input(('Digite a sua palavra'))
    Letra = input(('Digite qual letra deve ser contada'))
    contagem = Palavra.count(Letra)

    return contagem

#Separação

print(Contador_de_letras())