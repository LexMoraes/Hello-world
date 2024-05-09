import actions
import models

while True:

    actions.System.menu_principal()
    choose = int(input("Escolha: "))
    user = models.Funcionario

    match choose:
        case 1:
            actions.System.cadastrar(user)
        case 2:
            actions.System.mostrarFuncionarios()
        case 3:
            actions.System.buscaGenero()
        case 4:
            actions.System.buscaSetor()
        case 5:
            actions.System.logar(user)
        case _:
            print('Opção inválida, entre com qualquer tecla e escolha novamente.')
            actions.System.menu_principal()
    if choose == 6:
        break
