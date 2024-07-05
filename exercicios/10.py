def encontrar_elemento(lista, numero):
    try:
        
        if numero in lista:
            return numero
        else:
            return "O número não está presente na lista."
    except TypeError:
        return "Erro: Os parâmetros fornecidos não são válidos."


lista_numeros = [1, 2, 3, 4, 5]
numero_procurado = 3

resultado = encontrar_elemento(lista_numeros, numero_procurado)
print(resultado)
