import math

def funcao(a, b):
    return 2*math.pi*a*(a+b)


a = float(input("Digite o raio: "))
b = float(input("Digite a altura: "))

print(f"A área do cilindro é: {funcao(a, b)}")