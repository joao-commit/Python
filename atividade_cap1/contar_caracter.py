def contador_letras(texto):
    frequencia = {}
    for caracter in texto:
        if caracter in frequencia:
            frequencia[caracter] += 1
        else:
            frequencia[caracter] = 1
    return frequencia

texto_exemplo = ("Ola Brasil")
print(f"{contador_letras(texto_exemplo)}")