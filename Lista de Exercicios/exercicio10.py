'''Converter um inteiro informado menor que 32 para sua representação em binário'''

numero = int(input("Informe um numero inteiro"))

if (numero == 0):
    n0 = 0
else:
    n0 = 1
d1 =numero / 2
if (d1 == 0):
    n1 = 0
else:
    n1 = 1
d2 = d1 % 2
if (d2 == 0):
    n2 = 0
else:
    n2 = 1


print(d1, d2)
print(n0, n1, n2)