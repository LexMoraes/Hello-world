# Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra, escrever: F - Feminino, M - Masculino, Sexo Inválido.

nome = input('Qual o seu nome? ')
print('Prazer em te conhecer, {}!'.format(nome))

print("[M] - Masculino")
print("[F] - Feminino")

genero = str(input('Informe o seu gênero? '))
genero = genero.upper()

if genero == 'M':
    print(f'{nome} é do gênero masculino')
elif genero == 'F':
    print(f'{nome} é do gênero feminino')
else:
    print('Sexo inválido.')