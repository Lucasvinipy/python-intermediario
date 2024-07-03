print('progama que que le horario')

while True:
    try:
        horario=int(input('horario : '))

    except:
        print('por favor insira um numero inteiro')
        continue
    else:
        print('numero valido')
        break


if horario > 0 and horario < 11:
    print('bom dia')

elif horario >= 12 and horario < 17:
    print('boa tarde')

else:
    print('boa noite')
