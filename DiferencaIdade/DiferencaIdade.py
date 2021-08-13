from datetime import date
AnoAtual = date.today().year
SoftwareName = "DIFERENCA DE IDADE"
Version = "1.0"
CopyrightName = "Heitor Bisneto."

print("Nome:", SoftwareName)
print("Versão:", Version)
print("Criado por:", CopyrightName)
if AnoAtual == 2020:
    print("Copyright ©", AnoAtual, "|", CopyrightName, "All rights reserved.")
else:
    print("Copyright © 2020 -", AnoAtual, "|", CopyrightName, "All rights reserved.")
print("")

Nome = str(input(">>> Insira o seu nome: "))
NomeSegundaPessoa = str(input(">>> Insira o nome da segunda pessoa: "))
Nascimento = int(input(">>> Em que ano você nasceu: "))
NascimentoSegundaPessoa = int(input(">>> Em que ano a segunda pessoa nasceu: "))

if Nascimento < NascimentoSegundaPessoa:
    Calc = (Nascimento - NascimentoSegundaPessoa)
    if Calc < 0:
        Calc = Calc * (-1)
    if Calc == 1:
        print(">>> ", Nome, "é", Calc, "ano mais velho(a) que", NomeSegundaPessoa)
    else:
        print(">>> ", Nome, "é", Calc, "anos mais velho(a) que", NomeSegundaPessoa)
elif Nascimento > NascimentoSegundaPessoa:
    Calc = (Nascimento - NascimentoSegundaPessoa)
    if Calc < 0:
        Calc = Calc * (-1)
    if Calc == 1:
        print(">>> ", NomeSegundaPessoa, "é", Calc, "ano mais velho(a) que", Nome)
    else:
        print(">>> ", NomeSegundaPessoa, "é", Calc, "anos mais velho(a) que", Nome)
else:
    print(">>> Vocês têm a mesma idade!")
