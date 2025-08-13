menor_v = float('inf')
maior_v = float('-inf')
print("Digite [0] para sair da repetição")
while True:
    valor = int(input("Digite um valor: "))
    if valor == 0:
        break
    if valor < menor_v:
        menor_v = valor
    if valor > maior_v:
        maior_v = valor

print("\nMenor valor = ", menor_v)
print("\nMaior valor = ", maior_v)





