def Verificador_de_maioridade():
    Documento = input('Você possui documento S ou N').upper()
    Idade = int(input('Qual sua idade'))
    if Documento == 'S' and Idade >= 18:
        return  'Acesso permitido'
    else:
        return 'Acesso negado'
    
#Separador 

print (Verificador_de_maioridade())