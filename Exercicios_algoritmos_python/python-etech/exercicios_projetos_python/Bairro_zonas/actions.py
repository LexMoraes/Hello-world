# 1. Cria um novo projeto em python.
# 2. Crie um arquivo models.py para guardarmos as classes dos nossos projetos.
# 3. Crie uma class que represente um bairro com código autoincremento, nome, zona e população estimada.
# 4. Crie um arquivo actions.py e dentro crie uma classe BairroActions com um método estático
# para fazer o carregamentos dos bairros a partir do CSV.
# 5. Crie um arquivo chamada app.py com uma estrutura de menus para listar todos os bairros,
# listar bairros de uma determinada zona (digitada pelo usuário),
# total de habitantes por zona e quantidade de bairros por zonas.

class BairroZonas:
    @staticmethod
    def __init__():
        def obter_dados():

            dados = []

            arquivo = open('Bairros Manaus.csv', 'r')

            linhas = arquivo.readlines()

            linhas.pop(0)

            for linha in linhas:
                colunas = linha.split(',')

                name = colunas[0]
                zone = colunas[1]
                population = colunas[2]

            return name, zone, population

            arquivo.close()



