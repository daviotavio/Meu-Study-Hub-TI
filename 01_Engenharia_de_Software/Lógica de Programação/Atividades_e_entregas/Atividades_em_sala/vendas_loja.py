nomeProduto = str(input("Digite o nome do produto: "))
valorCompra = float(input("Digite o valor de compra do produto: "))
valorVenda = float(input("Digite o valor de venda do produto: "))
lucro = 0
prejuizo = 0
if valorCompra > valorVenda:
    prejuizo = valorVenda - valorCompra
    print("O valor de compra do produto", nomeProduto, "é: R$", valorCompra, "e o valor de venda é: R$", valorVenda, "portanto, houve prejuízo de: R$", prejuizo)
elif valorVenda > valorCompra:
    lucro = valorVenda - valorCompra
    print("O valor de venda do produto", nomeProduto, "é: R$", valorVenda, "e o valor de compra é: R$", valorCompra, "portanto, houve lucro de: R$", lucro)
else:
    print("Os valores R$", valorCompra, "e R$", valorVenda, "são iguais!")