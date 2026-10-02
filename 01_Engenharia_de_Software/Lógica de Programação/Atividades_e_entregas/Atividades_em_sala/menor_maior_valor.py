menor_valor = 999999999
maior_valor = 0
qtd_valores = 0
soma_valores = 0
media_aritmetica = 0
maior_10 = 0

print('Digite valores inteiros e o sistema encontrará o menor valor. Digite [0] para sair\n')

while True:
    valor = int(input('Digite os valores inteiros:'))
    if valor == 0:
        print('\n--------Você encerrou o programa------------------------------\n')    
        break
    if valor < menor_valor:
        menor_valor = valor
    if valor > maior_valor:
        maior_valor = valor
    if valor > 10:
        maior_10 += 1
    print(menor_valor)  
    print(maior_valor)

    qtd_valores += 1
    soma_valores += valor
    media_aritmetica = soma_valores / qtd_valores

print(f'O menor valor digitado é {menor_valor}')
print(f'O maior valor digitado é {maior_valor}')
print(f'A quantidade de números digitados é {qtd_valores}')
print(f'A soma dos valores digitados é {soma_valores}')
print(f'A média aritmética dos valores digitados é {media_aritmetica}')
print(f'A quantidade de valores maiores que 10 é {maior_10}')