

import modulo

lista = []

print('Programa de cadastro')

while True:
    nome = input('Digite seu nome: ')
    idade = int(input('Idade: '))
    pais = input('País: ')
    
    usuario = {'nome': nome, 'idade': idade, 'pais': pais}
    lista.append(usuario)
    
    if not modulo.continuar_operacao():
        break

print('Usuários cadastrados:')
for usuario in lista:
    print(usuario)
