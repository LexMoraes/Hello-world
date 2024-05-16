# CLASSES - Exercício 1: Conta Bancária
# Crie uma classe chamada ContaBancaria que:
# Tenha atributos privados para titular (string) e saldo (float).
# Utilize o decorador @property para permitir que o usuário obtenha o saldo,
# mas não o modifique diretamente.
# Adicione um método para depositar dinheiro. Se o valor do depósito for negativo, mostre um erro.
# Adicione um método para sacar dinheiro. Se o saque for maior que o saldo, mostre um erro.
# Você deve criar o atributo saldo com __saldo, sendo assim ele será um atributo privado

class ContaBancaria(object):
    def __init__(self, titular = None):
        self.titular = titular
        self.__saldo = 0
    @property
    def saldo(self):
        return self.__saldo
    def sacar(self, valor: float):
        if valor > 0:
            self.__saldo -= valor
        else:
            print('operação inválida, sem saldo')

    def depositar(self, valor: float):
        self.__saldo += valor

    depositar(1000)
    print(saldo)



