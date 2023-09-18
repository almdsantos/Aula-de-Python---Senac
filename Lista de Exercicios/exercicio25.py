'''Escreva um programa que leia o número equivalente ao mês e imprima a quantidade de
dias deste mês.'''

mes = int(input("Informe o número do mês, sendo:\n1-Janeiro\n2-Fevereiro\n3-Março\n4-Abril\n5-Maio\n6-Junho\n7-Julho\n8-Agosto\n9-Setembro\n10-Outubro\n11-Novembro\n12-Dezembro "))

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    print("Esse mês tem 31 dias")
elif mes == 2:
    print("Esse mês tem 28 dias")
elif mes == 4 or mes == 6 or mes == 9 or mes ==11:
    print("Esse mês tem 30 dias")
else:
    print("Favor informar um mês válido")
    
input("\n\nClique ENTER para finalizar.")