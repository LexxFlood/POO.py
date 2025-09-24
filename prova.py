from cdb import maior_v

ct = 0
soma_idade = 0
menor_v = 200
maior_v = 0
print("0 para reiniciar")
while True:
    idade = int(input("idade do aluno: "))
    if idade == 0:
        break
    ct = ct + 1
    soma_idade = soma_idade + idade

    if idade < menor_v:
        menor_v = idade

    if idade > maior_v:
         maior_v = idade

    if idade > 30:
        ct_30 += 1

media_idade = soma_idade / ct

print(f"A media das idades é: {media_idade}")
print(f"A menor idade é: {menor_v}")
print(f"O maior valor é: {maior_v}")
print(f"Alunos com idade de 30 anos")

