'''Dado que a fórmula para conversão de Fahrenheit para Celsius é C = 5/9 (F – 32), leu um 
valor de temperatura em Fahrenheit e exibi-lo em Celsius'''

F = float(input("Qual a temperatura em Fahrenheit "))

C = 5/9 * (F - 32)

print("O valor em Celsius é: %.2f" % C)

input("\n\nClique ENTER para finalizar.")