class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_estoque(self):
        return self.preco * self.quantidade
    
    def show_info(self):
        print(f"Produto: {self.nome}")
        print(f"Preço: {self.preco}")
        print(f"Quantidade: {self.quantidade}")
        print(f"Valor do estoque: {self.calcular_estoque(): .2f}")