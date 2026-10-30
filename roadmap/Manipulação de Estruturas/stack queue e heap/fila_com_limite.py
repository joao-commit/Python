from collections import deque

def entrar_fila(fila, pessoa):
    if len(fila) < 5:
        fila.append(pessoa)
        print(f"pessoa {pessoa} entrou na fila")
    else:
        print("Fila cheia")

fila = deque()

entrar_fila(fila, "Ana")
entrar_fila(fila, "João")
entrar_fila(fila, "Maria")
entrar_fila(fila, "Pedro")
entrar_fila(fila, "Carlos")
entrar_fila(fila, "Lucas")

print(fila)