#Implemente o programa que leia a nota de vários alunos de uma turma e gere uma tela de saída com as seguintes informações:
# a quantidade de alunos que fizeram a prova
# a quantidade de alunos aprovados
# a quantidade de alunos reprovados
# a média da turma.
# Considere que o aluno será aprovado com nota for maior ou igual a cinco.

nota = 0
qtd_alunos = 1
qtd_aprovados = 0
qtd_reprovados = 0
soma_nota = 0

print('Digite as notas dos alunos e -1 para parar o loop')


while True:
    nota = float(input(f'Nota aluno {qtd_alunos}: '))

    if nota == -1:
        break

    if nota > 10:
        print('A nota deve ser entre 0 e 10')
        continue

    if nota >= 5:
        qtd_aprovados += 1
    else:
        qtd_reprovados += 1

    soma_nota += nota
    qtd_alunos += 1

media_turma = soma_nota / qtd_alunos

print(f'Quantidade de alunos que fizeram a prova: {qtd_alunos -1}')
print(f'Quantidade de alunos aprovados: {qtd_aprovados}')
print(f'Quantidade de alunos reprovados: {qtd_reprovados}')
print(f'Média da turma: {media_turma:.2f}')
