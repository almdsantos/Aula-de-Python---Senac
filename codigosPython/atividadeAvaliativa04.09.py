'''print("Vamos Calcular o IMC?")
peso = float(input("Informe o seu peso"))
altura = float(input("Informe a sua altura"))

imc = peso / (altura*altura)

if imc < 18.5:
    print("Abaixo do Peso")
elif imc >= 18.5 and imc <= 24.9:
    print("Peso Normal")
elif imc >= 25.0 and imc <= 29.9:
    print("Pré Obesidade")
elif imc >= 30.0 and imc <= 34.9:
    print("Obesidade Grau 1")
elif imc >= 35.0 and imc <= 39.9:
    print("Obesidade Grau 2")
else:
    print("Obesidade Grau 3")
print(imc)'''