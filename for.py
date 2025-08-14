lista_preco = (1000, 5490, 736, 92)

for preco in lista_preco:
    if preco <= 2000:
        imposto1 = preco * 0.15
    else:
        imposto1 = preco * 0.30
    imposto2 = preco * 0.23
    imposto3 = preco * 0.075

    imposto_total = imposto1 + imposto2 + imposto3

    print(f"O imposto total sobre um produto de R$ {preco} é de: R$ {imposto_total:.2f}")
    print(f"O valor de cada imposto é de: R$ {imposto1:.2f} R$ {imposto2:.2f} R$ {imposto3:.2f}\n")