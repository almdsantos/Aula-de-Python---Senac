'''import random

print('random.randrage(100): ', random.randrange(100))
print('random.randrage(50,100): ', random.randrange(50,100))
print('random.choice([20,5,10,15,54]): ', random.choice([20, 5, 10, 15, 54]))
print('random.random(): ', random.random())
print('random.randint(30,60): ', random.randint(30,60))'''

#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#

'''escola = 'taboão da serra'

print(escola)
print(escola[3])
print(len(escola))
print(escola.count("a"))
print(escola.find('a'))
print(escola.upper())
print(escola.lower())
print(escola.capitalize())
print(escola.strip())
print(escola.title())
print(escola.isalpha())
print(".".join(escola))
print(escola.replace('serra', 'treva'))
print(escola.split(" "))
print(escola[0:4])'''

#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#

'''A = int(input("Informe um número para a variavel A:"))
B = int(input("Informe um número para a variavel B:"))

X = A + B

if X >= 10:
    print('O valor calculado é maior que 10, sendo', X)
else:
    print('O valor calculado é menor que 10, sendo', X)'''

#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#

'''nht = float(input("Informe a quantidade de horas trabalhadas"))
vph = float(input("Informe o valor pago por hora"))
ptd = float(input("Informe o percentual de desconto"))
sb = nht*vph
desconto = sb * (ptd/100)
sl = sb – desconto

print("O Valor de Salário Bruto é", sb)
print("O Valor de Salário Liquido é",sl)'''

#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#

nht = float(input("Informe a quantidade de horas trabalhadas"))
vph = float(input("Informe o valor pago por hora"))

salarioBruto = nht * vph

if salarioBruto < 1000:
    desconto = salarioBruto*0.05

elif salarioBruto >= 1000 and 2000:
    desconto = salarioBruto*0.10

else:
    desconto = salarioBruto*0.15

salarioLiquido = salarioBruto - desconto

print("O salário recebido é de: ", salarioBruto, "reais")
print("Com desconto de 10", desconto, "reais")
print("O salário liquido é de ", salarioLiquido, "reais")