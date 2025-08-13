ct = 0
soma = 0
print("Digite [-1] para sair da repetição")
while True:
    numero = int(input("Digite um número: "))
    if numero == -1:
        break

    soma = soma + numero
    ct = ct + 1
print("Numero digitados:", ct)
print("soma dos valores digitados", soma)