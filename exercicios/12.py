try:
    nome_arquivo = input("Digite o nome do arquivo: ")
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
        print(conteudo)
except FileNotFoundError:
    print("Erro: Arquivo não encontrado.")
