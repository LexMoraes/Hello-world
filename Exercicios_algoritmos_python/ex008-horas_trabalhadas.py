print("Este é o programa de pagamento por horas trabalhadas")
valor_hora = float(input("Informe o valor da hora trabalhada: "))
horas_mes = float(input("Informe a quantidade de horas trabalhadas no mês: "))

valor_mes = valor_hora * horas_mes

print(f"O valor pago pelas horas trabalhadas no mês é de: R${valor_mes}")