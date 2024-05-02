from datetime import date


class Pessoa:
    def __init__(self, nome, nascimento, cidade):
        self.nome = nome
        self.nascimento = None
        self.cidade = cidade

    def __str__(self):
        print(f'Olá, {self.nome}, bem vindo a saudacao do exercício do Alex.')
        print(f'\nPercebo que você possuem {self.nascimento} anos de idade.')
        print(f'E você é de {self.cidade}, é uma cidade muito boa.')

    @property
    def get_idade(self):
        return date.today() - 