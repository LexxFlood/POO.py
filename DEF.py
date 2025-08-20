def calculo_dobro(p_valor):
    dobro = p_valor * 2
    return dobro

if __name__== '__main__':
valor = int(input("valor inteiro: "))
v_retornado = calculo_dobro(valor)
print("valor retornado pela função:", v_retornado)

print("valor retornado pela função:", calculo_dobro(valor))