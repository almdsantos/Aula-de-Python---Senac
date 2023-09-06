f = float(input("Informe um número "))
cont = 1
r = 1

if f < 0:
    print("Favor informar um número válido")
elif f <= 1:
    print("Resultado do fatorial igual a 1")
else:
    while cont <= f:
        r = r * cont
        cont= cont + 1

print (r)