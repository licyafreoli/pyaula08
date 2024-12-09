vendas = [
    [2000, 2500, 2200],
    [3000, 2800, 3500],
    [1500, 1700, 1600],
    [4000, 4200, 4300]
]

media_trimestre = [sum(trimestre) / len(trimestre) for trimestre in vendas]
somas_trimestres = [sum(trimestre) for trimestre in vendas]
indice_max = somas_trimestres.index(max(somas_trimestres))
trimestre_max = vendas[indice_max]
indice_min = somas_trimestres.index(min(somas_trimestres))
trimestre_min = vendas[indice_min]
total_vendas = sum(somas_trimestres)

print("Média de vendas por trimestre:", media_trimestre)
print("Trimestre com a maior soma de vendas:", trimestre_max, "com vendas totais:", max(somas_trimestres))
print("Trimestre com a menor soma de vendas:", trimestre_min, "com vendas totais:", min(somas_trimestres))
print("Total de vendas no ano:", total_vendas)
