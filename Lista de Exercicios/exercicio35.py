'''Escreva um programa que leia um número inteiro de 1 a 7 e informe o dia da semana
correspondente, sendo domingo o dia de número 1. Se o número não corresponder a um
dia da semana, mostre uma mensagem de erro.'''

dia = int(input("Informe um numero até 7:  "))

if dia == 1:
    print("Domingo")
elif dia == 2:
    print("Segunda Feira")
elif dia == 3:
    print("Terça Feira")
elif dia == 4:
    print("Quarta Feira")
elif dia == 5:
    print("Quinta Feira")
elif dia == 6:
    print("Sexta Feira")
elif dia == 7:
    print("Sabado")
else:
    print("Informe o número corretamente")
    
input("\n\nClique ENTER para finalizar.")