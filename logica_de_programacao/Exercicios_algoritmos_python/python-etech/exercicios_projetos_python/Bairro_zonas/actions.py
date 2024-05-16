# 1. Cria um novo projeto em python.
# 2. Crie um arquivo models.py para guardarmos as classes dos nossos projetos.
# 3. Crie uma class que represente um bairro com código autoincremento, nome, zona e população estimada.
# 4. Crie um arquivo actions.py e dentro crie uma classe BairroActions com um método estático
# para fazer o carregamentos dos bairros a partir do CSV.
# 5. Crie um arquivo chamada app.py com uma estrutura de menus para listar todos os bairros,
# listar bairros de uma determinada zona (digitada pelo usuário),
# total de habitantes por zona e quantidade de bairros por zonas.

from typing import List, Iterator
import models

bairros: List[models.Bairro] = []


class BairroActions:

    @staticmethod
    def carregar_dados():
        arquivo = open('Bairros Manaus.csv', 'r')
        dados = arquivo.readlines()
        dados.pop(0)
        for dado in dados:
            bairros.append(BairroActions.criar_bairro(dado))
        arquivo.close()

    @staticmethod
    def criar_bairro(linha: str) -> models.Bairro:
        colunas = linha.split(';')
        bairro = models.Bairro(
            colunas[0],
            colunas[1],
            int(colunas[2])
        )
        models.Bairro.incrementar_id()
        return bairro

    @staticmethod
    def buscar_bairro(zona: str) -> Iterator[models.Bairro]:
        return filter(
            lambda bairro: bairro.zona.lower() == zona.lower(),
            bairros
        )
        # retorna [b para b em bairros se b.zona.lower() == zona.lower() com parâmetro a variável tupla 'bairro']

    @staticmethod
    def total_habitantes(zona: str) -> int:
        populacao_zona = map(
            lambda bairro: bairro.populacao,
            BairroActions.buscar_bairro(zona)
        )
        return sum(populacao_zona)

    @staticmethod
    def total_bairros(zona: str) -> int:
        return len(list(BairroActions.buscar_bairro(zona)))
