from poo.produto import Produto

nome = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: "))
quantidade = int(input("Digite a quantidade do produto: "))

produto2 = Produto(nome, preco, quantidade)
produto2.visualizar()
