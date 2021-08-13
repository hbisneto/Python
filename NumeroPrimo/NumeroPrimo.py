from datetime import date
AnoAtual = date.today().year
SoftwareName = "Número Primo"
Version = "1.0"
CopyrightName = "Heitor Bisneto."
print("Nome:", SoftwareName)
print("Versão:", Version)
print("Criado por:", CopyrightName)
if AnoAtual == 2021:
    print("Copyright ©", AnoAtual, "|", CopyrightName, "All rights reserved.")
else:
    print("Copyright © 2021 -", AnoAtual, "|", CopyrightName, "All rights reserved.")
print("="*80)
print(f'[{SoftwareName}] - Em Execução...')
print("="*80)

Qtd = 0
Numero = int(input(">> Informe um número: "))

for N in range(1, Numero + 1):
    Resto = Numero % N
    if Resto == 0:
        Qtd += 1
        
if Qtd == 2:
	print(f'>> O número "{Numero}" é um número primo')
else:
    print(f'>> O número "{Numero}" não é um número primo')
