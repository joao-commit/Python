def inverter_palavra(palavra):
    if palavra is None:
        return
    normal = []
    invertida = []
    for letras in palavra:
        normal.append(letras)
    while normal:
        invertida.append(normal.pop())
    return "".join(invertida)

print(inverter_palavra("python"))