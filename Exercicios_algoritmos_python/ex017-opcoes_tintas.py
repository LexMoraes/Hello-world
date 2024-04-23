while True:

    print("Essa é a calculadora de consumo de tinta da loja de tinta do Alex")

    area = float(input("Qual a medida da área a ser pintada em m²?: "))

    necessidade_tinta = area / 3

    lata_de_tinta = 18
    galao = 3.6
    necessidade_lata = necessidade_tinta / lata_de_tinta
    necessidade_galao = necessidade_tinta / galao

    valor_lata = 80.00
    valor_galao = 25.00

    resto_lata = necessidade_tinta - lata_de_tinta
    resto_galao = necessidade_tinta - galao

    valor_total_galao = necessidade_galao * valor_galao
    valor_total_lata = necessidade_lata * valor_lata

    print("[1] - Comprar apenas lata conforme a necessidade;")
    print("[2] - Comprar apenas galão conforme a necessidade;")
    print("[3] - Comprar lata e/ou galão conforme a necessidade;")
    print("[4] - Sair do programa;")

    def escolha(c):
        c = int(input("Escolha uma opção de 1 à 3 para voltar ao Menu"))

    choise = int(input("Escolha: "))

    match choise:
        case 1:
            if necessidade_tinta % necessidade_lata != 0:
                qtde_lata = (necessidade_tinta // lata_de_tinta)+1
                print(f"A quantidade de latas de tintas necessárias é de {qtde_lata} lata(as) de tinta e o valor a ser pago é R${valor_lata*qtde_lata:.2f}")
                print("\n")

            else:
                qtde_lata = necessidade_tinta/lata_de_tinta
                print(f"A quantidade de latas de tintas necessárias é de {qtde_lata} lata(as) de tinta e o valor a ser pago é R${valor_lata*qtde_lata:.2f}")
                print("\n")

        case 2:
            if necessidade_tinta % necessidade_lata != 0:
                qtde_galao = (necessidade_tinta // galao)+1
                print(f"A quantidade de galões de tintas necessárias é {qtde_galao} e o valor a ser pago é R${valor_galao*qtde_galao:.2f}")
                print("\n")

            else:
                qtde_galao = necessidade_tinta/galao
                print(f"A quantidade necessária é {necessidade_tinta} litros de tinta, que corresponde a {qtde_galao} galões de tinta")
                print(f"O valor a ser pago é R${valor_galao*qtde_galao:.2f}")
                print("\n")
        case 3:
            if ((necessidade_tinta // necessidade_galao)*valor_galao) > ((necessidade_tinta // necessidade_lata)*valor_galao):
                if resto_lata <= 7.2:
                    qtde_lata = necessidade_tinta // lata_de_tinta
                    necessidade_galao = resto_lata // galao
                    print(f"A quantidade necessária é {necessidade_tinta} litros de tinta que correspondem a {necessidade_galao} galão(ões) e {qtde_lata} lata(as)")
                    print(f"O valor a ser pago é de R${valor_galao*necessidade_galao + valor_lata*qtde_lata}")
                    print("\n")

                else:
                    qtde_lata = (necessidade_tinta // lata_de_tinta)+1
                    print(f"A quantidade necessária é {necessidade_tinta} litros de tinta que correspondem a {qtde_lata} latas) ")
                    print(f"O valor a ser pago é de R${valor_lata*qtde_lata}")
                    print("\n")

            else:
                if resto_galao > 0:
                    qtde_galao = necessidade_tinta/galao
                    print(f"A quantidade necessária é {necessidade_tinta} litros de tinta que correspondem a {necessidade_galao} galões")
                    print(f"O valor a ser pago é de R${valor_galao*qtde_galao}")
                    print("\n")

        case 4:
            print("Você saiu do programa")
            print("\n")

            break
        case _:
            print("!ERRO! Opção de escolha não existe no menu: ")
            escolha(choise)
            print("\n")

    if choise == 4 or choise > 4 or choise < 0:
        break
