from datetime import datetime, date

class Pessoa(object):

    contador = 0

    def __init__(self, nome = None, aniversario = None): #__init__ -> método construtor
        print('passou pelo metodo construtor')
        self.nome = nome
        self.aniversario = aniversario

    @staticmethod # Um dos 'decorator' mais utilizados, serve para métodos de classes que não utilizam a permissão
    # 'self', sendo uma função que atua em uma situação especial, casos isolados. Todo decorator é utilizado antes
    #  de uma funçao dentro de uma classe.

    def __str__(self) -> str:
        return self.nome

    @property # Segundo 'Decorator' mais usado. Permite que uma função definida após o 'property'
    # sejá chamada como se fosse um atributo. Exemplo: uma funcão comum que possue um parâmetro
    # pode ser chamada como 'exemplo(variavel)', assim como uma função sem parâmetro pode ser chamada
    # com 'exemplo()'. Já uma função definida abaixo do decorator @property permite que uma função
    # 'exemplo' seja chamada como 'variavel.idade'
    def idade(self):
        hoje = datetime.now().date()
        diferenca = hoje - self.aniversario
        return int((diferenca).days/365)

p1 = Pessoa()