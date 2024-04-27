# 1. Cria um novo projeto em python.
# 2. Crie um arquivo models.py para guardarmos as classes dos nossos projetos.
# 3. Crie uma class que represente um bairro com código autoincremento, nome, zona e população estimada.
# 4. Crie um arquivo actions.py e dentro crie uma classe BairroActions com um método estático
# para fazer o carregamentos dos bairros a partir do CSV.
# 5. Crie um arquivo chamada app.py com uma estrutura de menus para listar todos os bairros,
# listar bairros de uma determinada zona (digitada pelo usuário),
# total de habitantes por zona e quantidade de bairros por zonas.

from typing import List
import models

bairros: List[models.Bairro] = []

class BairroActions:
    @staticmethod
    def obter_arquivo():
        # "-> List[models.Bairro]" - é definida a typagem do retorno, apenas para melhoras a legibilidade.
        # Lista para armazenar todos os bairros durante as varreduras em linhas do arquivo.
        arquivo = open('Bairros Manaus.csv', 'r')
        linhas = arquivo.readlines()
        linhas.pop(0) # apagando a primeira linha, pois é o cabeçalho
        for linha in linhas:
            bairros.append(BairroActions.createBairros(linha))
        return bairros

        arquivo.close()

   # def buscar_bairro(zona: str) -> List[models.Bairro]:

    @staticmethod
    def createBairros(linhas: str) -> List[models.Bairro]:
        colunas = linhas.split(';')
        bairro = models.Bairro(
            colunas[0],
            colunas[1],
            colunas[2])
        models.Bairro.id()
        return
        arquivo.close()