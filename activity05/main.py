from collections import Counter

vendas = {
    "produto 1": 10,
    "produto 2": 15,
    "produto 3": 15,
    "produto 4": 8,
    "produto 5": 12,
}

def produto_mais_vendido(vendas):
    max_venda = max(vendas.values())
    
    maisvendidos = [produto for produto, quantidade in vendas.items() if quantidade == max_venda]
    
    return maisvendidos

top = produto_mais_vendido(vendas)
print("Produto(s) mais vendido(s):", top)
