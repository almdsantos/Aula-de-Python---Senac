'''Escreva um programa que leia um número e exiba se ele é positivo ou negativo.'''

numero = int(input("Informe um número para verificação: "))

divisor = numero % 2

if divisor == 0:
    print("O número é par")
else:
    print("O número é impar")
    
input("\n\nClique ENTER para finalizar.")