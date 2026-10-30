p = float(input("Qual é o seu peso? "))
w = input("Em Libras ou Quilos (L/Q)? ").lower()

def transformar_peso(p,w):
    if w == "l":
        peso = p * 0.4536
    else:
        peso = p * 2.20462

    return peso

print("O seu peso convertido é:", transformar_peso(p, w))