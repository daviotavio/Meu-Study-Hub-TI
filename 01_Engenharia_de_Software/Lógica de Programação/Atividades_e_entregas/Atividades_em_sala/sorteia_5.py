import random

print('Sorteia 5 números aleatórios')

for numeros in range(1,11,1):
    numero_sorteado = random.randint(-3,3)
    print(numero_sorteado)

print('fim do programa')