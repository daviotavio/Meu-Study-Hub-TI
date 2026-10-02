print('Média aritmética alunos')

contador = 0
contador_aprovados = 0
contador_reprovados = 0
soma = 0

for aluno in range(1,10+1,1):
    notas_alunos = float(input(f'Digite a nota do aluno {aluno}: '))
    contador += 1
    soma += notas_alunos
    if notas_alunos >= 5:
        contador_aprovados += 1
    else:
        contador_reprovados += 1

media = soma / contador
print(f'Média da turma: {media}')
print(f'Alunos aprovados: {contador_aprovados}')
print(f'Alunos reprovados: {contador_reprovados}')
