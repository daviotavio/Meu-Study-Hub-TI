# 3.Construa o programa que calcule a média aritmética dos números pares e a média aritmética dos números ímpares.
# O usuário fornecerá os valores de entrada que pode ser um número qualquer par ou ímpar. ok
# A condição de saída será o número 0 (zero). ok
# Na tela de saída, mostre também a quantidade total de números digitados e a soma total de números digitados. ok

soma_pares = 0
soma_impares = 0
contador = 0
contador_pares= 0
contador_impares = 0
soma_total = 0
media_aritmetica_pares = 0
media_aritmetica_impares = 0

print('Digite números inteiros (digite 0 para sair):')

while True:
    numero = int(input('Número: '))
    if numero == 0:
        break
    if numero % 2 == 0:
        print('Você digitou um número par')
        soma_pares += numero
        contador_pares += 1
        media_aritmetica_pares = soma_pares / contador_pares

    else:
        print('Você digitou um número ímpar')
        soma_impares += numero
        contador_impares += 1
        media_aritmetica_impares = soma_impares / contador_impares

    contador += 1
    soma_total = soma_pares + soma_impares

print(f'A média aritmética dos números pares digitados é: {media_aritmetica_pares}')
print(f'A média aritmética dos números ímpares digitados é: {media_aritmetica_impares}')
print(f'A quatidade total de números digitados é: {contador}')
print(f'A soma dos números digitados é: {soma_total}')


