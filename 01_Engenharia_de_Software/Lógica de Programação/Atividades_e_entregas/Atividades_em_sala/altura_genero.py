qtd_genero_m = 0
qtd_genero_f = 0
maior_altura = 0
menor_altura = 3

while True:
    altura = float(input('Digite a altura em metros. (0 para sair): '))
    if altura == 0:
        break
    genero = str(input('\nDigite seu gênero. M para masculino e F para feminino\n'))
    if altura < menor_altura:
        menor_altura = altura
    if altura > maior_altura:
        maior_altura = altura
    if genero == 'M':
        qtd_genero_m += 1
    if genero == 'F':
        qtd_genero_f += 1

print(f'A maior altura do grupo é: {maior_altura}')
print(f'O menor altura do grupo é: {menor_altura}')
print(f'A quantidade de homens é: {qtd_genero_m}')
print(f'A quantidade de mulheres é: {qtd_genero_f}')