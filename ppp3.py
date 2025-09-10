class carro:
    def __init__(self, nome: str, valor: int, potencia: float, cor: str, quantidade: int):
        self.__nome = nome
        self.__valor = valor
        self.__potencia = potencia
        self.__cor = cor
        self.__quantidade = quantidade

    def get_nome(self):
        return self.__nome
    def get_valor(self):
        return self.__valor
    def get_potencia(self):
        return self.__potencia
    def get_cor(self):
        return self.__cor
    def get_quantidade(self):
        return self.__quantidade

    def set_nome(self, nome: str):
        self.__nome = nome
    def set_valor(self, valor: int):
        self.__valor = valor
    def set_potencia(self, potencia: float):
        self.__potencia = potencia
    def set_cor(self, cor: str):
        self.__cor = cor

    def calculo_de_estoque(self):
        return self.__valor * self.__quantidade

def main():
    Modelo_1 = carro(nome= "Camaro", valor= 214000, potencia= 431, cor= "Amarelo", quantidade= 5)
    Modelo_2 = carro(nome= "Aventador", valor= 484000, potencia= 691, cor= "Roxo", quantidade= 1)
    Modelo_3 = carro(nome= "Mustang", valor= 234000, potencia= 540, cor= "Azul", quantidade= 4)

    print("Modelo_1", Modelo_1.get_nome(), "| valor", Modelo_1.get_valor(), "| quantidade",
          Modelo_1.get_quantidade(), "| potencia", Modelo_1.get_potencia(), "| cor:", Modelo_1.get_cor(),)
    print("Modelo_2", Modelo_2.get_nome(), "| valor", Modelo_2.get_valor(), "| quantidade",
          Modelo_2.get_quantidade(), "| potencia", Modelo_2.get_potencia(), "| cor:", Modelo_2.get_cor(),)
    print("Modelo_3", Modelo_3.get_nome(), "| valor", Modelo_3.get_valor(), "| quantidade",
          Modelo_3.get_quantidade(), "| potencia", Modelo_3.get_potencia(), "| cor:", Modelo_3.get_cor(),)

    Modelo_1.set_cor("Azul Metálico")
    Modelo_2.set_valor(789239)
    Modelo_3.set_nome("Mustang Gt500")

    print("\nApós algumas atualizações: \n")
    print("Atualizações de produto 1: ", Modelo_1.get_cor())
    print("Atualizações do produto 2: ", Modelo_2.get_valor())
    print("Atualizações do produto 3: ", Modelo_3.get_nome())

    print("\nValor total de carros em estoque:\n")
    print(f"{Modelo_1.get_nome()} → R$ {Modelo_1.calculo_de_estoque():.2f}")
    print(f"{Modelo_2.get_nome()} → R$ {Modelo_2.calculo_de_estoque():.2f}")
    print(f"{Modelo_3.get_nome()} → R$ {Modelo_3.calculo_de_estoque():.2f}")


if __name__ == "__main__":
    main()
