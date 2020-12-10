# Importação de bibliotecas
from datetime import date

# SOBRE O PROGRAMA
# Atribui o valor do ano atual a 'AnoAtual'
AnoAtual = date.today().year
# Atribui o valor 'MÉDIA ALUNO' a 'SoftwareName'
SoftwareName = "MÉDIA ALUNO"
# Atribui o valor da versão do programa a 'Version'
Version = "1.0"
# Atribui o valor 'Heitor Bisneto' a 'CopyrightName'
CopyrightName = "Heitor Bisneto."
# Imprime o nome do programa
print("Nome:", SoftwareName)
# Imprime a versão do programa
print("Versão:", Version)
# Imprime o texto de copyright
print("Criado por:", CopyrightName)
# Se o ano atual for igual a '2020'
if AnoAtual == 2020:
    # Imprime texto de copyright para o ano de 2020
    print("Copyright ©", AnoAtual, "|", CopyrightName, "All rights reserved.")
# Senão
else:
    # Imprime texto de copyright para os anos posteriores a 2020
    print("Copyright © 2020 -", AnoAtual, "|", CopyrightName, "All rights reserved.")
# Nova Linha: Questão de estética. Somente para deixar visualmente mais organizado.
print()

# ENTRADAS E SEUS TIPOS
# Enquanto 'True' mantém o programa rodando
Loop = True
# Matriz que manterá o nome dos alunos
AlunoArray = []
# Matriz que manterá as notas dos alunos
NotasArray = []
# Matriz que manterá as médias dos alunos
MediaArray = []
# Matriz que manterá as medias trimestrais dos alunos
MediaTriArray = []
# Matriz que manterá as medias semestrais dos alunos
MediaSemArray = []
# Contador de Loop
LoopCount = int(0)
# Inicio do Programa
print("=" * 30, SoftwareName, "=" * 30)
# Informação sobre o programa
print(">> As informações inseridas processam dados de média")
# Informação sobre o programa
print(">> Se você gostaria de fazer o calculo por semestre ou trimestre:\n- Preencha as notas restantes com a média.")
# Informação sobre o programa
print("- Execute a função com o comando MediaCalc() e faça o cálculo pelo periodo.")
# Nova Linha: Questão de estética. Somente para deixar visualmente mais organizado.
print()

# Função MediaCalc()
def MediaCalc():
    # Texto explicativo
    print("=" * 10, "Escolha um dos periodos abaixo:", "=" * 10)
    # Nova Linha: Questão de estética. Somente para deixar visualmente mais organizado.
    print()
    # Primeira opção
    print(">> 1. Bimestre")
    # Segunda opção
    print(">> 2. Trimestre")
    # Terceira opção
    print(">> 3. Semestre")
    # Nova Linha: Questão de estética. Somente para deixar visualmente mais organizado.
    print()
    # Permite o usuário digitar uma das opções acima
    MediaCalc.Periodo = int(input("Digite o número do periodo acima: "))
    # Se o periodo digitado pelo usuário for 1 (Bimestre)
    if MediaCalc.Periodo == 1:
        # Imprime periodo escolhido
        print("Periodo escolhido: Bimestre")
        # Atribui o valor da média do Bimestre
        MediaCalc.Media = float(input("Qual a média do Bimestre? [Use ponto ao invés de virgula]: "))
        #Nova Linha: Questão de estética. Somente para deixar visualmente mais organizado.
        print()
        # Calculo da média pelo periodo
        MediaCalc.Diferenca = ((Dados.Nota1 + Dados.Nota2 + Dados.Nota3 + Dados.Nota4) / 4)
        # Contador limitado ao número de itens na matriz AlunoArray
        for MediaCalc.i in range(0, len(AlunoArray)):
            # Imprime o nome do aluno
            print(">> Aluno:", AlunoArray[MediaCalc.i])
            # Imprime a média do aluno
            print(">> Media:", MediaArray[MediaCalc.i])
            # Se a media do aluno for maior ou igual a média do bimestre
            if MediaArray[MediaCalc.i] >= MediaCalc.Media:
                # Imprime mensagem de aluno aprovado
                print(">> Você foi aprovado!")
                # Imprime a soma das notas acima da media
                print(">> Notas acima da média:", MediaArray[MediaCalc.i] - MediaCalc.Media)
                # Nova Linha: Questão de estética. Somente para deixar visualmente mais organizado.
                print()
            # Senão
            else:
                # Imprime mensagem de aluno reprovado
                print(">> Você foi retido!")
                # Imprime pontos necessários para aprovação
                print("Pontos necessários para aprovação:", MediaArray[MediaCalc.i] - MediaCalc.Media)
                # Nova Linha: Questão de estética. Somente para deixar visualmente mais organizado.
                print()
    # Se o periodo digitado pelo usuário for 2 (Trimestre)    
    elif MediaCalc.Periodo == 2:
        # Imprime periodo escolhido
        print("Periodo escolhido: Trimestre")
        # Atribui o valor da média do Trimestre
        MediaCalc.Media = float(input("Qual a média do Trimestre? [Use ponto ao invés de virgula]: "))
        # Nova Linha: Questão de estética. Somente para deixar visualmente mais organizado.
        print()
        # Calculo da média pelo periodo
        MediaCalc.Diferenca = ((Dados.Nota1 + Dados.Nota2 + Dados.Nota3) / 3)
        # Contador limitado ao número de itens na matriz AlunoArray
        for MediaCalc.i in range(0, len(AlunoArray)):
            # Imprime o nome do aluno
            print(">> Aluno:", AlunoArray[MediaCalc.i])
            # Imprime a média do aluno
            print(">> Media:", MediaTriArray[MediaCalc.i])
            # Se a media do aluno for maior ou igual a média do trimestre
            if MediaTriArray[MediaCalc.i] >= MediaCalc.Media:
                # Imprime mensagem de aluno aprovado
                print(">> Você foi aprovado!")
                # Imprime a soma das notas acima da media
                print(">> Notas acima da média:", MediaTriArray[MediaCalc.i] - MediaCalc.Media)
                # Nova Linha: Questão de estética. Somente para deixar visualmente mais organizado.
                print()
            # Senão
            else:
                # Imprime mensagem de aluno reprovado
                print(">> Você foi retido!")
                # Imprime pontos necessários para aprovação
                print("Pontos necessários para aprovação:", MediaTriArray[MediaCalc.i] - MediaCalc.Media)
                # Nova Linha: Questão de estética. Somente para deixar visualmente mais organizado.
                print()
    # Se o periodo digitado pelo usuário for 3 (Semestre)
    elif MediaCalc.Periodo == 3:
        # Imprime periodo escolhido
        print("Periodo escolhido: Semestre")
        # Atribui o valor da média do Semestre
        MediaCalc.Media = float(input("Qual a média do Semestre? [Use ponto ao invés de virgula]: "))
        # Nova Linha: Questão de estética. Somente para deixar visualmente mais organizado.
        print()
        # Calculo da média pelo periodo
        MediaCalc.Diferenca = ((Dados.Nota1 + Dados.Nota2) / 2)
        # Contador limitado ao número de itens na matriz AlunoArray
        for MediaCalc.i in range(0, len(AlunoArray)):
            # Imprime o nome do aluno
            print(">> Aluno:", AlunoArray[MediaCalc.i])
            # Imprime a média do aluno
            print(">> Media:", MediaSemArray[MediaCalc.i])
            # Se a media do aluno for maior ou igual a média do trimestre
            if MediaSemArray[MediaCalc.i] >= MediaCalc.Media:
                # Imprime mensagem de aluno aprovado
                print(">> Você foi aprovado!")
                # Imprime a soma das notas acima da media
                print(">> Notas acima da média:", MediaSemArray[MediaCalc.i] - MediaCalc.Media)
                # Nova Linha: Questão de estética. Somente para deixar visualmente mais organizado.
                print()
            # Senão
            else:
                # Imprime mensagem de aluno reprovado
                print(">> Você foi retido!")
                # Imprime pontos necessários para aprovação
                print("Pontos necessários para aprovação:", MediaSemArray[MediaCalc.i] - MediaCalc.Media)
                # Nova Linha: Questão de estética. Somente para deixar visualmente mais organizado.
                print()
# Função Dados()          
def Dados():
    # Atribui dado em 'Dados.NomeAluno'
    Dados.NomeAluno = str(input(">> Nome do Aluno: "))
    # Tratativa de erros
    try:
        # Adiciona o Aluno na Matriz
        AlunoArray.append(Dados.NomeAluno)

        # Atribui dado em 'Nota1'
        Dados.Nota1 = float(input(">> 1º Nota: "))
        # Atribui dado em 'Nota2'
        Dados.Nota2 = float(input(">> 2º Nota: "))
        # Atribui dado em 'Nota3'
        Dados.Nota3 = float(input(">> 3º Nota: "))
        # Atribui dado em 'Nota4'
        Dados.Nota4 = float(input(">> 4º Nota: "))

        # Adiciona Nota1 a Matriz
        NotasArray.append(Dados.Nota1)
        # Adiciona Nota2 a Matriz
        NotasArray.append(Dados.Nota2)
        # Adiciona Nota3 a Matriz
        NotasArray.append(Dados.Nota3)
        # Adiciona Nota4 a Matriz
        NotasArray.append(Dados.Nota4)
        # Adiciona a media para a matriz
        MediaArray.append((Dados.Nota1 + Dados.Nota2 + Dados.Nota3 + Dados.Nota4) / 4)
        # Adiciona a média trimestral a matriz
        MediaTriArray.append((Dados.Nota1 + Dados.Nota2 + Dados.Nota3) / 3)
        # Adiciona a média Semestral a matriz
        MediaSemArray.append((Dados.Nota1 + Dados.Nota2) / 2)

        # Imprime o último aluno inserido na matriz
        print(">> Nome do Aluno:", AlunoArray[LoopCount - 1])
        # Imprime a média do Aluno
        print(">> Media do Aluno", AlunoArray[LoopCount - 1] + ":", MediaArray[LoopCount - 1])
        # Nova Linha: Questão de estética. Somente para deixar visualmente mais organizado.
        print()
    # Caso dê ruim...
    except Exception as ex:
        # Imprime a mensagem de erro personalizada.
        print(">> Erro: Faça novamente!")
        # Mostra a descrição do erro disparado
        print(">> Relatorio de Erro:", ex)
# Enquanto o 'Loop' for 'True'...
while Loop == True:
    # Adiciona 1 ao contador
    LoopCount += 1
    # Executa a função Dados()
    Dados()
    # Pergunta ao usuário se ele gostaria de continuar
    SysQuest = str(input(">> Gostaria de continuar? [S] ou [N]: "))
    #Nova Linha: Questão de estética. Somente para deixar visualmente mais organizado.
    print()
    # Verifica se a resposta do usuário foi N ou outro caractere
    if SysQuest == "N":
        # Atribui o valor 'False' ao 'Loop'
        Loop = False
        # Imprime o último aluno inserido na matriz
        print(">> Último Aluno Inserido na Matriz:", AlunoArray[LoopCount - 1])
        # Imprime a média do aluno
        print(">> Media do Aluno", AlunoArray[LoopCount - 1], ":", MediaArray[LoopCount - 1])
        #Nova Linha: Questão de estética. Somente para deixar visualmente mais organizado.
        print()
        # Imprime os alunos na matriz
        print(">> Alunos na Matriz:", AlunoArray)
        # Imprime as notas na matriz
        print(">> Notas na Matriz:", NotasArray)
        # Imprime a Media
        print(">> Medias na Matriz:", MediaArray)
