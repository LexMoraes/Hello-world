import string

print('Bem vindo(a) à ferramenta que retorna se a string informada é uma vogal ou consoante:')

entrada = input('Digite uma letra: ')

numeros = list(string.digits)
caracteres = list(string.punctuation)
vogais = ['a', 'e', 'i', 'o', 'u']

if entrada in vogais:
    print(f'O valor "{entrada}" é uma vogal')

elif entrada in numeros:
    print(f'O valor "{entrada}" é um número')

elif entrada in caracteres:
    print(f'O valor "{entrada}" é um caracter especial')

else:
    print(f'O valor "{entrada}" é uma consoante')


