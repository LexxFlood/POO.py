lista_preco = (1000, 5490, 736, 92)

def calculo_imposto_total(preco):
    if preco <= 2000:
        imposto1 = preco * 0.15
    else:
        imposto1 = preco * 0.30
    imposto2 = preco * 0.23
    imposto3 = preco * 0.075
    imposto_total = imposto1 + imposto2 + imposto3
    return imposto_total

for preco in lista_preco:
    imposto_total = calculo_imposto_total(preco)
    print(f"O imposto total sobre um produto de R$ {preco} é de: R$ {imposto_total:.2f}")

nova_lista_produtos = (2000, 345, 8732, 234)

for preco in nova_lista_produtos:
    imposto_total = calculo_imposto_total(preco)
    print(f"O imposto total sobre um produto de R$ {preco} é de: R$ {imposto_total:.2f}")

