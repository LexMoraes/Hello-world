# 1. Cria um novo projeto em python.
# 2. Crie um arquivo models.py para guardarmos as classes dos nossos projetos.
# 3. Crie uma class que represente um bairro com código autoincremento, nome, zona e população estimada.
# 4. Crie um arquivo actions.py e dentro crie uma classe BairroActions com um método estático
# para fazer o carregamentos dos bairros a partir do CSV.
# 5. Crie um arquivo chamada app.py com uma estrutura de menus para listar todos os bairros,
# listar bairros de uma determinada zona (digitada pelo usuário),
# total de habitantes por zona e quantidade de bairros por zonas.

class Bairro:
    id = 1

    def __init__(self, nome, zona, populacao):
        self.codigo = Bairro.id
        self.nome = nome
        self.zona = zona
        self.populacao = populacao

    def __str__(self):
        return f'{self.codigo}  |  {self.nome}  |  {self.zona}  |  {self.populacao}'

    @staticmethod
    def incrementar_id():
        Bairro.id += 1
