'''Faça um algoritmo para calcular a nota semestral de um aluno. A nota semestral é obtida 
pela média aritmética entre a nota de 2 bimestres. Cada nota de bimestre é composta por 
2 notas de provas. '''


nota1 = float(input("Informe a a nota da sua primeira prova do 1º Bimestre. "))
nota2 = float(input("Informe a a nota da sua segunda prova do 1º Bimestre. "))

nota3 = float(input("Informe a a nota da sua primeira prova do 2º Bimestre. "))
nota4 = float(input("Informe a a nota da sua segunda prova do 2º Bimestre. "))

bimestre1 = nota1 + nota2
bimestre2 = nota3 + nota4

semestre = (bimestre1 + bimestre2) / 4

if (semestre <= 5 ):
    print("\n\nA junção das suas notas lhe deu uma média de: %.2f" % semestre)
    print("\nVocê foi REPROVADO")
else:
    print("\n\nA junção das suas notas lhe deu uma média de: %.2f" % semestre)
    print("\nVocê foi APROVADO")

input("\n\nClique ENTER para finalizar.")