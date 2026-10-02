print('User digita valor inicial e final da sequencia: ')

valor_inicial = int(input('Digite o valor inicial: '))
valor_final = int(input('Digite o valor final: '))
contador = 0

for numero in range(valor_inicial,valor_final+1,1):
    contador += 1
    print(numero)

print(f'Foram gerados {contador} numeros')
print('fim do programa')