def remover_duplicados(lista):
    unicos = set(lista)
    return unicos

print("Insira uma lista contendo números repetidos ")
numbers = input()
remover_duplicados(numbers)