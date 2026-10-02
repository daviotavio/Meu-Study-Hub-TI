salario_minimo = float(input("Digite o valor do salário mínimo: "))

menores_5 = 0
faixa_5_10 = 0
maiores_10 = 0
folha_total = 0

while True:
    salario = float(input("Digite o salário do funcionário (ou -1 para sair): "))
    
    if salario == -1:
        break
    
    folha_total += salario
    
    salarios_minimos = salario / salario_minimo
    
    if salarios_minimos < 5:
        menores_5 += 1
    elif salarios_minimos < 10:
        faixa_5_10 += 1
    else:
        maiores_10 += 1

print(f"\nFuncionários com menos de 5 salários mínimos: {menores_5}")
print(f"Funcionários de 5 a menos de 10 salários mínimos: {faixa_5_10}")
print(f"Funcionários com 10 ou mais salários mínimos: {maiores_10}")
print(f"Total da folha de pagamento: {folha_total}")
