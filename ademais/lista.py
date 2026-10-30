lista_map = list(map(int, input("Digite seus números inteiros:").split()))

maior = max(lista_map)
menor = min(lista_map)
media = sum(lista_map) / len(lista_map)

print(f"Maior número: {maior}, Menor número: {menor}, Média: {media}")