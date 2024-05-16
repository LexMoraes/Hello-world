# 1. Criar um programa para ler o dataset
# 2. O Programa deve permitir informar um nome de um job e retornar a média de salários desse job
# 3. Maior salário US
# 4. Menor salário US

salarios_pais = []
dados = []

def obter_dados():
    dados = []
    arquivo = open('salaries.csv', 'r')

    linhas = arquivo.readlines()

    linhas.pop(0)

    for linha in linhas:
        colunas = linha.split(',')

        profissao = colunas[3]
        salario = colunas[4]
        pais = colunas[9]

        dados.append({
            "profissao": profissao,
            "salario": float(salario),
            "pais": pais
        })
    arquivo.close()
    return dados

def media_salarios(dados):
    media_profissao = []
    for dado in dados['profissao']:
        cash = 0
        cash += sum(dado["salario"])
        jobs = dado+1
    return cash/jobs

print(dados["profissao"])

# profissao = len(dado["profissao"])

def interacao():
    print('[1]. Visualizar a média salarial de uma profissão de TI;')
    print('[2]. Maior salário em dollar(U$);')
    print('[3]. Menor salário em dollar(U$);')

interacao()

choise = int(input('Escolha sua opção: '))

match choise:
    case (1):
        trabalho = input('Informe o nome da profissão: ')
        print(f'A média salarial de {trabalho} é R${media_salarios(dados[trabalho])}')


salarios = [f['salario'] for f in obter_dados() if f['pais'] == 'US']
profissoes = [f['profissao'] for f in obter_dados() if f['pais'] == 'US']

salarios_us = []
salarios_us.append([salarios])
