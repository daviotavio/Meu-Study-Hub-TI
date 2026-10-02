from struct import pack_into

valor1 = int(input("Digite o primeiro número: "))
valor2 = int(input("Digite o segundo número: "))

if valor1 > valor2:
    print("O número: ", valor1, " é maior que o número: ", valor2)
elif valor2 > valor1:
    print("O número: ", valor2, " é maior que o número: ", valor1)
else:
    print("Os valores", valor1, "e", valor2, "são iguais!")