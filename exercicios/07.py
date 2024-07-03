print('Programa que classifica o nome do usuário')

while True:
    try:
        nome = input('Nome: ')
        if not nome.isalpha():
            raise ValueError('Nome deve conter apenas letras.')  
    except ValueError as e:
        print(f'\033[31mERRO! {e}\033[m')
        continue
    else:
        break

if len(nome) <= 4:
    print('Nome curto')
elif 5 <= len(nome) <= 8:
    print('Nome médio')
else:
    print('Nome grande')
