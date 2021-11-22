## O programa permite que usuário entre com um número (somente números)
## O algorítimo verifica se ele é palíndromo (verificando o número digitado de trás pra frente) e,
## Caso não seja, soma o número original com o número invertido.
## O programa verifica novamente se o resultado é um palíndromo e soma novamente
## Até encontrar o palíndromo do número.

print(">> Palindromo <<")
print("="*80)

AUX = str(input(">> Digite um número: "))
print("="*80)
StrNumber = AUX.split()
Sequence = ''.join(StrNumber)
Size = len(Sequence)-1
Inverse = ''
    
for i in range(Size, -1, -1):
    Inverse += Sequence[i]

try:
    print(f'>> O inverso de {int(Sequence)} é {int(Inverse)}')

    if int(Sequence) == int(Inverse):
        print(">> Forma um palíndromo")
        print("="*80)
    else:
        print(">> Não forma um palíndromo")
        print(f'>> Sequence: {Sequence}')
        print(f'>> Inverse: {Inverse}')
        print("="*80)
        Calc = int(Sequence) + int(Inverse)
        StrCalc = str(Calc).split()
        NewSequence = ''.join(StrCalc)
        NewSize = len(NewSequence)-1
        NewInverse = ''

        for x in range(NewSize, -1, -1):
            NewInverse += NewSequence[x]

        print(f'>> O inverso de {int(NewSequence)} é {int(NewInverse)}')
        
        if int(NewSequence) == int(NewInverse):
            print(">> Forma um palíndromo")
            print("="*80)
        else:
            print(">> Não forma um palíndromo")
            print(f'>> NewSequence: {NewSequence}')
            print(f'>> NewInverse: {NewInverse}')
            print("="*80)

            Loop = True
            Count = 0
            while Loop == True:
                Count += int(NewInverse)
                Result = int(NewSequence) + Count
                StrResult = str(Result).split()
                ResultSequence = ''.join(StrResult)
                ResultSize = len(ResultSequence)-1
                ResultInverse = ''

                for j in range(ResultSize, -1, -1):
                    ResultInverse += ResultSequence[j]

                print(f'>> Encontrando palíndromo... {ResultInverse}')
            
                if int(Result) == int(ResultInverse):
                    Loop = False
                    print(f'>> ResultSequence: {ResultSequence}')
                    print(f'>> ResultInverse: {ResultInverse}')
                print("="*80)
                    
except:
    print("Não é um número")
    print("="*80)
