#4.	Elabore o programa que simule uma calculadora com as quatro operações aritméticas básicas.
# O usuário fornecerá dois números e a operação aritmética desejada.
# Mostre o menu com estes símbolos (+ , - , * , / ) para o usuário escolher a operação aritmética.
# Utilize o comando “se . . . senão . . . ” encadeado, ou seja, “if . . . else . . . ” encadeado. 

# Obs: não utilizei IA

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

print('Escolha a operação que deseja realizar digitando algum dos caracteres abaixo:')
print('+ para adição, - para subtração, * para multiplicação, / para divisão')

operacao = input("Digite o símbolo da operação desejada: ")

if operacao == '+':
    resultado = numero1 + numero2
    print(f"O resultado da soma é: {resultado}")
elif operacao == '-':
    resultado = numero1 - numero2
    print(f"O resultado da subtração é: {resultado}")
elif operacao == '*':
    resultado = numero1 * numero2
    print(f"O resultado da multiplicação é: {resultado}")
elif operacao == '/':
    resultado = numero1 / numero2
    print(f"O resultado da divisão é: {resultado}")
else:
    resultado = "Operação inválida"

