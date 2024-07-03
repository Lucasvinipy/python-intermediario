

try:
    a=int(input('numerador : '))
    b=int(input('denominador : '))
    c=a/b

except(ValueError,TypeError):
    print('ERRO valores ou tipo de dados invalidos')

except ZeroDivisionError:
    print('nao pode ser dividido por zero')

except KeyboardInterrupt:
    print(' o usuario nao digitou nada ')

else:
    print(f'o resultado é igual a {c}')

finally:
    print('progama finalizado')