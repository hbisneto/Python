# Número Primo

O programa processa o número inserido pelo usuário e imprime na tela se ele for primo ou não.

Código:

```
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
```

Output (Número primo):

```
Nome: Número Primo
Versão: 1.0
Criado por: Heitor Bisneto.
Copyright © 2021 | Heitor Bisneto. All rights reserved.
================================================================================
[Número Primo] - Em Execução...
================================================================================
>> Informe um número: 3
>> O número "3" é um número primo
>>> 
```
Output (Número não primo):

```
Nome: Número Primo
Versão: 1.0
Criado por: Heitor Bisneto.
Copyright © 2021 | Heitor Bisneto. All rights reserved.
================================================================================
[Número Primo] - Em Execução...
================================================================================
>> Informe um número: 8
>> O número "8" não é um número primo
>>>
```