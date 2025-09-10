class veiculo:
    def __init__(self, modelo: str, ano: int, valor: float):
        self.__modelo = modelo
        self.__ano = ano
        self.__valor = valor

    def get_modelo(self):
        return self.__modelo

    def get_ano(self):
        return self.__ano

    def get_valor(self):
        return self.__valor

    def set_modelo(self, novo_modelo):
        self.modelo = novo_modelo

    def set_ano(self, novo_ano):
        self.ano = novo_ano

    def set_valor(self, novo_valor):
        self.valor = novo_valor

    def aumento_valor(self, aumento_valor):
        self.valor = self.valor + aumento_valor

if __name__ == '__main__':
    carro1 = veiculo(modelo = "hb20", ano = 2020, valor = 80000.00)
    carro2 = veiculo( "civic",  2024,  142000.00)


    print("Carro1", carro1.get_modelo(),"| Ano", carro1.get_ano(), "| Valor", carro1.get_valor() )
    print("Carro2", carro2.get_modelo(),"| Ano", carro2.get_ano(), "| Valor", carro2.get_valor() )

    print("\nDados atualizados!! \n")

    print("Atualizações do carro 1\n")
    m = input("Digite o novo modelo:")
    a = int(input("Digite o ano:"))
    v = float(input("Digite o valor:"))

    print("Atualizações do carro 2\n")
    m2 = input("Digite o novo modelo:")
    a2 = int(input("Digite o ano:"))
    v2 = float(input("Digite o valor:"))

    print("carro1", m, "| ano", a, "| valor", v)
    print("carro2", m2, "| ano", a2, "| valor", v2)

    vl_aumento = float(input("Valor do aumento: "))
    carro2.aumento_valor(vl_aumento)
    print("valor aualizado: ", carro2.get_valor())

