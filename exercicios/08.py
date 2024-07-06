# Criação da lista e adição de elementos
lista = []

# Adicionar número à lista
try:
    num = float(input("Digite um número para adicionar à lista: "))
    lista.append(num)
except ValueError:
    print("Entrada inválida. Por favor, insira um número.")

# Verificar se o número está na lista
try:
    acesso = float(input("Digite um número para ver se está na lista: "))
    if acesso in lista:
        print(f"O número {acesso} está na lista.")
    else:
        print("O número não está na lista.")
except ValueError:
    print("Entrada inválida. Por favor, insira um número válido.")
