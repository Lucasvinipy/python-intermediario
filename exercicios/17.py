lista=[[],[]]


def pares():
    
    while True:
        try:
            num = int(input('numero: '))

            if num % 2 == 0:
                lista[0].append(num)
            
            else:
                lista[1].append(num)

            
            
            continuar = input('outro numero [S/N]: ').upper()

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
    
    for c in lista:
        print(f'os numeros pares sao {lista[0]} e impares {lista[1]}')
    

pares()