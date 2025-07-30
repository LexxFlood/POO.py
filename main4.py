
nota1 = float(input("primeira nota:"))
nota2 = float(input("segunda nota:"))

media = (nota1 + nota2)/2

if media > 5:
    print('aprovado')
else:
    print('reprovado')

print(f'Media: {media :.2f}')
