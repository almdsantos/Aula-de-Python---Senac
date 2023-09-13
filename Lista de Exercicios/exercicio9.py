'''Faça um algoritmo que calcule e apresente o valor do volume de uma lata de óleo, dado 
seu raio e sua altura'''

import math

raio = float(input("Informa o raio"))
altura = float(input("Informe a altura"))

volume = raio*math.pi*(raio**2)*2

print(volume)

input("\n\nClique ENTER para finalizar.")