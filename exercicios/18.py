
def multiplicacao(num):
    def dobro():
        return num * 2
    
    def triplo():
        return num * 3
    
    def quadruplo():
        return num * 4
    
    return dobro, triplo, quadruplo

numero = int(input("Digite um número: "))


dobro, triplo, quadruplo = multiplicacao(numero)

print(f"O dobro de {numero} é {dobro()}")
print(f"O triplo de {numero} é {triplo()}")
print(f"O quadruplo de {numero} é {quadruplo()}")
