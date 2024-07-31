import copy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

def aumentar(produtos, percentual):
    produtos_copy = copy.deepcopy(produtos)
    novos_produtos = []
    
    for produto in produtos_copy:
        novo_preco = produto['preco'] + produto['preco'] * (percentual / 100)
        novos_produtos.append({
            'nome': produto['nome'],
            'preco': novo_preco
        })
    
    novos_produtos_ordenados_nome = sorted(novos_produtos, key=lambda x: x['nome'])
    

    novos_produtos_ordenados_preco = sorted(novos_produtos, key=lambda x: x['preco'])
    
    return novos_produtos_ordenados_nome, novos_produtos_ordenados_preco

novos_produtos_nome, novos_produtos_preco = aumentar(produtos, 10)


print("Ordenados por nome:")
for produto in novos_produtos_nome:
    print(f"Nome: {produto['nome']}, Novo Preço: {produto['preco']:.2f}")


print("\nOrdenados por preço:")
for produto in novos_produtos_preco:
    print(f"Nome: {produto['nome']}, Novo Preço: {produto['preco']:.2f}")
