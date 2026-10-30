class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    
    def valor_estoque(self):
        return self.preco * self.quantidade
        
    def visualizar(self):
        print(f"Produto: {self.nome}")
        print(f"Preço: R${self.preco: .2f}")
        print(f"Quantidade: {self.quantidade}")
        print(f"Valor do estoque: {self.valor_estoque(): .2f}")
        