def media():
    Nome_do_Aluno = str(input('Qual o nome do aluno'))
    Nota1= float(input('Digite a primeira nota do aluno'))
    Nota2= float(input('Digite segunda nota do aluno'))
    Nota3= float(input('Digite a terceira nota do aluno'))
    Media = float((Nota1 + Nota2 + Nota3)/3)
    if Media < 7:
        return f'O aluno {Nome_do_Aluno} reprovou com média {Media}'
    else:
        return f'O Aluno {Nome_do_Aluno} passou com média {Media}'

#Separação da função

print (media())
