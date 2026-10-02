# 3.	Construa o programa que tendo como dados de entrada dois pontos quaisquer do plano cartesiano, P(x1, y1) e Q(x2, y2), calcule a distância entre eles.
# Use a seguinte fórmula: √((x_2-〖x_1)〗^2+〖(y_2-〖y_1〗_ )〗^2 )
# Obs: não utilizei IA

x1 = int(input("Digite o x do primeiro ponto: "))
y1 = int(input("Digite o y do primeiro ponto: "))
x2 = int(input("Digite o x do segundo ponto: "))
y2 = int(input("Digite o y do segundo ponto: "))

distancia = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

print(f"A distância é: {distancia}")