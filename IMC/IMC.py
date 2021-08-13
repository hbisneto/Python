from datetime import date
AnoAtual = date.today().year
SoftwareName = "IMC"
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

Nome = str(input("Qual o seu nome: "))
Altura = float(input("Insira a sua altura (use ponto ao inves de virgula): "))
Peso = float(input("Insira o seu peso (use ponto ao inves de virgula): "))
print()

IMC = Peso / (Altura * Altura)

#Formatação - Maneira 1 (Usando duas casas decimais depois do ponto):
print(f"IMC - (Formato #.##): {IMC:.2f}")
#Formatação - Maneira 2 (Usando três casas decimais depois do ponto):
print("IMC - (Formato #.###): {:.3f}".format(IMC))
print()

if IMC < 17:
    print("Conclusão: Muito abaixo do peso")
elif IMC >= 17 and IMC < 18.5:
    print("Conclusão: Abaixo do peso")
elif IMC >= 18.5 and IMC < 25:
    print("Conclusão: Peso normal")
elif IMC >= 25 and IMC < 30:
    print("Conclusão: Acima do peso")
elif IMC >= 30 and IMC < 35:
    print("Conclusão: Obesidade Grau 1")
elif IMC >= 35 and IMC <= 40:
    print("Conclusão: Obesidade Grau 2")
else:
    print("Conclusão: Obesidade Grau 3")
print()

print(Nome + ", obrigado por participar do teste!")
