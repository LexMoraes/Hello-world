def menu():
    print("_________________________________________________________________________")
    print("-  Esse é o programa para informar rendimentos, o que você quer fazer?: -")
    print("-  [1]. Visualizar salario bruto;                               -")
    print("-  [2]. Valor pago ao sindicato;                                        -")
    print("-  [3]. Valor pago ao INSS;                                             -")
    print("-  [4]. Valor pago ao Imposto de Renda (IF);                            -")
    print("-  [5]. Total em descontos e salário líquido;                           -")
    print("-  [6]. Exit;                                                           -")
    print("_________________________________________________________________________")

escolha = 0

while escolha < 6:

    menu()

    escolha = int(input("Escolha sua opção: "))

    if escolha == 1:
        ganho_mensal = float(input("Digite o valor do ganho mensal: "))
        print("O salário informado é: ", ganho_mensal)

    if escolha == 2:
        ganho_mensal = float(input("Digite o valor do ganho mensal: "))
        sindicato = 0.05*ganho_mensal
        print("Valor pago ao sindicato: ", sindicato)

    if escolha == 3:
        ganho_mensal = float(input("Digite o valor do ganho mensal: "))
        inss = 0.08*ganho_mensal
        print("Valor pago ao INSS é: ", inss)

    if escolha == 4:
        ganho_mensal = float(input("Digite o valor do ganho mensal: "))
        ir = 0.11*ganho_mensal
        print("Valor pago ao Imposto de Renda(IF): ", ir)

    if escolha == 5:
        ganho_mensal = float(input("Digite o valor do ganho mensal: "))
        inss = 0.08*ganho_mensal
        sindicato = 0.05*ganho_mensal
        ir = 0.11*ganho_mensal
        descontos = inss+sindicato+ir
        total_liquido = ganho_mensal-descontos
        print("O salário líquido é R$",total_liquido,"e o desconto total é de R$",descontos)

    if escolha == 6:
        print("Programa finalizado")
        break
    elif escolha > 6:
        print("Opção inexistente no menu")
        escolha = int(input("Escolha outra opção, de 1 à 6 para retornar ao menu do programa: "))
