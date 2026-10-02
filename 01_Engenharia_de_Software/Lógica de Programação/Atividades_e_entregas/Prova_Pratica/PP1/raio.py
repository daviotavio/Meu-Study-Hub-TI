# Enunciado: 1.	Implemente o programa que calcule o volume de uma esfera de raio R. O usuário fornecerá o dado necessário.
# Onde: volume = 4/3 * pi * r3

# Obs: não utilizei IA

raio = float(input('Digite o raio para descobrir o volume de uma esfera: '))
pi = 3.14159
volume = ((4/3)*(pi))*raio**3

print(f'O volume da esfera cujo raio é {raio} é {volume:.2f}')
