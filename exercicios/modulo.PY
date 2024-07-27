# 1 modulo 'continuar operação'
# modulo.py

def continuar_operacao():
    while True:
        try:
            continuar = input('continuar [S/N]: ').upper()

            if continuar == "S":
                return True
            elif continuar == "N":
                return False
            else:
                print('valor inválido')
        except Exception:
            print('valor inválido')
