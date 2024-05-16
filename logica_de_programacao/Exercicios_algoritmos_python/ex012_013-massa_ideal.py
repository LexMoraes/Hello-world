# Tendo como dados de entrada a altura de uma pessoa,
# construa um algoritmo que calcule seu peso ideal,
# usando as seguintes fórmulas:
# Para homens: (72.7*altura) - 58;
# Para mulheres: (62.1*h) - 44.7;


print('')
print("--------------------------------------")
print("Esta ferramenta retorna a massa ideal.")
print("--------------------------------------")

print("Qual seu gênero?:")
print("[1] - Masculino")
print("[2] - Feminino")
print("[3] - Prefiro não responder")
genero = int(input("Insira: "))

match genero:

    case 1:
        altura = float(input("Informe sua altura(m): "))
        massa_ideal = (72.7 * altura) - 58
        print(f"A massa ideal do gênero masculino com a altura de {altura}m é, aproximadamente: {massa_ideal}kg")
    case 2:
        altura = float(input("Informe sua altura(m)?: "))
        massa_ideal = (62.1 * altura) - 44.7
        print(f"A massa ideal do gênero feminino com a altura de {altura}m é, aproximadamente: {massa_ideal}kg")
    case 3:
        altura = float(input("Informe sua altura(m)?: "))
        massa_ideal = (((72.7 * altura) - 58) + ((62.1 * altura) - 44.7))/2
        print(f"A massa ideal é, aproximadamente: {massa_ideal}kg")
