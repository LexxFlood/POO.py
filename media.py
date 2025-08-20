media = 0
ct = 0
soma = 0
for i in range(1, 5+1, 1):
    nota = float(input('Nota do aluno: '))
    ct = ct + 1
    soma = soma + nota

media = soma / ct
print("\nMedia da turma = ", media)