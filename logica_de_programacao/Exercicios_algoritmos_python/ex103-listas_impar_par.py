# Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
# Imprima os três vetores

def ler_numeros():
    numeros = []
    for c in range(20):
        numero = int(input(f'Digite o {c+1}º numero inteiro: '))
        numeros.append(numero)
    return numeros

def impar_par(numeros):
    impar = []
    par = []
    nulos = 0

    for n in numeros:
        if n % 2 == 0 and n != 0:
            par.append(n)
        elif n == 0:
            nulos += 1
        else:
            impar.append(n)
    return impar, par, nulos

numeros = ler_numeros()

impar, par, nulos = impar_par(numeros)

print('impar\n',impar)
print('par:\n', par)
print('Dígitos nulos: \n', nulos)
