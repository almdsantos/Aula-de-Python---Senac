'''Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool                  Até 25 litros, desconto de 2% por litro
                        Acima de 25 litros, desconto de 4% por litro

Gasolina                Até 25 litros, desconto de 3% por litro
                        Acima de 25 litros, desconto de 5% por litro
                        
Escreva um algoritmo que leia o número de litros vendidos e o tipo de combustível
(codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser
pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,70 e o preço do litro
do álcool é R$ 1,90.'''

tipo = int(input("Informe o combustivel que pretende usar, sendo\n1 - Gasolina\n2 - Alcool "))
if tipo <= 0 or tipo >= 3:
    print("Informe o combustivel a ser usado corretamente!")
else:
    qtd = int(input("Quer abastecer quantos litros?"))
    
    if tipo == 1:
        if qtd <= 24.99:
            desconto = 2.70 * 0.03
            total = (qtd * 2.70) - (qtd * desconto)
            print("A gasolina saiu por R$ %.2f" % total)
        if qtd > 25:
            desconto = 2.70 * 0.05
            total = (qtd * 2.70) - (qtd * desconto)
            print("A gasolina saiu por R$ %.2f" % total)
        else:
            print("Informe uma quantidade válida")
    else:
        if qtd <= 24.99:
            desconto = 1.90 * 0.03
            total = (qtd * 1.90) - (qtd * desconto)
            print("O alcool saiu por R$ %.2f" % total)
        if qtd > 25:
            desconto = 1.90 * 0.05
            total = (qtd * 1.90) - (qtd * desconto)
            print("O alcool saiu por R$ %.2f" % total)
        else:
            print("Informe uma quantidade válida")
            
input("\n\nClique ENTER para finalizar.")