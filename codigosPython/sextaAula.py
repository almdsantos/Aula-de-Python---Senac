def soma(numero1, numero2):
    print(numero1 + numero2)
def subtracao(numero1, numero2):
    print(numero1 - numero2)
def multiplicacao(numero1, numero2):
    print(numero1 * numero2)
def divisao(numero1, numero2):
    print(numero1 / numero2)

opcao = int(input("Qual operação deseja realizar? 1 - Soma; 2 - Subtração; 3 - Multiplicação; 4 - Divisão\n\n"))

if(opcao >= 5):
    print("Informe uma operação válida")
elif(opcao <= 0):
    print("Informe uma operação válida")
else:
    numero1 = float(input("Informe o primeiro valor\n"))
    numero2 = float(input("Informe o segundo valor\n"))
    if(opcao == 1):
        soma(numero1, numero2)
    elif(opcao == 2):
        subtracao(numero1, numero2)
    elif(opcao == 3):
        multiplicacao(numero1, numero2)
    else:
        divisao(numero1, numero2)