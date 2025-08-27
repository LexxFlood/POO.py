def maximo (X, Y):
    if X > Y:
        maior = X
    else:
        maior = Y
    return maior

X = int(input("Primeiro numero: "))
Y = int(input("Segundo numero: "))

print("Maior valor: ", maximo(X, Y))
