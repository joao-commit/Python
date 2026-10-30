class Cachorro:
    def __init__(self, nome, altura, peso):
        self.nome = nome
        self.altura = altura
        self.peso = peso

    def __del__():
        print("Você deletou o objeto")

c = Cachorro("José", 1.40, 50)
print(c.nome)