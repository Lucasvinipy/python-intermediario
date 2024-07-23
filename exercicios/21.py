import copy

lista = []

while True:
    try:
        pessoa = {}
        pessoa['nome'] = input('nome: ')
        pessoa['idade'] = int(input('idade: '))
        pessoa['situação'] = input('casado ou solteiro: ')

        lista.append(pessoa)

        continuar = input('outra pessoa [S/N]: ').upper()

        if continuar == "S":
            continue
        elif continuar == 'N':
            break
        else:
            print('valor invalido')
            continue

    except ValueError:
        print('valor invalido')
        continue

organizar=sorted(lista, key=lambda item: item['idade'] and item['nome'])
for c in organizar:
    print(c)