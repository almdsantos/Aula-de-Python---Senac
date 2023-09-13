'''Dado o tamanho do raio de uma circunferência, calcular a área e o perímetro da mesma'''
import math

raio = float(input("Qual a medida do raio"))

a = math.pi*(raio*raio)
p = 2*math.pi*raio

print("O perimetro da circuferencia é:%.2f"% p, "e a area é:%.2f"% a)

input("\n\nClique ENTER para finalizar.")