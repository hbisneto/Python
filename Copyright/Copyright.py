from datetime import date
AnoAtual = date.today().year
SoftwareName = "Copyright App"
Version = "2021"
CopyrightName = "Heitor Bisneto."
print("Nome:", SoftwareName)
print("Versão:", Version)
print("Criado por:", CopyrightName)
if AnoAtual == 2020:
    print("Copyright ©", AnoAtual, "|", CopyrightName, "All rights reserved.")
else:
    print("Copyright © 2020 -", AnoAtual, "|", CopyrightName, "All rights reserved.")
print("="*80)
print(f'[{SoftwareName}] - Em Execução...')
print("="*80)
