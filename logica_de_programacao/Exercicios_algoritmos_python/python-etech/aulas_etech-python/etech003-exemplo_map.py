frutas = ['mango', 'apple', 'banana']

def tamanho_item(item):
    return len(item)

transformado = map(tamanho_item, frutas)

transformado2 = map(lambda item: len(frutas), frutas)

print(f'transformado 1: {list(transformado)}')
print(f'transformado 2: {list(transformado2)}')