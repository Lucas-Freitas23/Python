def Saudacao_completa():
    nome = input('Digite o seu nome: ')
    nome_formatado = nome.strip().title()
    return f'Olá, {nome_formatado}! Seja bem-vindo(a)!'

#Separação
print(Saudacao_completa())
