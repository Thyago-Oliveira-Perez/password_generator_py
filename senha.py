import random
import string
import salvar

alfabeto = list(string.ascii_letters)
numeros = list(string.digits)
caracteres_especiais = list("!@#$%^&*()+=-")

caracteres = alfabeto + numeros + caracteres_especiais

senha = []

tamanho_da_senha = int(input("Digite o tamanho da senha que você deseja:"))

def gerador_de_senha(tamanho_da_senha):

    n_alfabetos = random.randrange(0, 10)
    n_numeros = random.randrange(0, 10)
    n_caracteres_especiais = random.randrange(0, 10)

    n_caracteres_totais_gerados = n_alfabetos + n_numeros + n_caracteres_especiais

    if n_caracteres_totais_gerados > tamanho_da_senha:
        gerador_de_senha(tamanho_da_senha)
    else:
        for i in range(n_alfabetos):
            senha.append(random.choice(alfabeto))
        for i in range(n_numeros):
            senha.append(random.choice(numeros))
        for i in range(n_caracteres_especiais):
            senha.append(random.choice(caracteres_especiais))
        if n_caracteres_totais_gerados < tamanho_da_senha:
            random.shuffle(caracteres)
        for i in range(tamanho_da_senha - n_caracteres_totais_gerados):
            senha.append(random.choice(caracteres))    
        random.shuffle(senha)
        
        senha_final = "".join(senha)
        print(senha_final)
        salvar.salvar_senha(senha_final+"\n")
        

gerador_de_senha(tamanho_da_senha)