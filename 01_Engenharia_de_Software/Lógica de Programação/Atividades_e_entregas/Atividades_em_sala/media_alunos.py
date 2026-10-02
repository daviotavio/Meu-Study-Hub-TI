contador = 0
soma = 0


print('MÉDIA ARITMÉTICA DA TURMA')
materia = str(input('Digite o nome da matéria: '))
print('Digite [-1] para sair da repetição')
while True:
    nota = float(input('Digite uma nota: '))
    if nota == -1:
        break
    contador = contador + 1
    soma = soma + nota
media_aritmetica = soma / contador
print('\nQuantidade de notas digitados', contador)
print('A matéria em questão é', materia)
print('Soma das notas', soma)
print(f"Média aritmética: {media_aritmetica:.2f}")