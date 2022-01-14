def salvar_senha(senha):
    arquivo_de_senha = open("minhas_senhas.txt", "a")
    arquivo_de_senha.write(senha)
    arquivo_de_senha.close()