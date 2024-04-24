# Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
# Imprima os três vetores

def ler_numeros():
    numeros = []
    for c in range(20):
        numero = int(input(f'Digite {c+1}º numero inteiro: '))
        numeros.append(numero)
    return numeros

def impar_par(numeros):
    impar = []
    par = []
    for n in numeros:
        if n % 2 == 0:
            par.append(n)
        else:
            impar.append(n)
    return impar, par

numeros = ler_numeros()

impar, par = impar_par(numeros)

print('impar\n',impar)
print('par\n', par)