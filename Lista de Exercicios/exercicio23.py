'''Escreva um programa que leia um número e imprima se este número é ou não par.'''

numero = int(input("Informe um número"))

modulo = numero % 2

if modulo == 0:
    print("Esse número é par")
else:
    print("Esse número não é par")
    
input("\n\nClique ENTER para finalizar.")