# A água é um nutriente essencial. Sem ela, o corpo não pode funcionar com perfeição.
# Cada pessoa precisa de uma quantidade diferente de água para hidratar o corpo.
# A dose ideal, ou seja, a necessidade diária em litros é calculada através da fórmula: massa (em kg) vezes 0,03.
# Elabore o programa que realize esse cálculo.

# Obs: não utilizei IA

massa = float(input("Digite a massa do corpo (em kg): "))
calculo = massa * 0.03
print(f"A massa do corpo é {massa} kg.")
print(f"A quantidade de água necessária é {calculo:.2f} L.")