# ProgressBar

O programa mostra exemplos de barras de progresso e suas formatações.


Código:

```
from datetime import date
AnoAtual = date.today().year
SoftwareName = "Barra de Progresso"
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

ProgressBar = "█"
UserPrompt = int(input(">> Insira um valor para a barra de progresso: "))

Progress = int(UserPrompt/10)
ProgressValue = f'{ProgressBar}' * Progress

print(">>")
print(">>")

if Progress > 10 or UserPrompt < 0:
    print(f'>> {UserPrompt}% não é um valor válido para a barra de progresso.')
    print(f'>> Insira um valor entre 0 e 100')
else:
    print("="*80)
    print("[Exemplo 1] - Em execução...")
    print("="*80)
    print(f'Status: {ProgressValue}')
    print("="*80)
    print(">>")
    print(">>")
    print("="*80)
    print("[Exemplo 2] - Em execução...")
    print("="*80)
    print(f'Status: {UserPrompt}%')
    print("="*80)
    print(">>")
    print(">>")
    print("="*80)
    print("[Exemplo 3] - Em execução...")
    print("="*80)
    print(f'Status ({UserPrompt}%): {ProgressValue}')
    print("="*80)
    print(">>")
    print(">>")
    print("="*80)
    print("[Exemplo 4] - Em execução...")
    print("="*80)
    print(f'{ProgressValue} {UserPrompt}%\n>> Instalando sistema...\n>> Acerca de X minutos')
    print("="*80)

    print(">>")
    print(">>")
    print("="*80)
    print("[Exemplo 5] - Em execução...")
    print("="*80)
    print(f'|{ProgressValue}| {UserPrompt}MB {Progress}kB/s\n>> Instalando sistema...\n>> Acerca de {Progress} minutos restantes...')
    print("="*80)
```

Output:

```
Nome: Barra de Progresso
Versão: 1.0
Criado por: Heitor Bisneto.
Copyright © 2021 | Heitor Bisneto. All rights reserved.
================================================================================
[Barra de Progresso] - Em Execução...
================================================================================
>> Insira um valor para a barra de progresso: 100
>>
>>
================================================================================
[Exemplo 1] - Em execução...
================================================================================
Status: ██████████
================================================================================
>>
>>
================================================================================
[Exemplo 2] - Em execução...
================================================================================
Status: 100%
================================================================================
>>
>>
================================================================================
[Exemplo 3] - Em execução...
================================================================================
Status (100%): ██████████
================================================================================
>>
>>
================================================================================
[Exemplo 4] - Em execução...
================================================================================
██████████ 100%
>> Instalando sistema...
>> Acerca de X minutos
================================================================================
>>
>>
================================================================================
[Exemplo 5] - Em execução...
================================================================================
|██████████| 100MB 10kB/s
>> Instalando sistema...
>> Acerca de 10 minutos restantes...
================================================================================
>>> 
```