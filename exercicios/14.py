#cadastro de funcionarios CRUD
import os


os.system('cls')


dici = {}
listafun = []

def cadastrar_funcionario():
    try:
        nome = input('Nome: ')
        funcao = input('Função: ')
        salario = float(input('Salário: '))
        idade = int(input('Idade: '))
        funcionario = {
            'nome': nome,
            'função': funcao,
            'salario': salario,
            'idade': idade
        }
        listafun.append(funcionario)
    except ValueError:
        print('Valores inválidos. Tente novamente.')

def alterar_dados_funcionario():
    nome = input('Nome do funcionário que deseja alterar: ')
    for funcionario in listafun:
        if funcionario['nome'] == nome:
            try:
                funcao = input('Nova função: ')
                salario = float(input('Novo salário: '))
                idade = int(input('Nova idade: '))
                funcionario['função'] = funcao
                funcionario['salario'] = salario
                funcionario['idade'] = idade
                print(f'Dados de {nome} atualizados com sucesso.')
                return
            except ValueError:
                print('Valores inválidos. Tente novamente.')
                return
    print('Funcionário não encontrado.')

def listar_funcionarios():
    if not listafun:
        print('Nenhum funcionário cadastrado.')
    else:
        for funcionario in listafun:
            print(f"Nome: {funcionario['nome']}, Função: {funcionario['função']}, Salário: {funcionario['salario']}, Idade: {funcionario['idade']}")

def excluir_funcionario():
    nome = input('Nome do funcionário que deseja excluir: ')
    for funcionario in listafun:
        if funcionario['nome'] == nome:
            listafun.remove(funcionario)
            print(f'{nome} excluído com sucesso.')
            return
    print('Funcionário não encontrado.')

def cadastro():
    while True:
        print(''' --MENU DE CADASTRO--
        1 - Cadastrar Funcionário
        2 - Alterar Dados Funcionário
        3 - Listar Todos Funcionários
        4 - Excluir Funcionário
        5 - Sair ''')

        try:
            escolha = int(input('Opção: '))
        except ValueError:
            print('Valor inválido. Tente novamente.')
            continue

        if escolha == 1:
            cadastrar_funcionario()
        elif escolha == 2:
            alterar_dados_funcionario()
        elif escolha == 3:
            listar_funcionarios()
        elif escolha == 4:
            excluir_funcionario()
        elif escolha == 5:
            print('Finalizando...')
            break
        else:
            print('Opção inválida. Tente novamente.')

cadastro()







