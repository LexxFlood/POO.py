def soma(a, b):
    return a + b

def subtração(a, b):
    calculo = a - b
    return calculo

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
opção = int(input('Digite (1) para somar\n Digite (2) para subtrair\n Opção: '))

if opção == 1:
    print('A soma é: ', soma(a, b))
else:
    print('A subtração é: ', subtração(a, b))




