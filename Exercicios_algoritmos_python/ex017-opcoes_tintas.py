print("Essa é a calculadora de consumo de tinta loja de tinta do Alex")

area = float(input("Qual a medida da área a ser pintada em m²?: "))

necessidade_tinta = area / 3

lata_de_tinta = 18
galao = 3.6
necessidade_lata = necessidade_tinta // lata_de_tinta
necessidade_galao = necessidade_tinta // galao

valor_lata = 80.00
valor_galao = 25.00

valor_total_galao = necessidade_galao * valor_galao
valor_total_lata = necessidade_lata * valor_lata

if necessidade_tinta > necessidade_lata:
    qtde_lata = necessidade_tinta // lata_de_tinta
    resto_lata = necessidade_tinta % lata_de_tinta
    qtde_galao = resto_lata // galao
    resto_galao = resto_lata % galao
    litros_pendentes = (resto_lata-qtde_lata)*18

    print(f"{qtde_lata} latas de tinta cheias")
    print(f"{resto_lata-qtde_lata} resto de lata de tinta necessárias")
    print(f"{litros_pendentes} litros de tinta faltando")
    print(f"{qtde_galao} galões de tinta cheios")
    print(f"{resto_galao-qtde_galao} resto de galão de tinta")