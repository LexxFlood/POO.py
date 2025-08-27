def soma (a, b):
    return a + b

def subtração (a, b):
    calculo = a - b
    return calculo

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
opção = str(input('Digite (+) para somar\n Digite (-) para subtrair\n Opção: '))

if opção == "+":
    print('A soma é: ', soma(a, b))
elif opção == "-":
    print('A subtração é: ', subtração(a, b))
else:
    print("Opção inválida")




