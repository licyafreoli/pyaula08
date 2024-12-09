def filtrar(lista):
    return filter(lambda s: s == s[::-1], lista)

lista_strings = ["sorvete", "harrypotter", "arara", "sos", "level"]
palindromos = list(filtrar(lista_strings))
print(palindromos)  