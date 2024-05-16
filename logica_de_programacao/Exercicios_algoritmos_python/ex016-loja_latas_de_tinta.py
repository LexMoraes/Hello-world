print("Essa é a calculadora de consumo de tinta loja de tinta do Alex")
area = float(input("Qual a medida da área a ser pintada em m²?: "))

necessidade_tinta = area / 3
lata_de_tinta = 18

if necessidade_tinta > lata_de_tinta:
    necessidade_lata = necessidade_tinta // lata_de_tinta
    if necessidade_tinta % lata_de_tinta != 0:
        necessidade_lata+=1
        valor_lata = 80.00
        valor = necessidade_lata * valor_lata
    else:
        valor_lata = 80.00
        valor = necessidade_lata * valor_lata
else:
    necessidade_lata = 1
    valor_lata = 80.00
    valor = necessidade_lata * valor_lata

print("Para",area,"m², você precisará de",necessidade_tinta,"L de tinta.")
print("Logo, será necessário",necessidade_lata,"lata(s) de 18L, e deverá ser pago um total de R$",valor)
print("Visto que a lata custa R$",valor_lata)


