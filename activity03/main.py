cores = {"vermelho", "azul", "verde", "amarelo", "roxo", "preto", "branco", "laranja"}

def quatro_letras():
    return {cor for cor in cores if len(cor) > 4}

print(quatro_letras())
