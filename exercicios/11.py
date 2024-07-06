import os
os.system('cls')

lista = []

while True:
    try:
        item = input('ITEM: ').upper()
        lista.append(item)
        print('='*50)
        
        while True:
            continuar = input('OUTRO? [S/N] ').strip().upper()
            if continuar == 'N':
                break
            elif continuar == 'S':
                break
            else:
                print('Opção inválida! Digite S para continuar ou N para parar.')
        
        if continuar == 'N':
            break
    
    except Exception as e:
        print('Ocorreu um erro:', e)
        print('Digite um valor válido.')
os.system('cls')

print('='*50)
while True:
    try:
        print('''1 - apagar item lista
2 - listar valores
3- encerrar progama ''')
        escolha=int(input('ESCOLHA UM VALOR :  '))
        print("="*50)

    except:
        print('valor invalido')
        continue

    if escolha == 1:
        apagar=input('NOME DO ITEM : ').upper().strip()

        try:
            lista.remove(apagar)
            print('-------ITEM APAGADO-------')
            continue

        except:
            print('valor nao encontrado')
            continue

    if escolha == 2:
        for i , e in enumerate(lista):
            print(f' {i + 1} == {e}')
            print('='*50)

    if escolha == 3:
        os.system('cls')
        print('PROGAMA ENCERRADO')