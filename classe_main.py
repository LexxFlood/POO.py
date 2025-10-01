from classe import funcionario
from classe import gerente

if __name__ == '__main__':
    f1 = funcionario(nome="Bruno", salario= 1200.00)
    print(f1)
    f2 = funcionario(nome= "Jurandir", salario= 3000.00)
    print(f2)
    f3 = funcionario(nome="Ronaldo", salario=2000.00)
    print(f3)

    f1.set_nome("Jorge")
    print("Novo nome: ", f1.get_nome())

    f2.set_nome("Vinicius")
    print("Novo nome: ", f2.get_nome())

    print("\nFuncionario 1: ", f1.get_nome(), "| salario: ", f1.get_salario())
    f1.set_nome(f1)

    print("Funcionario 2: ", f2.get_nome(), "| salario: ", f2.get_salario())
    print("Bonificacao: ", f2.bonus())

    print("Funcionario 3: ", f3.get_nome(), "| salario: ", f3.get_salario())
    print("Bonificacao: ", f3.bonus())



    g1 = gerente(nome= "Fabio", salario= 7500.00, funcionarios= 3)
    print(g1)
    print("\nGerente: ", g1.get_nome(), "| salario: ", g1.get_salario(), "| funcionarios: ", g1.get_funcionarios())
    print("Bonificacao: ", g1.bonus())

