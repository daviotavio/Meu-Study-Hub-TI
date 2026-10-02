soma_idade = 0
ct_geral = 0
ct_menor_idade = 0
mais_novo = 999999
mais_velho = -999999

for numero in range(1,7):
    idade = int(input('Idade do aluno: '))
    soma_idade += idade
    ct_geral += 1
    if idade < mais_novo:
        mais_novo = idade
    if idade > mais_velho:
        mais_velho = idade
    if idade >= 18:
        ct_menor_idade += 1

media = soma_idade / ct_geral
print(f'soma das idades {soma_idade}')
print(f'Média aritmética das idades {media}')
print(f'Idade do aluno mais novo {mais_novo}')
print(f'Idade do aluno mais velho {mais_velho}')
print(f'Alunos maiores de idade {ct_menor_idade}')
