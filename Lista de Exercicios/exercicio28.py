'''Escreva um programa que leia uma letra e mostre se ela é vogal ou consoante.'''

letra = input("Qual letra você deseja consultar ")
letra = letra.lower()

if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print("A letra é vogal")
else:
    print("A letra é uma consoante")

input("\n\nClique ENTER para finalizar.")