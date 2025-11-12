from geo import FormaGeometrica, Quadrado

print("Geral")
try:
    f = FormaGeometrica("vermelho")
except TypeError as e:
    print("Erro esperado:", e)

print("\nTeste com a subclasse concreta")
q1 = Quadrado("azul", 5)
print(f"Cor: {q1.get_cor()}")
print(f"Lado: {q1.get_lado()}")
print(f"Área: {q1.area()}")
print(f"Perímetro: {q1.perimetro()}")

q1.set_cor("verde")
print(f"\nCor alterada: {q1.get_cor()}")

q2 = Quadrado("amarelo")
print(f"\nQuadrado 2 - Cor: {q2.get_cor()}, Lado: {q2.get_lado()}")
print(f"Área: {q2.area()}, Perímetro: {q2.perimetro()}")
