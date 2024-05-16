while True:

    print("Este é o programa de conversão de temperaturas Celsius e Fahrenheit.")

    print("[1] - Celsius")
    print("[2] - Fahrenheit")
    print("[3] - Sair do programa")

    choise = int(input("Informe qual é a escala da temperatura que será convertida: "))

    match choise:
        case 1:
            celsius = float(input("Insira a temperatura em Celsius: "))
            fahrenheit = (celsius * 1.8) + 32
            print(f"A temperatura {celsius}°C em Fahrenheit é: {fahrenheit}°F")
        case 2:
            fahrenheit = float(input("Digite o valor da temperatura em Fahrenheit: "))
            celsius = 5 * ((fahrenheit-32) / 9)
            print(f"A temperatura {fahrenheit}°F em Celsius é: {celsius}°C")
        case 3:
            print("Saindo do programa...")

    if choise == 3:
        break