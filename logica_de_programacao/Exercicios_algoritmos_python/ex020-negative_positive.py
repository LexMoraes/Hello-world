# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

print("Este programa retorna se um dado valor numérico é positivo ou negativo.")

num = int(input("Insira um valor inteiro: "))

if num > 0:
    print("O valor informado é positivo.")
elif num == 0:
    print("O valor informado é nulo.")
else:
    print("O valor informado é negativo.")