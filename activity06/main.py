def contar_pares_impares(lista):
    pares = len(list(filter(lambda x: x % 2 == 0, lista)))
    impares = len(list(filter(lambda x: x % 2 != 0, lista)))
    
    return pares, impares

lista= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares, impares = contar_pares_impares(lista)

print(f"Pares: {pares}, Ímpares: {impares}")
