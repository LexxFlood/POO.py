ct = 0
soma = 0
print("Digite [-1] para sair da repetição")
Disciplina = str(input("Digitre o nome da disciplina:"))
while True:
    nota = int(input("Digite uma nota: "))
    if nota == -1:
        break

    ct = ct + 1
    soma = soma + nota
    media = soma/ct

print("Media:", media)
print("N de alunos:", ct)
print("Soma das notas:", soma)
print("Disciplina", Disciplina)
