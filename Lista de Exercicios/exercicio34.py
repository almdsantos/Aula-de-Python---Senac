'''Uma financeira usa o seguinte critério para conceder empréstimos: o valor total do
empréstimo deve ser até dez vezes o valor da renda mensal do solicitante e o valor da
prestação deve ser no máximo 30% da renda mensal do solicitante. Escreva um programa
que leia a renda mensal de um solicitante, o valor total do empréstimo solicitado e o
número de prestações que o solicitante deseja pagar e informe se o empréstimo pode ou
não ser concedido.'''

renda = float(input("Nos informe qual a sua renda mensal"))
empr = float(input("Qual o valor o senhor deseja financiar"))
parc = int(input("Em quantas parcelas quer pagar?"))

criterio1 = renda * 10
prestacao = renda * 0.30

if empr <= criterio1:
    print("Valor de R$%.2f" % empr, "aprovado")
    print("Parcelas de R$ %.2f" % prestacao,", em", parc, "parcelas" )
else:
    print("O valor solicitado não se enquadra nas condições do banco")

input("\n\nClique ENTER para finalizar.")