contador = 0
numero = int(input('Digite o número: '))

for numeros in range(numero,0,-1):
    print(numeros)
    contador += 1
print(f'A quantidade de números foi: {contador}')