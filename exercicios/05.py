print('progama dos numeros inteiros')

while True:
    try:
        num=int(input('numero inteiro : '))

    except:
        print(f'digite um numero inteiro')
        continue
    else:
        print('numero registrado')
        break


if num % 2 == 0:
    print(f'{num} é par ')
else:
    print(f'{num} é impar ')