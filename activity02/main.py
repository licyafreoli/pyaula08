produtos = {}

def adicionar(nome, preco, quantidade):
    if nome in produtos:
        print(f"O produto '{nome}' já está no estoque. Atualize a quantidade ou remova-o antes de adicionar novamente.")
    else:
        produtos[nome] = {'preco': preco, 'quantidade': quantidade}
        print(f"Produto '{nome}' adicionado com sucesso.")

def remover(nome):
    if nome in produtos:
        del produtos[nome]
        print(f"Produto '{nome}' removido com sucesso.")
    else:
        print(f"Produto '{nome}' não encontrado no estoque.")

def atualizar(nome, preco=None, quantidade=None):
    if nome in produtos:
        if preco is not None:
            produtos[nome]['preco'] = preco
        if quantidade is not None:
            produtos[nome]['quantidade'] = quantidade
        print(f"Produto '{nome}' atualizado com sucesso.")
    else:
        print(f"Produto '{nome}' não encontrado no estoque.")

adicionar("Camiseta", 29.90, 100)
adicionar("Calça Jeans", 79.90, 50)
adicionar("Tênis", 199.90, 20)

atualizar("Camiseta", preco=34.90, quantidade=120)

remover("Calça Jeans")

print(produtos)
