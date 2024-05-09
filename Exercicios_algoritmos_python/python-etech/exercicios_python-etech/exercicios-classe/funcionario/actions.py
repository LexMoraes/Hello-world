import actions
import models


class System(models.Funcionario):


    @staticmethod
    def menu_principal():
        print(f'''
        [1] - Cadastrar funcionario;
        [2] - Listar funcionarios;
        [3] - Buscar funcionários por genero;
        [4] - Buscar funcionários por setor;
        [5] - Fazer login;
        [6] - Sair do programa;
        ''')

    @staticmethod
    def menu_contabil():
        print(f'''
        Bem vindo ao menu de contabilidade!
        [1]. Voltar ao menu principal; 
        ''')

    @staticmethod
    def menu_financeiro():
        print(f'''
        Bem vindo ao menu do financeiro!
        [1]. Voltar ao menu principal; 
        ''')

    @staticmethod
    def menu_administrado():
        print(f'''
        Este é o menu de administradores.
        Aqui você tem acesso ao menu contábil e financeiro.
        {System.menu_contabil()}
        {System.menu_financeiro()}
        ''')

    @staticmethod
    def cadastrar(user: models.Funcionario):
        lista = []
        user = models.Funcionario(
            nome=input('Digite um nome: '),
            genero=input('Digite um genero: '),
            setor=input('Informe o setor (ADMINISTRATIVO/CONTABIL/FINANCEIRO: '),
            login=input('Crie um username para o login: '),
            senha=input('Crie uma senha para o login: '))
        lista.append(user)
        return lista

    @staticmethod
    def mostrarFuncionarios():
        for u in actions.System.lista:
            print(u)

    @staticmethod
    def buscaGenero():
        g = input('Digite um gênero: ')
        for _, value in enumerate(actions.System.lista):
            if value == g and g == 'm' or 'M':
                print(value)
            elif value == g and g == 'F' or 'f':
                print(value)

    @staticmethod
    def buscaSetor():
        for _, v in enumerate(actions.System.lista):
            if v == 'FINANCEIRO' or 'financeiro':
                print(v)
            elif v == 'CONTABIL' or 'contabil':
                print(v)
            elif v == 'ADMINISTRATIVO' or 'administrativo':
                print(v)

    @staticmethod
    def logar(user):
        for index in actions.System.lista:
            if user[index] == 'ADMINISTRATIVO' or 'administrativo':
                actions.System.menu_administrado()
                option = int
                match option:
                    case 1:
                        actions.System.menu_principal()
                    case _:
                        print("Opção não existe no menu.")

            elif user[index].upper() == 'CONTABIL' or 'contabil':
                actions.System.menu_contabil()
                option = int
                match option:
                    case 1:
                        actions.System.menu_principal()
                    case _:
                        print("Opção não existe no menu.")

            elif user[index].upper() == 'FINANCEIRO' or 'financeiro':
                actions.System.menu_financeiro()
                option = int
                match option:
                    case 1:
                        actions.System.menu_principal()
                    case _:
                        print("Opção não existe no menu.")
            else:
                print('Setor inexistente!')
                actions.System.menu_principal()


