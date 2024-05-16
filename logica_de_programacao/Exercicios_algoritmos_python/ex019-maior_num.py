# Faça um Programa que peça dois números e imprima o maior deles.

print('Este programa retorna o maior número entre dois valores informados')

num = int(input('Insira o primeiro número: '))
num2 = int(input('Insira o segundo número: '))

if num > num2:
    print(f'O maior número é: {num}')
else:
    print(f'O maior número é: {num2}')