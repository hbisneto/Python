from datetime import date
AnoAtual = date.today().year
SoftwareName = "ADD TO ARRAY"
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

Demo = str(input("Gostaria de executar uma DEMO agora? [Y/N]: "))
if Demo == "Y" or Demo == "y" or Demo == "1":
    Frase = "A BB CCC DDDD"
    print("\nEscreva uma frase:",Frase)
    WordSplit = Frase.split()
    MyArray = []
    Count = 0

    for CurrentWord in WordSplit:
        Count = Count + 1
        MyArray.append(CurrentWord.upper())
        print()
        print("Index", Count-1,":", MyArray[Count - 1])
        print("Linha", Count,":", MyArray)
        
    print()
    print("Array:", MyArray)
    print()

    try:
        if MyArray[0] == "A":
            print("Execução de processo, caso o texto corresponda ao índice 0")
            
        if MyArray[1] == "BB":
            print("Execução de processo, caso o texto corresponda ao índice 1")

        if MyArray[2] == "CCC":
            print("Execução de processo, caso o texto corresponda ao índice 2")

        if MyArray[30] == "???":
            print("Execução de processo, caso o texto corresponda ao índice 30")
    except:
        print("\n*** MENSAGEM DE TRATATIVA DE ERRO: FORA DOS ÍNDICES DA MATRIZ ***")
elif Demo == "N" or Demo == "n" or Demo == "0":
    Frase = str(input("Escreva uma frase: "))
    WordSplit = Frase.split()
    MyArray = []
    Count = 0

    for CurrentWord in WordSplit:
        Count = Count + 1
        MyArray.append(CurrentWord.lower())
        print()
        print("Index", Count-1,":", MyArray[Count - 1])
        print("Linha", Count,":", MyArray)
        
    print()
    print("Array:", MyArray)
    print()

    try:
        if MyArray[0] == "1":
            print("Linha 1")
            
        if MyArray[1] == "2":
            print("Linha 2")

        if MyArray[2] == "3":
            print("Linha 3")

        if MyArray[30] == "30":
            print("Linha 30")
    except:
        print("\n>>> PARECE QUE VOCÊ QUER RETORNAR UM VALOR DE UM INDEX INEXISTENTE.")
