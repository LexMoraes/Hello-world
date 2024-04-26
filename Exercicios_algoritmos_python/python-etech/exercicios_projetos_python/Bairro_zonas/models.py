# 1. Cria um novo projeto em python.
# 2. Crie um arquivo models.py para guardarmos as classes dos nossos projetos.
# 3. Crie uma class que represente um bairro com código autoincremento, nome, zona e população estimada.
# 4. Crie um arquivo actions.py e dentro crie uma classe BairroActions com um método estático
# para fazer o carregamentos dos bairros a partir do CSV.
# 5. Crie um arquivo chamada app.py com uma estrutura de menus para listar todos os bairros,
# listar bairros de uma determinada zona (digitada pelo usuário),
# total de habitantes por zona e quantidade de bairros por zonas.

from actions import BairroZonas



class Bairro(BairroZonas):
    def __init__(self, nome = None, zona = None, populacao = None):
        self.__nome = nome
        self.__zona = zona
        self.populacao = populacao

p = Bairro()
p.nome = '<NAME>'
p.zona = 'Bairro'
p.populacao = 20