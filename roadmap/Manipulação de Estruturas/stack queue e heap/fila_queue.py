from collections import deque

fila = deque()

fila.append("Ana")
fila.append("João")
fila.append("Maria")
fila.append("Pedro")

for i in range(0, 2):
    pessoa = fila.popleft()
    print(f"Atendendo: {pessoa}")

print("Fila restante:")
for pessoa in fila:
    print(pessoa)