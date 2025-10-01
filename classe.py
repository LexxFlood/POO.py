class funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def get_nome(self):
        return self.nome

    def get_salario(self):
        return self.salario

    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def set_salario(self, novo_salario):
        self.salario = novo_salario

class gerente(funcionario):
    def __init__(self, nome, salario, funcionarios):
       # self.nome = nome
       # self.salario = salario
        self.funcionarios = funcionarios
        super().__init__(nome, salario)

    #def get_nome(self):
        #return self.nome

    #def get_salario(self):
        #return self.salario

    def get_funcionarios(self):
        return self.funcionarios

    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def set_salario(self, novo_salario):
        self.salario = novo_salario

    def set_funcionarios(self, novo_funcionario):
        self.funcionarios = novo_funcionario
