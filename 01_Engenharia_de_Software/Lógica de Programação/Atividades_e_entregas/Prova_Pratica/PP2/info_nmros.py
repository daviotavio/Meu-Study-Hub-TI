# - Implemente:

# 1.	Desenvolva o programa que leia vários valores reais e no final mostre as seguintes informações:
# A quantidade de valores digitados;
# A soma dos valores digitados;
# A média aritmética dos valores digitados;
# E a quantidade de valores digitados maior que 20.

# contador
qtd_valor_digitado = 0
soma_vlrs = 0
qtd_maior20 = 0


print('Digite alguns valores')
print("Para sair da repetição, digite '-1'")

while True:
    valores = float(input('Valor:'))
    if valores == -1:
        break
    qtd_valor_digitado += 1
    soma_vlrs += valores
    if valores > 20:
        qtd_maior20 = qtd_maior20 + 1

media = soma_vlrs / qtd_valor_digitado

print(f'A quantidade de valores digitados: {qtd_valor_digitado}')
print(f'A soma de valores digitados: {soma_vlrs}')
print(f'A média aritmética dos valores digitados: {media}')
print(f'A quantidade de valores digitados maior que 20: {qtd_maior20}')