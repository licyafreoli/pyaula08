import random

random.seed(42)

anos = range(2010, 2024)
culturas = ['Milho', 'Soja', 'Trigo', 'Arroz']
fazendas = ['Fazenda A', 'Fazenda B', 'Fazenda C', 'Fazenda D']

dados = [
    [ano, cultura, fazenda, random.randint(1000, 5000)]
    for ano in anos
    for cultura in culturas
    for fazenda in fazendas
]

producao_ano = {}
for ano in anos:
    producao_ano[ano] = sum([d[3] for d in dados if d[0] == ano])

producao_cultura = {}
for cultura in culturas:
    producao_cultura[cultura] = sum([d[3] for d in dados if d[1] == cultura])

producao_fazenda_2020 = {}
for fazenda in fazendas:
    producao_fazenda_2020[fazenda] = sum([d[3] for d in dados if d[2] == fazenda and d[0] == 2020])

ano_max = max(producao_ano, key=producao_ano.get)
ano_min = min(producao_ano, key=producao_ano.get)
cultura_max = max(producao_cultura, key=producao_cultura.get)
cultura_min = min(producao_cultura, key=producao_cultura.get)
fazenda_max_ano = max(producao_fazenda_2020, key=producao_fazenda_2020.get)
fazenda_min_ano = min(producao_fazenda_2020, key=producao_fazenda_2020.get)

print(ano_max, ano_min, cultura_max, cultura_min, fazenda_max_ano, fazenda_min_ano)
