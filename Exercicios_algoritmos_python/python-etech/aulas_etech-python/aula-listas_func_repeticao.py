#Criando listas

print("")
lista = ["hello"]

lista.append("world")

print(lista)

frutas = []

frutas.append("maçã")
frutas.append("morango")
frutas.append("banana")
frutas.append("mamão")
frutas.append("abacaxi")

print("Lista frutas")
print(frutas)

family = []

family.append("Alex")
family.append("Si")
family.append("Nala")
family.append("Pheobe")
family.append("Pastel")
family.append("Bilbo")

print("lista de frutas invertidas")

# Para inverter uma lista(ou uma string), deve fazer o slicing com parâmetro de passo negativo.
# Onde no python, o método de slicing possui 3 parâmetros; lista(início:meio:passo)

print(frutas[::-1])

print("Tupla")
tupla = ("maçã", "uva",)
print(tupla)

#Declarando um dicionário com variavel = {chave: valor}

funcionario = {"nome": "Alex","idade": 25, "gênero": "masculino"}

print("Mostrando dicionário 'funcionário'")
print(funcionario)

print(funcionario["nome"])
print(funcionario["idade"])
print(funcionario["gênero"])

#Outra forma de declarar utilizando explicitamente a função de dicionário

outro_funcionario = dict()
outro_funcionario["name"] = "Alex"
outro_funcionario["age"] = 25
outro_funcionario["genera"] = "male"

print("Imprimindo a outra declaração")
print(outro_funcionario)
print(outro_funcionario["name"])
print(outro_funcionario["age"])
print(outro_funcionario["genera"])

#repetição for, método range e função enumerate:

numeros = [10,20,30,40,50]

for n in numeros:
    print(numeros)


for posicao, valor in enumerate(numeros):
    print(f'{posicao} - {valor}')

#Definindo funções e conhecendo parâmetros
def somar (a, b):
    return a + b

def multiplicar (a, b):
    return a * b

def subtrair (a, b):
    return a - b

def dividir (a, b):
    return a / b

#imprimindo as funções definidas

print(somar(10,10))
print(subtrair(10,10))
print(multiplicar(10,10))
print(dividir(10,10))
