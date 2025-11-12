from banco import conta, pessoaFisica, pessoaJuridica

if __name__ == '__main__':
    p1 = pessoaFisica(nome="Vitor", saldo= 3200.00, genero="M")
    print("Pessoa fisica 1", p1)
    print(" nome: ", p1.get_nome())
    print(" saldo: ", p1.get_saldo())
    print(" genero: ", p1.get_genero())

    p2 = pessoaFisica(nome="Bruno", saldo=9800.00, genero="M")
    print("Pessoa fisica 2", p2)
    print(" nome: ", p2.get_nome())
    print(" saldo: ", p2.get_saldo())
    print(" genero: ", p2.get_genero())
    p2.set_nome("Luis")
    print(f"Nome alterado: ",p2.get_nome())

    pj1 = pessoaJuridica(nome="Jurandir", saldo=98900, modalidade="boxe")
    print("Pessoa Juridica", pj1)
    print(" nome: ", pj1.get_nome())
    print(" saldo: ", pj1.get_saldo())
    print(" modalidade: ", pj1.get_modalidade())
    pj1.set_modalidade("Taekwondo")
    print(f"Modalidade alterada: ", pj1.get_modalidade())

