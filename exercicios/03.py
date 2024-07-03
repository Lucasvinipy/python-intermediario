def leiaInt():
    while True:
        try:
            valorflo = float(input('Digite um número real: '))
        except (TypeError, ValueError):
            print('\033[31mERRO! Digite um número real válido.\033[m')
            continue
        
        try:
            valor = int(input('Digite um número inteiro: '))
        except (TypeError, ValueError):
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
            continue
        else:
            return valor, valorflo


n = leiaInt()
print(f'Você acabou de digitar o número inteiro {n[0]} e o número real {n[1]}')
