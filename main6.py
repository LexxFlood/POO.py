Compra = int(input('compra:'))
Venda = int(input('venda:'))

if Compra > Venda:
    print('Prejuízo')
elif Compra < Venda:
    print('Lucro')
else:
    print('Valores iguais')
