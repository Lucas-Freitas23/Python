def Avaliador_de_senha():
    senha = f'batata'
    userSenha = input(f'Digite a senha').strip()
    if userSenha == senha:
        return f'Acesso permitido '
    else:
        return f'Acesso negado, tente novamente'
    
#Separador

print (Avaliador_de_senha())