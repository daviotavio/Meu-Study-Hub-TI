print('Crescente ou decrescente dependendo das entradas: ')

valor_inicial = int(input('Digite o valor inicial: '))
valor_final = int(input('Digite o valor final: '))
contador = 0

if valor_inicial == valor_inicial:
    print('Os valores são iguais')

if valor_inicial < valor_final:
    print('Valores em ordem crescente')
    for numero in range(valor_inicial, valor_final+1, 1):
        contador += 1
        print(numero)


else:
    print('Valores em ordem descrescente')
    for numero in range(valor_inicial, valor_final-1, -1):
        contador += 1
        print(numero)


print(f'Foram gerados {contador} números')
