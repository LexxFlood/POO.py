

class Veiculo:
    def __init__(self, valor, km):
        self._valor = valor
        self._km = km

    def get_valor(self):
        return self._valor

    def get_km(self):
        return self._km

    def set_valor(self, novo_valor):
        self._valor = novo_valor

    def set_km(self, nova_km):
        self._km = nova_km

class Carro(Veiculo):
    def __init__(self, valor, km, n_portas=2):
        super().__init__(valor, km)
        self._n_portas = n_portas

    def get_n_portas(self):
        return self._n_portas

    def set_n_portas(self, novo_n):
        self._n_portas = novo_n

class Moto(Veiculo):
    def __init__(self, valor, km, n_rodas=2):
        super().__init__(valor, km)
        self._n_rodas = n_rodas

    def get_n_rodas(self):
        return self._n_rodas



