from datetime import date
AnoAtual = date.today().year
SoftwareName = "StringSelection"
Version = "3.0"
CopyrightName = "Heitor Bisneto."
print("Nome:", SoftwareName)
print("Versão:", Version)
print("Criado por:", CopyrightName)
if AnoAtual == 2019:
    print("Copyright ©", AnoAtual, "|", CopyrightName, "All rights reserved.")
else:
    print("Copyright © 2019 -", AnoAtual, "|", CopyrightName, "All rights reserved.")
print("="*80)
print(f'[{SoftwareName}] - Em Execução...')
print("="*80)

Nome = str(input("Escreva algo usando letras: "))

if Nome == "Moqueca" or Nome == "moqueca":
    print("Categoria: Comida")
elif Nome == "Ford" or Nome == "ford":
    print("Categoria: Marca de carro")
else:
    print("Categoria: Não Cadastrada")
