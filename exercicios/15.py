def leitor_de_arquivo():
    nome_arquivo = input("Digite o nome do arquivo (com extensão): ")
    
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            print("Conteúdo do arquivo:\n")
            print(conteudo)
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except PermissionError:
        print(f"Erro: Sem permissão para ler o arquivo '{nome_arquivo}'.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Chama a função
leitor_de_arquivo()
