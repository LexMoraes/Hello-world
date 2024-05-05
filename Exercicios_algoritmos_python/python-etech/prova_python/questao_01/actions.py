import models

car_list = []


def exibir_menu():
    asterisco = '**************************************************************'
    programa = 'Esse é o programa de cadastro de carros. O que quer fazer?'
    cadastrar = '[1] - Cadastrar carro;                                    '
    lis = '[2] - Listar carros cadastrados;                          '
    c_mar = '[3] - Listar carros de uma marca;                         '
    c_mod = '[4] - Listar carros de um modelo;                         '
    media = '[5] - Exibir valor médio de carros da mesma marca;        '
    sair = f'[0] - Sair;{47*' '}'
    print(f'{models.cor['amarelo']}{asterisco}{models.cor['limpa']}')
    print(f'{models.cor['amarelo']}*{models.cor['limpa']} {programa} {models.cor['amarelo']}*{models.cor['limpa']}')
    print(f'{models.cor['amarelo']}*{models.cor['limpa']} {cadastrar} {models.cor['amarelo']}*{models.cor['limpa']}')
    print(f'{models.cor['amarelo']}*{models.cor['limpa']} {lis} {models.cor['amarelo']}*{models.cor['limpa']}')
    print(f'{models.cor['amarelo']}*{models.cor['limpa']} {c_mar} {models.cor['amarelo']}*{models.cor['limpa']}')
    print(f'{models.cor['amarelo']}*{models.cor['limpa']} {c_mod} {models.cor['amarelo']}*{models.cor['limpa']}')
    print(f'{models.cor['amarelo']}*{models.cor['limpa']} {media} {models.cor['amarelo']}*{models.cor['limpa']}')
    print(f'{models.cor['amarelo']}*{models.cor['limpa']} {sair} {models.cor['amarelo']}*{models.cor['limpa']}')
    print(f'{models.cor['amarelo']}{asterisco}{models.cor['limpa']}')


def cadastrar_carros():
    carro = {}
    carro['placa'] = input('Informe a placa do carro: ')
    carro['marca'] = input('Informe a marca do carro: ')
    carro['modelo'] = input('Informe o modelo do carro: ')
    carro['cor'] = input('Informe a cor do carro: ')
    carro['valor'] = float(input('Informe o preco do carro: R$'))
    car_list.append(carro)
    print(f'{models.cor['verde']}Cadastro realizado com sucesso!{models.cor['limpa']}')


def listar_carros():
    for c in car_list:
        print(f'{models.cor['rosa']}Placa: {c['placa']}{models.cor['limpa']}')
        print(f'{models.cor['rosa']}Marca: {c['marca']}{models.cor['limpa']}')
        print(f'{models.cor['rosa']}Modelo: {c['modelo']}{models.cor['limpa']}')
        print(f'{models.cor['rosa']}Cor: {c['cor']}{models.cor['limpa']}')
        print(f'{models.cor['rosa']}Valor: {c['valor']}{models.cor['limpa']}')


def carros_marca(marca: str):
    for car in car_list:
        if car['marca'] == marca:
            print(f'''
            Placa: {car['placa']}
            Marca: {car['marca']}
            Modelo: {car['modelo']}
            Cor: {car['cor']}
            valor: {car['valor']}
            \n''')


def carros_modelo(modelo: str):
    for mod in car_list:
        if mod['modelo'] == modelo:
            print(f'''
            Placa: {mod['placa']}
            Marca: {mod['marca']}
            Modelo: {mod['modelo']}
            Cor: {mod['cor']}
            valor: {mod['valor']}
            \n''')

def media_marca(marca: str):
    cont = 0
    soma = 0
    for car in car_list:
        if car['marca'] == marca:
            soma += car['valor']
            cont += 1

    print(f'{models.cor['verde']}Média: {soma / cont}')

