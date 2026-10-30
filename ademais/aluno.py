class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def print_info(self):
        print(self.nome, self.idade)

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    def print_info(self):
        super().print_info()
        print(self.matricula)

aluno1 = Aluno("João", 20, "12345")
aluno1.print_info()