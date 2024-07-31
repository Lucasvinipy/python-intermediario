def soma(x, y):
    return x + y

def multiplica(x, y):
    return x * y

def criar_funcao(funcao, *args):
    def funcao_adiada(*outros_args):
        return funcao(*(args + outros_args))
    return funcao_adiada


soma_com_cinco = criar_funcao(soma, 5)


multiplica_por_dez = criar_funcao(multiplica, 10)


print(soma_com_cinco(3))  
print(multiplica_por_dez(2))  
