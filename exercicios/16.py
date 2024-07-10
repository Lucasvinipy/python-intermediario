lista = []

def multiplicacao():
    while True:
        try:
            numero = int(input('numero: '))
            lista.append(numero)
            
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
    
    total = 1
    for c in lista:
        total *= c

    print(total)

multiplicacao()

