'''Num dia de sol, você deseja medir a altura de um prédio, porém, a trena não é 
suficientemente longa. Assumindo que seja possível medir sua sombra e a do prédio no 
chão, e que você lembre da sua altura, faça um programa para ler os dados necessários e 
calcular a altura do prédio.'''

tamanhoPessoa = float(input("Informe a sua altura "))
sombraPessoa = float(input("Informe o tamanho da sua sombra "))
sombraPredio = float(input("Informe o tamanho da sombra do prédio "))

'''Aqui é a porcentagem necessário para calcularmos o prédio'''
A = sombraPessoa*100
B = A / tamanhoPessoa

'''Aqui nós calculamos o tamanho do prédio'''
C = sombraPredio*100
D = C / B

print("O tamanho do prédio é de: %.2f" % D)

input("\n\nClique ENTER para finalizar.")