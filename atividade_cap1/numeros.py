lista = list(map(int, input("Digite seus números").split()))

maior = max(lista)
menor = min(lista)
media = sum(lista) / len(lista)

print(f"Maior número: {maior}, Menor número: {menor}, Média: {media}")