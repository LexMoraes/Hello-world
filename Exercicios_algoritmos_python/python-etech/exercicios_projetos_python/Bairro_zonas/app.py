# 1. Cria um novo projeto em python.
# 2. Crie um arquivo models.py para guardarmos as classes dos nossos projetos.
# 3. Crie uma class que represente um bairro com código autoincremento, nome, zona e população estimada.
# 4. Crie um arquivo actions.py e dentro crie uma classe BairroActions com um método estático
# para fazer o carregamentos dos bairros a partir do CSV.
# 5. Crie um arquivo chamada app.py com uma estrutura de menus para listar todos os bairros,
# listar bairros de uma determinada zona (digitada pelo usuário),
# total de habitantes por zona e quantidade de bairros por zonas.
import actions


def menu_bairro_zona():
    print('* --------------------Menu principal-------------------- *')
    print('*  [1] - Listar todos os bairros;                        *')
    print('*  [2] - Listar bairros de uma zona;                     *')
    print('*  [3] - Total de habitantes por zona;                   *')
    print('*  [4] - Total de bairros por zonas;                     *')
    print('*  [5] - Sair do programa;                               *')
    print('* ------------------------------------------------------ *')

def main():
    actions.BairroActions.carregar_dados()
    while True:
        menu_bairro_zona()
        opcao = int(input('Digite sua opção: '))

        match opcao:
            case 1:
                for b in actions.bairros:
                    print(b)

            case 2:
                zona = input('Digite a zona: ')
                bairros = actions.BairroActions.buscar_bairro(zona)
                for b in bairros:
                    print(b)
            case 3:
                zona = input('Digite a zona: ')
                habitantes = actions.BairroActions.total_habitantes(zona)
                print(f'Total de habitantes da zona {zona}: {habitantes}')

            case 4:
                zona = input('Digite a zona: ')
                total_bairros = actions.BairroActions.total_bairros(zona)
                print(f'Total de bairros da zona {zona}: {total_bairros}')

            case 5:
                break
                
            case _:
                print('Opção inexistente, entre com qualquer tecla para voltar ao menu principal.')
                main()

main()
