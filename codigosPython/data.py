import datetime
x = datetime.datetime.now()

nome = input("Qual seu nome ")
dia = x.day
mes = x.strftime("%B")
ano = x.year

print("olá ", nome,"hoje é dia", dia, " do ", mes, "de ", ano)
