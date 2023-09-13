'''Dado o tamanho da base e da altura de um retângulo, calcular a sua área e o seu
perímetro'''
base = float(input("Informe o valor da Base: "))
altura = float(input("Informe o valor da altura: "))

area = base * altura
perimetro = base + base + altura + altura

print("A área do triangulo é: ", area)
print("O perimetro do triangulo é: ", perimetro)

input()