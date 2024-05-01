# 5 Faça um programa que converta metros para centímetros.

while True:

    print('Esse é o conversor de escala metros para centímetros')

    m = float(input('Insira a medida em metros para a conversão(ou insira o valor 0 para finalizar o programa): '))

    if m != 0:
        print(f'O resultado de {m}m é: {m * 100}cm')
    else:
        break
