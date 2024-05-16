
# João Papo-de-Pescador, homomem de bem, comprou um microcomputador para controlar o rendimento
# diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo
# regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo
# excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes)
# e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite
# e na variável multa o valor da multa que João deverá pagar.
# Imprima os dados do programa com as mensagens adequadas.

limite_kg_peixe = 50

peso_peixe = float(input('Informe o peso do peixe(kg): '))

if peso_peixe > limite_kg_peixe:
    excesso = peso_peixe - limite_kg_peixe
    multa = excesso * 4
    print(f'O excesso de peso do peixe é {excesso}kg, a multa corresponde é de aproximadamente R${multa}')
else:
    print("Não há não conformidades em relação ao regulamento de pesca do estado de São Paulo")