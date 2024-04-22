import math

print("Olá! Essa é a Calculadora de Área de Circulo do Alex")
r = float(input("Qual o raio do circulo que quer descobrir a área em cm²?: "))

equacao_area_circulo = 2*math.pi*r**2

print(f"A área deste círculo é: {equacao_area_circulo}cm²")
