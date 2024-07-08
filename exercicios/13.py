import os 
import time

os.system('cls')

print('Calculadora')
lista=[]

def calculadora(*n):
    while True:
        try:
            print(''' --CALCULADORA--
            1 - ADIÇÃO 
            2 - SUBTRAÇÃO
            3 - MULTIPLICAÇÃO
            4 - DIVISÃO
            5 - MOSTRAR RESULTADOS
            6 - SAIR ''')

            num = int(input('Escolha uma opção: '))

            if num > 6:
                print('Valor inválido')
                continue

        except ValueError:
            print('Digite um valor válido')
            continue

        if num == 1:
            print('ADIÇÃO SELECIONADA')
            time.sleep(1)
            try:
                valor1 = float(input('Valor: '))
                valor2 = float(input('Valor: '))
                soma = valor1 + valor2
                print(f'A soma entre {valor1} + {valor2} = {soma}')
                lista.append(soma)
            except ValueError:
                print('Digite valores numéricos válidos')
            print('='*50)

        elif num == 2:
            print('SUBTRAÇÃO SELECIONADA')
            time.sleep(1)
            try:
                valor1 = float(input('Valor: '))
                valor2 = float(input('Valor: '))
                sub = valor1 - valor2
                print(f'A subtração entre {valor1} - {valor2} = {sub}')
                lista.append(sub)
            except ValueError:
                print('Digite valores numéricos válidos')
            print('='*50)

        elif num == 3:
            print('MULTIPLICAÇÃO SELECIONADA')
            time.sleep(1)
            try:
                valor1 = float(input('Valor: '))
                valor2 = float(input('Valor: '))
                mult = valor1 * valor2
                print(f'A multiplicação {valor1} x {valor2} = {mult}')
                lista.append(mult)
            except ValueError:
                print('Digite valores numéricos válidos')
            print('='*50)

        elif num == 4:
            print('DIVISÃO SELECIONADA')
            time.sleep(1)
            try:
                valor1 = float(input('Valor: '))
                valor2 = float(input('Valor: '))
                if valor2 == 0:
                    print('Erro: Divisão por zero não é permitida.')
                else:
                    div = valor1 / valor2
                    print(f'A divisão entre {valor1} / {valor2} = {div}')
                    lista.append(div)
            except ValueError:
                print('Digite valores numéricos válidos')
            print('='*50)
        
        elif num == 5:
            print('RESULTADOS:')
            print(*lista)
            print('='*50)

        elif num == 6:
            print('FINALIZANDO...')
            time.sleep(1)
            break

        continue

calculadora()








    



    




calculadora()