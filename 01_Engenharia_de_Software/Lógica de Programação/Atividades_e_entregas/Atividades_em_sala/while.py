contador = 0
soma = 0

print('Digite [-1] para sair da repetição')
while True:
    numero = int(input('Digite um número: '))
    if numero == -1:
        break
    contador = contador + 1
    soma = soma + numero
print('\nQuantidade de números digitados', contador)
print('Soma', soma)