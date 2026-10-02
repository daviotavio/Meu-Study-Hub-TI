import random

ct1 = 0
ct2 = 0
ct3 = 0
ct4 = 0
ct5 = 0
ct6 = 0

print('MEGA-SENA')

for numeros in range(1,60+1):
    sorteio = random.randint(1,6)
    if sorteio == 1:
        ct1 += 1
    elif sorteio == 2:
        ct2 += 1
    elif sorteio == 3:
        ct3 += 1
    elif sorteio == 4:
        ct4 += 1
    elif sorteio == 5:
        ct5 += 1
    elif sorteio == 6:
        ct6 += 1
    print(sorteio)

print(f'O numero 1 foi sorteado {ct1} vezes')
print(f'O numero 2 foi sorteado {ct2} vezes')
print(f'O numero 3 foi sorteado {ct3} vezes')
print(f'O numero 4 foi sorteado {ct4} vezes')
print(f'O numero 5 foi sorteado {ct5} vezes')
print(f'O numero 6 foi sorteado {ct6} vezes')