def remover_duplicados(lista):
    lista2 = []
    for item in lista:
        if item not in lista2:
            lista2.append(item)
    return lista2

teste = [1, 1, 2, 2, 3, 6, 6]
print(remover_duplicados(teste))
