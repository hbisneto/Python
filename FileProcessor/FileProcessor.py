import os
import glob
from datetime import date
AnoAtual = date.today().year
SoftwareName = "FileProcessor"
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

MyArray = []
Nome = str()
SystemOpcao = int()
Count = int()

def Inserir():
    print()
    print("=" * 15, "INSERIR", "=" * 15)
    print(">> INSERIR")
    Inserir.Nome = str(input("  >> Informe o nome: "))
    MyArray.append(Inserir.Nome)
    open(f'{Inserir.Nome}.txt', "w+")
    F = open(f'{Inserir.Nome}.txt', "a+")
    Inserir.TextOnFile = str(input("  >> Digite o que gostaria de adicionar no arquivo: "))
    F.write(f'{Inserir.TextOnFile}')
    
    print(f'  >> O valor "{Inserir.Nome}" foi inserido na lista!')
    print("=" * 15, "INSERIR", "=" * 15)
    print()
    
def Deletar():
    print()
    print("=" * 15, "DELETAR", "=" * 15)
    print(">> DELETAR")
    Deletar.Nome = str(input("  >> Informe o nome que será deletado: "))

    for item in MyArray:
        if item == Deletar.Nome:
            MyArray.remove(item)
            os.remove(f'{item}.txt')
        print(f'  >> O valor "{Deletar.Nome}" foi removido na lista!')
    print("=" * 15, "DELETAR", "=" * 15)
    print()

def Buscar():
    MyDir = glob.glob('*.txt')
    print()
    print("=" * 15, "BUSCAR", "=" * 15)
    print(">> BUSCAR")
    TotalResults = 0
    ArquivoResult = []
    Count = 0
    Buscar.Nome = str(input(">> Qual nome gostaria de procurar: "))

    for files in MyDir:
        F = open(files, "r")
        Reader = F.readlines()
        for Line in Reader:
            ItemCount = 0
            if Buscar.Nome == Line:
                ItemCount += 1
                TotalResults += ItemCount
                print(f'>> +{ItemCount} A busca retornou "{Line}" como resultado em {files}')
                ArquivoResult.append(files)

        for Aqvs in ArquivoResult:
            Count += 1
    
    try:
        if Count >= 1:
            print(f'>> Sua busca retornou {Count} resultados em {files}')
        else:
            print(f'>> Sua busca não retornou resultados em {files}')
    except:
        print(f'>> Sua busca não retornou resultados.')
        
def Exibir():
    print()
    print(">> EXIBIR")
    print("  >> Dados abaixo:")
    print()

    MyCounter = 0
    MyDir = glob.glob('*.txt')
    print(f'  >> Exibindo em ordem alfabetica: {MyDir}')
    for files in MyDir:
        MyCounter += 1
        print(f'  >> Item {MyCounter}: {files}')
    print(f'  >> Total de itens na lista: {MyCounter}')

    print()
    
def System():
    while(SystemOpcao != 7):
        print("=" * 15, SoftwareName, "=" * 15)
        print(">> Escolha uma opção: ")
        print(">> 0. >> MAIS OPÇÕES")
        print(">> 1. Inserir")
        print(">> 2. Deletar")
        print(">> 3. Pesquisar")
        print(">> 4. Exibir")
        print(">> 5. Finalizar")
        print("=" * 15, SoftwareName, "=" * 15)
        print()
        Opcao = int(input(">> Digite o número da opção escolhida: "))

        if Opcao == 0:
            MaisOpc()
        elif Opcao == 1:
            Inserir()
        elif Opcao == 2:
            Deletar()
        elif Opcao == 3:
            Buscar()
        elif Opcao == 4:
            Exibir()
        elif Opcao == 5:
            exit()

def MaisOpc():
    print("=" * 15, SoftwareName, "=" * 15)
    print(">> Escolha uma opção: ")
    print(">> 1. Inserir texto no arquivo")
    print(">> 2. Ler arquivo")
    print(">> Qualquer Tecla. Voltar para opções iniciais")
    print("=" * 15, SoftwareName, "=" * 15)
    print()
    MaisOpc.Opcao = int(input(">> Digite o número da opção escolhida: "))
    if MaisOpc.Opcao == 1:
        ArquivoInsertText()
    elif MaisOpc.Opcao == 2:
        ArquivoReadText()
    else:
        System()

def ArquivoInsertText():
    AIT = ArquivoInsertText
    AIT.MyDir = glob.glob('*.txt')
    AIT.Nome = str(input("Insira o nome do arquivo (Ele deve estar no mesmo diretorio desse arquivo de python): "))

    for AIT.Arquivo in AIT.MyDir:
        if AIT.Arquivo == AIT.Nome + ".txt":
            # Abrir para ler
            F = open(f'{AIT.Arquivo}', "r")
            if F.mode == 'r':
                AIT.Contents = F.read()
            AIT.UserText = str(input(">> Digite o que gostaria de adicionar ao arquivo: "))
            # Abrir para escrever
            open(f'{AIT.Arquivo}', "w+")
            F = open(f'{AIT.Arquivo}', "a+")
            F.write(AIT.Contents)
            F.write(f'\n{AIT.UserText}')

def ArquivoReadText():
    AIT = ArquivoInsertText
    AIT.MyDir = glob.glob('*.txt')
    AIT.Nome = str(input("Insira o nome do arquivo (Ele deve estar no mesmo diretorio desse arquivo de python): "))

    for AIT.Arquivo in AIT.MyDir:
        if AIT.Arquivo == AIT.Nome + ".txt":
            # Abrir para ler
            F = open(f'{AIT.Arquivo}', "r")
            if F.mode == 'r':
                AIT.Contents = F.read()
    print(f'>> Leitura de arquivo: {AIT.Nome}.txt')
    print(AIT.Contents)

System()
