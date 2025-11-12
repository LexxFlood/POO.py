from carro import Veiculo
from carro import Carro
from carro import Moto

if __name__ == '__main__':

    v1 = Veiculo(valor=90000.00, km=22000)
    print("- Veículo 1:", v1)
    print("- Veículo 1:\nKm:", v1.get_km())
    print(f"Valor: {v1.get_valor():.2f}")
    v1.set_valor(80000.00)
    print(f"Valor alterado: {v1.get_valor():.2f}")

    print("-" * 20)

    v2 = Carro(valor=34000.00, km=143000)
    print("- Veículo 2:", v2)
    print("- Veículo 2:\nKm:", v2.get_km())
    print(f"Valor: {v2.get_valor():.2f}")
    v2.set_valor(65000.00)
    print(f"Valor alterado: {v2.get_valor():.2f}")
    print("Portas: ", v2.get_n_portas())

    print("-" * 20)

    v3 = Moto(valor=35000.00, km=13000)
    print("- Veículo 3:", v3)
    print("- Veículo 3:\nKm:", v3.get_km())
    print(f"Valor: {v3.get_valor():.2f}")
    v3.set_valor(26000.00)
    print(f"Valor alterado: {v3.get_valor():.2f}")
    print("Rodas: ", v3.get_n_rodas())

