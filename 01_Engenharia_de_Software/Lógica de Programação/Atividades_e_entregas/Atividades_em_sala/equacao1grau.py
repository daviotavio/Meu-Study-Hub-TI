valorA = int(input("Digite o valor de A: "))
valorB = int(input("Digite o valor de B: "))

if valorA == 0:
    print('Não posso dividir por zero')
else:
    raiz = -valorB / valorA
    print('Raiz =', raiz)
