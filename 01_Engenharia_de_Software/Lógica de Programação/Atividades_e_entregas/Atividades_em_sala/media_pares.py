contador = 0
soma = 0
contador_geral = 0

print('MÉDIA ARITMÉTICA DOS NUMEROS PARES')
print('Digite [0] para sair da repetição')

while True:
    nota = float(input('Digite uma nota: '))
    if nota == 0:
        break
    if nota % 2 == 0:
        soma = soma + nota
        contador = contador + 1
    contador_geral = contador_geral + 1

media_aritmetica = soma / contador  

print('\nQuantidade de notas pares digitados', contador)
print('\nQuantidade de notas digitados', contador_geral)
print('Soma das notas pares', soma)
print(f"Média aritmética: {media_aritmetica:.4f}")