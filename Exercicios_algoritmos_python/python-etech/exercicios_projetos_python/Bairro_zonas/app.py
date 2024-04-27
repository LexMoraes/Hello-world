# 1. Cria um novo projeto em python.
# 2. Crie um arquivo models.py para guardarmos as classes dos nossos projetos.
# 3. Crie uma class que represente um bairro com código autoincremento, nome, zona e população estimada.
# 4. Crie um arquivo actions.py e dentro crie uma classe BairroActions com um método estático
# para fazer o carregamentos dos bairros a partir do CSV.
# 5. Crie um arquivo chamada app.py com uma estrutura de menus para listar todos os bairros,
# listar bairros de uma determinada zona (digitada pelo usuário),
# total de habitantes por zona e quantidade de bairros por zonas.
import actions
from actions import BairroActions
from models import Bairro


bairros = BairroActions.obter_arquivo

def menu_bairro_zona():
    print('* --------------------Menu principal-------------------- *')
    print('*  [1] - Listar todos os bairros;                        *')
    print('*  [2] - Listar bairros de uma zona;                     *')
    print('*  [3] - Total de habitantes por bairros;                *')
    print('*  [4] - Total de bairros por zonas;                     *')
    print('*  [5] - Sair do programa;                               *')
    print('* ------------------------------------------------------ *')


choise = 0

while True:

    menu_bairro_zona()

    print('\n')
    choise = int(input('Escolha uma opção: '))

    match choise:

        case 1:
            print(bairros)
        case 2:
            zona = input('Digite a zona: ')
            habitantes = actions.BairroActions.total_habitantes(zona)
            print(f'Total de habitantes de zona {zona}: {habitantes}')

        #case '3':


    if choise >= 0 and choise <= 4:
        break