class Funcionario:
    user = {}
    funcionarios = []
    def __init__(self, nome, genero, setor, login, senha):
        self.user["nome"] = nome
        self.user["genero"] = genero
        self.user["setor"] = setor
        self.user["login"] = login
        self.user["senha"] = senha

    def __str__(self):
        return f"""
            Funcionário: {self.user['nome']}
            Gênero: {self.user['genero']}
            Grupo setorial: {self.user['setor']}
            Login: {self.user['login']}"""
