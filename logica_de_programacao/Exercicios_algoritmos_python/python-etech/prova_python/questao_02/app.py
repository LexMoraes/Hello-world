import actions
import models


choose: int


while True:

    actions.exibir_menu()
    choose = int(input('Escolha uma opção: '))

    match choose:
        case 1:
            actions.cadastrar_carros()
        case 2:
            actions.listar_carros()
        case 3:
            marca = input(f'{models.cor['azul']}Marca:{models.cor['limpa']} ')
            actions.carros_marca(marca)
        case 4:
            modelo = input(f'{models.cor['azul']}Modelo:{models.cor['limpa']} ')
            actions.carros_modelo(modelo)
        case 5:
            marca = input(f'{models.cor['azul']}Marca:{models.cor['limpa']} ')
            actions.media_marca(marca)
        case 0:
            break
        case _:
            print('A escolha não existe no menu! O programa irá finalizar automaticamente.')
            break
