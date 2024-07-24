palavras=[]
while True:
    palavraa=input('digite algo : ')
    palavras.append(palavraa)
    continuar = input('outra palavra [S/N]: ').upper()

    if continuar == "S":
        continue
    elif continuar == 'N':
        break
    else:
        print('valor invalido')
        continue



lista = [palavra for palavra in palavras if palavra.strip()[0] in 'aA']

print(f'as palavras que começam com A {lista}')
