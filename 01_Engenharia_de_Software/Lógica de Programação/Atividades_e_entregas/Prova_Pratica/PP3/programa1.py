quantidade = 0
soma = 0
maior = float('-inf')
menor = float('inf')
maiores_50 = 0

while True:
    valor = float(input("Digite um valor (ou número negativo para sair): "))
    
    if valor < 0:
        break
    
    quantidade += 1
    soma += valor
    
    if valor > maior:
        maior = valor
    
    if valor < menor:
        menor = valor
    
    if valor >= 50:
        maiores_50 += 1

if quantidade > 0:
    media = soma / quantidade
    print(f"\nQuantidade de valores: {quantidade}")
    print(f"Soma dos valores: {soma}")
    print(f"Média aritmética: {media}")
    print(f"Maior valor: {maior}")
    print(f"Menor valor: {menor}")
    print(f"Valores >= 50: {maiores_50}")
else:
    print("Nenhum valor foi digitado.")
