def contar_letras(palavra):
    contador = {}

    for i in palavra:
        if i in contador:
            contador[i] = contador[i] + 1
        else:
            contador[i] = 1
    
    return contador

print(contar_letras("Banana"))