'''Em uma certificação são feitos são feitos 5 exames (I, II, III, IV e V). Escreva um
programa que leia as notas destes exames e imprima a classificação do aluno, sabendo
que a média é 70.
Classificação: A – passou em todos os exames;
B – passou em I, II e IV, mas não em III ou V;
C – passou em I e II, III ou IV, mas não em V.
Reprovado – outras situações.'''

examI = float(input("Informe a nota do exame I"))
if examI >= 7.0:
    statusExamI = "aprovado"
else:
    statusExamI = "reprovado"
examII = float(input("Informe a nota do exame II"))
if examII >= 7.0:
    statusExamII = "aprovado"
else:
    statusExamII = "reprovado"
examIII = float(input("Informe a nota do exame III"))
if examI >= 7.0:
    statusExamIII = "aprovado"
else:
    statusExamIII = "reprovado"
examIV = float(input("Informe a nota do exame IV"))
if examIV >= 7.0:
    statusExamIV = "aprovado"
else:
    statusExamIV = "reprovado"
examV = float(input("Informe a nota do exame V"))
if examI >= 7.0:
    statusExamV = "aprovado"
else:
    statusExamV = "reprovado"
    
if statusExamI == "aprovado" and statusExamII == "aprovado" and statusExamIII == "aprovado" and statusExamIV == "aprovado" and statusExamV == "aprovado":
    print("Classificação A - Passou em todos os testes")
elif statusExamI == "aprovado" and statusExamII == "aprovado" and statusExamIV == "aprovado":
    print("Classificação B - Passou em I, II e IV")
elif statusExamI == "aprovado" and statusExamII == "aprovado" and statusExamIII == "aprovado" and statusExamIV == "aprovado":
    print("Classificação C - Passou em I, II, III e IV")
else:
    print("Reprovado")