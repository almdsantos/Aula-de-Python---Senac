'''Escreva um programa que calcula o desconto previdenciário de um funcionário. Dado um 
salário, o programa deve retornar o valor do desconto proporcional ao mesmo. O cálculo 
segue a regra: o desconto é de 11% do valor do salário, entretanto, o valor máximo de 
desconto é 334,29, o que seja menor.'''

salario = float(input("Informe o valor do seu salário"))
descontoMaximo = 334.29
desconto = salario * 0.11

if (desconto > descontoMaximo):
    salarioLiquido = salario - descontoMaximo
    print("O salário bruto com desconto de %.2f" % descontoMaximo, "da um total de %.2f" % salarioLiquido)
else:
    salarioLiquido = salario - desconto
    print("O salário bruto com desconto de %.2f" % desconto, "da um total de %.2f" % salarioLiquido)

input("\n\nClique ENTER para finalizar.")