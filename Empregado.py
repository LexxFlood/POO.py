from abc import ABC, abstractmethod
class Empregado(ABC):
    def __init__(self, nome, sobrenome, salario, horas_trabalhadas, ):
        self.nome = nome
        self.sobrenome = sobrenome
        self.get_salario = salario

    def get_nome(self):
        return self.nome
    def get_sobrenome(self):
        return self.sobrenome
    def set_nome(self, novo_nome):
        return novo_nome
    def set_sobrenome(self, novo_sobrenome):
        return novo_sobrenome
    def get_salario(self):
        return self.salario
    def get_horas_trabalhadas(self):
        return self.horas_trabalhadas
    @abstractmethod


