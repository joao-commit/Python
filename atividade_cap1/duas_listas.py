def solitario(lista1, lista2):
    conjunto1 = set(lista1) #set transforma uma lista em uma lista sem repetição
    conjunto2 = set(lista2)

    exclusivos = conjunto1 ^ conjunto2
    return list(exclusivos)

## TESTE
lista_a = [1, 3, 5, 6, 8, 9]
lista_b = [2, 4, 6, 7, 8]
resultado = solitario(lista_a, lista_b)
print(f"O resultado: {resultado}")