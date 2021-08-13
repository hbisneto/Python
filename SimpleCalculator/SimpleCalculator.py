from datetime import date
AnoAtual = date.today().year
SoftwareName = "SIMPLE CALCULATOR"

print("Nome:", SoftwareName)
print("Versão: 1.0")
print("Criado por: Heitor Bisneto")
print("Copyright © 2020 -", AnoAtual, "Bisneto. All rights reserved.")
print("")

Number = float(input("Digite o primeiro número: "))
Number2 = float(input("Digite o segundo número: "))

print("")
print("#" * 30)
print("+ para soma")
print("- para subtração")
print("* para multiplicação")
print("/ para divisão")
print("#" * 30)
print("")

Operator = str(input("Digite o operador: "))

if Operator == "+":
    Result = (Number + Number2)
elif Operator == "-":
    Result = (Number - Number2)
elif Operator == "*":
    Result = (Number * Number2)
else:
    Result = (Number / Number2)
print("")

print("Resultado:", Result)
