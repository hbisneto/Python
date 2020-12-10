from datetime import date
AnoAtual = date.today().year
SoftwareName = "SIGNO"

print("Nome:", SoftwareName)
print("Versão: 1.2")
print("Criado por: Heitor Bisneto")
print("Copyright © 2019 -", AnoAtual, "Bisneto. All rights reserved.")
print("")


MesNumber = 0
Separator = "----xx----"
MesNome = ""
GrupoSigno = ""

Nome = str(input("<" + SoftwareName + "> Qual o seu nome? "))
Dia = int(input("<" + SoftwareName + "> Insira o dia do seu nascimento? "))

if Dia > 31:
    print("<" + SoftwareName + "> Valor inválido...")
    print("<" + SoftwareName + "> Reinicie o programa...")
else:    
    Mes = str(input("<" + SoftwareName + "> Insira o mês do seu nascimento: "))
    AnoNascimento = int(input("<" + SoftwareName + "> Insira seu ano de nascimento: "))
    if Mes == "JAN" or Mes == "jan" or Mes == "01":
        MesNumber = 1
        MesNome = "Janeiro"
        if Dia >= 21:
            Signo = "Aquário"
            GrupoSigno = "Aquariano"
            print("")
            print("")
            print("<" + SoftwareName + "> Nome: ", Nome)
            print("<" + SoftwareName + "> Data de Nascimento: ", '{:0>2}'.format(Dia), "/", '{:0>2}'.format(MesNumber), "/", AnoNascimento)
            print("<" + SoftwareName + "> Idade: ", (AnoAtual - AnoNascimento), "anos")
            print("<" + SoftwareName + "> Signo: ", Signo)
            print("")
            print("")
            print("<" + SoftwareName + "> " + Nome + ". Nascido no dia " + str(Dia) + " de " + MesNome + ", é " + GrupoSigno)
            print(Separator*5)
        else:
            Signo = "Capricórnio"
            GrupoSigno = "Capricorniano"
            print("")
            print("")
            print("<" + SoftwareName + "> Nome: ", Nome)
            print("<" + SoftwareName + "> Data de Nascimento: ", '{:0>2}'.format(Dia), "/", '{:0>2}'.format(MesNumber), "/", AnoNascimento)
            print("<" + SoftwareName + "> Idade: ", (AnoAtual - AnoNascimento), "anos")
            print("<" + SoftwareName + "> Signo: ", Signo)
            print("")
            print("")
            print("<" + SoftwareName + "> " + Nome + ". Nascido no dia " + str(Dia) + " de " + MesNome + ", é " + GrupoSigno)
            print(Separator*5)
        
    if Mes == "FEV" or Mes == "fev" or Mes == "02":
        MesNumber = 2
        MesNome = "Fevereiro"
        if Dia >= 20:
            Signo = "Peixes"
            GrupoSigno = "Pisciano"
            print("")
            print("")
            print("<" + SoftwareName + "> Nome: ", Nome)
            print("<" + SoftwareName + "> Data de Nascimento: ", '{:0>2}'.format(Dia), "/", '{:0>2}'.format(MesNumber), "/", AnoNascimento)
            print("<" + SoftwareName + "> Idade: ", (AnoAtual - AnoNascimento), "anos")
            print("<" + SoftwareName + "> Signo: ", Signo)
            print("")
            print("")
            print("<" + SoftwareName + "> " + Nome + ". Nascido no dia " + str(Dia) + " de " + MesNome + ", é " + GrupoSigno)
            print(Separator*5)
        else:
            Signo = "Aquário"
            GrupoSigno = "Aquariano"
            print("")
            print("")
            print("<" + SoftwareName + "> Nome: ", Nome)
            print("<" + SoftwareName + "> Data de Nascimento: ", '{:0>2}'.format(Dia), "/", '{:0>2}'.format(MesNumber), "/", AnoNascimento)
            print("<" + SoftwareName + "> Idade: ", (AnoAtual - AnoNascimento), "anos")
            print("<" + SoftwareName + "> Signo: ", Signo)
            print("")
            print("")
            print("<" + SoftwareName + "> " + Nome + ". Nascido no dia " + str(Dia) + " de " + MesNome + ", é " + GrupoSigno)
            print(Separator*5)
        
    if Mes == "MAR" or Mes == "mar" or Mes == "03":
        MesNumber = 3
        MesNome = "Março"
        if Dia >= 21:
            Signo = "Áries"
            GrupoSigno = "ariano"
            print("")
            print("")
            print("<" + SoftwareName + "> Nome: ", Nome)
            print("<" + SoftwareName + "> Data de Nascimento: ", '{:0>2}'.format(Dia), "/", '{:0>2}'.format(MesNumber), "/", AnoNascimento)
            print("<" + SoftwareName + "> Idade: ", (AnoAtual - AnoNascimento), "anos")
            print("<" + SoftwareName + "> Signo: ", Signo)
            print("")
            print("")
            print("<" + SoftwareName + "> " + Nome + ". Nascido no dia " + str(Dia) + " de " + MesNome + ", é " + GrupoSigno)
            print(Separator*5)
        else:
            Signo = "Peixes"
            GrupoSigno = "pisciano"
            print("")
            print("")
            print("<" + SoftwareName + "> Nome: ", Nome)
            print("<" + SoftwareName + "> Data de Nascimento: ", '{:0>2}'.format(Dia), "/", '{:0>2}'.format(MesNumber), "/", AnoNascimento)
            print("<" + SoftwareName + "> Idade: ", (AnoAtual - AnoNascimento), "anos")
            print("<" + SoftwareName + "> Signo: ", Signo)
            print("")
            print("")
            print("<" + SoftwareName + "> " + Nome + ". Nascido no dia " + str(Dia) + " de " + MesNome + ", é " + GrupoSigno)
            print(Separator*5)
            
    if Mes == "ABR" or Mes == "abr" or Mes == "04":
        MesNumber = 4
        MesNome = "Abril"
        if Dia >= 21:
            Signo = "Touro"
            GrupoSigno = "taurino"
            print("")
            print("")
            print("<" + SoftwareName + "> Nome: ", Nome)
            print("<" + SoftwareName + "> Data de Nascimento: ", '{:0>2}'.format(Dia), "/", '{:0>2}'.format(MesNumber), "/", AnoNascimento)
            print("<" + SoftwareName + "> Idade: ", (AnoAtual - AnoNascimento), "anos")
            print("<" + SoftwareName + "> Signo: ", Signo)
            print("")
            print("")
            print("<" + SoftwareName + "> " + Nome + ". Nascido no dia " + str(Dia) + " de " + MesNome + ", é " + GrupoSigno)
            print(Separator*5)
        else:
            Signo = "Áries"
            GrupoSigno = "ariano"
            print("")
            print("")
            print("<" + SoftwareName + "> Nome: ", Nome)
            print("<" + SoftwareName + "> Data de Nascimento: ", '{:0>2}'.format(Dia), "/", '{:0>2}'.format(MesNumber), "/", AnoNascimento)
            print("<" + SoftwareName + "> Idade: ", (AnoAtual - AnoNascimento), "anos")
            print("<" + SoftwareName + "> Signo: ", Signo)
            print("")
            print("")
            print("<" + SoftwareName + "> " + Nome + ". Nascido no dia " + str(Dia) + " de " + MesNome + ", é " + GrupoSigno)
            print(Separator*5)
           
    if Mes == "MAI" or Mes == "mai" or Mes == "05":
        MesNumber = 5
        MesNome = "Maio"
        if Dia >= 21:
            Signo = "Gêmeos"
            GrupoSigno = "geminiano"
            print("")
            print("")
            print("<" + SoftwareName + "> Nome: ", Nome)
            print("<" + SoftwareName + "> Data de Nascimento: ", '{:0>2}'.format(Dia), "/", '{:0>2}'.format(MesNumber), "/", AnoNascimento)
            print("<" + SoftwareName + "> Idade: ", (AnoAtual - AnoNascimento), "anos")
            print("<" + SoftwareName + "> Signo: ", Signo)
            print("")
            print("")
            print("<" + SoftwareName + "> " + Nome + ". Nascido no dia " + str(Dia) + " de " + MesNome + ", é " + GrupoSigno)
            print(Separator*5)
        else:
            Signo = "Touro"
            GrupoSigno = "taurino"
            print("")
            print("")
            print("<" + SoftwareName + "> Nome: ", Nome)
            print("<" + SoftwareName + "> Data de Nascimento: ", '{:0>2}'.format(Dia), "/", '{:0>2}'.format(MesNumber), "/", AnoNascimento)
            print("<" + SoftwareName + "> Idade: ", (AnoAtual - AnoNascimento), "anos")
            print("<" + SoftwareName + "> Signo: ", Signo)
            print("")
            print("")
            print("<" + SoftwareName + "> " + Nome + ". Nascido no dia " + str(Dia) + " de " + MesNome + ", é " + GrupoSigno)
            print(Separator*5)
        
    if Mes == "JUN" or Mes == "jun" or Mes == "06":
        MesNumber = 6
        MesNome = "Junho"
        if Dia >= 21:
            Signo = "Câncer"
            GrupoSigno = "Canceriano"
            print("")
            print("")
            print("<" + SoftwareName + "> Nome: ", Nome)
            print("<" + SoftwareName + "> Data de Nascimento: ", '{:0>2}'.format(Dia), "/", '{:0>2}'.format(MesNumber), "/", AnoNascimento)
            print("<" + SoftwareName + "> Idade: ", (AnoAtual - AnoNascimento), "anos")
            print("<" + SoftwareName + "> Signo: ", Signo)
            print("")
            print("")
            print("<" + SoftwareName + "> " + Nome + ". Nascido no dia " + str(Dia) + " de " + MesNome + ", é " + GrupoSigno)
            print(Separator*5)
        else:
            Signo = "Gêmeos"
            GrupoSigno = "geminiano"
            print("")
            print("")
            print("<" + SoftwareName + "> Nome: ", Nome)
            print("<" + SoftwareName + "> Data de Nascimento: ", '{:0>2}'.format(Dia), "/", '{:0>2}'.format(MesNumber), "/", AnoNascimento)
            print("<" + SoftwareName + "> Idade: ", (AnoAtual - AnoNascimento), "anos")
            print("<" + SoftwareName + "> Signo: ", Signo)
            print("")
            print("")
            print("<" + SoftwareName + "> " + Nome + ". Nascido no dia " + str(Dia) + " de " + MesNome + ", é " + GrupoSigno)
            print(Separator*5)
            
    if Mes == "JUL" or Mes == "jul" or Mes == "07":
        MesNumber = 7
        MesNome = "Julho"
        if Dia >= 22:
            Signo = "Leão"
            GrupoSigno = "Leonino"
            print("")
            print("")
            print("<" + SoftwareName + "> Nome: ", Nome)
            print("<" + SoftwareName + "> Data de Nascimento: ", '{:0>2}'.format(Dia), "/", '{:0>2}'.format(MesNumber), "/", AnoNascimento)
            print("<" + SoftwareName + "> Idade: ", (AnoAtual - AnoNascimento), "anos")
            print("<" + SoftwareName + "> Signo: ", Signo)
            print("")
            print("")
            print("<" + SoftwareName + "> " + Nome + ". Nascido no dia " + str(Dia) + " de " + MesNome + ", é " + GrupoSigno)
            print(Separator*5)
        else:
            Signo = "Câncer"
            GrupoSigno = "Canceriano"
            print("")
            print("")
            print("<" + SoftwareName + "> Nome: ", Nome)
            print("<" + SoftwareName + "> Data de Nascimento: ", '{:0>2}'.format(Dia), "/", '{:0>2}'.format(MesNumber), "/", AnoNascimento)
            print("<" + SoftwareName + "> Idade: ", (AnoAtual - AnoNascimento), "anos")
            print("<" + SoftwareName + "> Signo: ", Signo)
            print("")
            print("")
            print("<" + SoftwareName + "> " + Nome + ". Nascido no dia " + str(Dia) + " de " + MesNome + ", é " + GrupoSigno)
            print(Separator*5)
                
    if Mes == "AGO" or Mes == "ago" or Mes == "08":
        MesNumber = 8
        MesNome = "Agosto"
        if Dia >= 22:
            Signo = "Virgem"
            GrupoSigno = "Virginiano"
            print("")
            print("")
            print("<" + SoftwareName + "> Nome: ", Nome)
            print("<" + SoftwareName + "> Data de Nascimento: ", '{:0>2}'.format(Dia), "/", '{:0>2}'.format(MesNumber), "/", AnoNascimento)
            print("<" + SoftwareName + "> Idade: ", (AnoAtual - AnoNascimento), "anos")
            print("<" + SoftwareName + "> Signo: ", Signo)
            print("")
            print("")
            print("<" + SoftwareName + "> " + Nome + ". Nascido no dia " + str(Dia) + " de " + MesNome + ", é " + GrupoSigno)
            print(Separator*5)
        else:
            Signo = "Leão"
            GrupoSigno = "Leonino"
            print("")
            print("")
            print("<" + SoftwareName + "> Nome: ", Nome)
            print("<" + SoftwareName + "> Data de Nascimento: ", '{:0>2}'.format(Dia), "/", '{:0>2}'.format(MesNumber), "/", AnoNascimento)
            print("<" + SoftwareName + "> Idade: ", (AnoAtual - AnoNascimento), "anos")
            print("<" + SoftwareName + "> Signo: ", Signo)
            print("")
            print("")
            print("<" + SoftwareName + "> " + Nome + ". Nascido no dia " + str(Dia) + " de " + MesNome + ", é " + GrupoSigno)
            print(Separator*5)
                
    if Mes == "SET" or Mes == "set" or Mes == "09":
        MesNumber = 9
        MesNome = "Setembro"
        if Dia >= 23:
            Signo = "Libra"
            GrupoSigno = "Libriano"
            print("")
            print("")
            print("<" + SoftwareName + "> Nome: ", Nome)
            print("<" + SoftwareName + "> Data de Nascimento: ", '{:0>2}'.format(Dia), "/", '{:0>2}'.format(MesNumber), "/", AnoNascimento)
            print("<" + SoftwareName + "> Idade: ", (AnoAtual - AnoNascimento), "anos")
            print("<" + SoftwareName + "> Signo: ", Signo)
            print("")
            print("")
            print("<" + SoftwareName + "> " + Nome + ". Nascido no dia " + str(Dia) + " de " + MesNome + ", é " + GrupoSigno)
            print(Separator*5)
        else:
            Signo = "Virgem"
            GrupoSigno = "Virginiano"
            print("")
            print("")
            print("<" + SoftwareName + "> Nome: ", Nome)
            print("<" + SoftwareName + "> Data de Nascimento: ", '{:0>2}'.format(Dia), "/", '{:0>2}'.format(MesNumber), "/", AnoNascimento)
            print("<" + SoftwareName + "> Idade: ", (AnoAtual - AnoNascimento), "anos")
            print("<" + SoftwareName + "> Signo: ", Signo)
            print("")
            print("")
            print("<" + SoftwareName + "> " + Nome + ". Nascido no dia " + str(Dia) + " de " + MesNome + ", é " + GrupoSigno)
            print(Separator*5)
        
    if Mes == "OUT" or Mes == "out" or Mes == "10":
        MesNumber = 10
        MesNome = "Outubro"
        if Dia >= 23:
            Signo = "Escorpião"
            GrupoSigno = "escorpiano"
            print("")
            print("")
            print("<" + SoftwareName + "> Nome: ", Nome)
            print("<" + SoftwareName + "> Data de Nascimento: ", '{:0>2}'.format(Dia), "/", '{:0>2}'.format(MesNumber), "/", AnoNascimento)
            print("<" + SoftwareName + "> Idade: ", (AnoAtual - AnoNascimento), "anos")
            print("<" + SoftwareName + "> Signo: ", Signo)
            print("")
            print("")
            print("<" + SoftwareName + "> " + Nome + ". Nascido no dia " + str(Dia) + " de " + MesNome + ", é " + GrupoSigno)
            print(Separator*5)
        else:
            Signo = "Libra"
            GrupoSigno = "Libriano"
            print("")
            print("")
            print("<" + SoftwareName + "> Nome: ", Nome)
            print("<" + SoftwareName + "> Data de Nascimento: ", '{:0>2}'.format(Dia), "/", '{:0>2}'.format(MesNumber), "/", AnoNascimento)
            print("<" + SoftwareName + "> Idade: ", (AnoAtual - AnoNascimento), "anos")
            print("<" + SoftwareName + "> Signo: ", Signo)
            print("")
            print("")
            print("<" + SoftwareName + "> " + Nome + ". Nascido no dia " + str(Dia) + " de " + MesNome + ", é " + GrupoSigno)
            print(Separator*5)
                
    if Mes == "NOV" or Mes == "nov" or Mes == "11":
        MesNumber = 11
        MesNome = "Novembro"
        if Dia >= 22:
            Signo = "Sagitário"
            GrupoSigno = "Sagitariano"
            print("")
            print("")
            print("<" + SoftwareName + "> Nome: ", Nome)
            print("<" + SoftwareName + "> Data de Nascimento: ", '{:0>2}'.format(Dia), "/", '{:0>2}'.format(MesNumber), "/", AnoNascimento)
            print("<" + SoftwareName + "> Idade: ", (AnoAtual - AnoNascimento), "anos")
            print("<" + SoftwareName + "> Signo: ", Signo)
            print("")
            print("")
            print("<" + SoftwareName + "> " + Nome + ". Nascido no dia " + str(Dia) + " de " + MesNome + ", é " + GrupoSigno)
            print(Separator*5)
        else:
            Signo = "Escorpião"
            GrupoSigno = "escorpiano"
            print("")
            print("")
            print("<" + SoftwareName + "> Nome: ", Nome)
            print("<" + SoftwareName + "> Data de Nascimento: ", '{:0>2}'.format(Dia), "/", '{:0>2}'.format(MesNumber), "/", AnoNascimento)
            print("<" + SoftwareName + "> Idade: ", (AnoAtual - AnoNascimento), "anos")
            print("<" + SoftwareName + "> Signo: ", Signo)
            print("")
            print("")
            print("<" + SoftwareName + "> " + Nome + ". Nascido no dia " + str(Dia) + " de " + MesNome + ", é " + GrupoSigno)
            print(Separator*5)

    if Mes == "DEZ" or Mes == "dez" or Mes == "12":
        MesNumber = 12
        MesNome = "Dezembro"
        if Dia >= 22:
            Signo = "Capricórnio"
            GrupoSigno = "Capricorniano"
            print("")
            print("")
            print("<" + SoftwareName + "> Nome: ", Nome)
            print("<" + SoftwareName + "> Data de Nascimento: ", '{:0>2}'.format(Dia), "/", '{:0>2}'.format(MesNumber), "/", AnoNascimento)
            print("<" + SoftwareName + "> Idade: ", (AnoAtual - AnoNascimento), "anos")
            print("<" + SoftwareName + "> Signo: ", Signo)
            print("")
            print("")
            print("<" + SoftwareName + "> " + Nome + ". Nascido no dia " + str(Dia) + " de " + MesNome + ", é " + GrupoSigno)
            print(Separator*5)
        else:
            Signo = "Sagitário"
            GrupoSigno = "Sagitariano"
            print("")
            print("")
            print("<" + SoftwareName + "> Nome: ", Nome)
            print("<" + SoftwareName + "> Data de Nascimento: ", '{:0>2}'.format(Dia), "/", '{:0>2}'.format(MesNumber), "/", AnoNascimento)
            print("<" + SoftwareName + "> Idade: ", (AnoAtual - AnoNascimento), "anos")
            print("<" + SoftwareName + "> Signo: ", Signo)
            print("")
            print("")
            print("<" + SoftwareName + "> " + Nome + ". Nascido no dia " + str(Dia) + " de " + MesNome + ", é " + GrupoSigno)
            print(Separator*5)
