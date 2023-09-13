'''Ler dois números inteiros e exibir o quociente e o resto da divisão inteira entre eles.'''

numero1 = int(input("Informe um número"))
numero2 = int(input("Informe um número"))

resultado = numero1 / numero2
resto = numero1 % numero2

print("O resultado de", numero1, "dividido por", numero2, "é igual a:", resultado, "e o resto é", resto)

input("\n\nClique ENTER para finalizar.")