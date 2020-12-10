#O algoritmo abaixo, le o destino do passageiro e mostra o preço da passagem
#de acordo com a tabela abaixo
from time import sleep
from datetime import date
AnoAtual = date.today().year
SoftwareName = "PASSAGEM"

print("Nome:", SoftwareName)
print("Versão: 1.1")
print("Criado por: Heitor Bisneto")
print("Copyright © 2020 -", AnoAtual, "Bisneto. All rights reserved.")
print("")

CentroOeste_Ida = str("300,00")
CentroOeste_Ida_Volta = str("550,00")
Nordeste_Ida = str("350,00")
Nordeste_Ida_Volta = str("650,00")
Norte_Ida = str("500,00")
Norte_Ida_Volta = str("950,00")
Sudeste_Ida = str("600,00")
Sudeste_Ida_Volta = str("850,00")
Sul_Ida = str("200,00")
Sul_Ida_Volta = str("350,00")

print("="*80)
print("             DESTINO                    IDA                         IDA E VOLTA")
print("="*80)
print("<" + SoftwareName + "/1> Região Centro-Oeste        R$ 300,00                   R$ 550,00")
print("<" + SoftwareName + "/2> Região Nordeste            R$ 350,00                   R$ 650,00")
print("<" + SoftwareName + "/3> Região Norte               R$ 500,00                   R$ 950,00")
print("<" + SoftwareName + "/4> Região Sudeste             R$ 600,00                   R$ 850,00")
print("<" + SoftwareName + "/5> Região Sul                 R$ 200,00                   R$ 350,00")
print("="*80)

Destino = str(input("<" + SoftwareName + "> " + "Digite o número da opção que tem o destino da sua viagem: "))
print("")

if Destino == "1":
    print("<" + SoftwareName + "\Região Centro-Oeste> O preço da passagem de ida é R$ " + CentroOeste_Ida)
    print("<" + SoftwareName + "\Região Centro-Oeste> O preço das passagens de ida e volta é R$ " + CentroOeste_Ida_Volta)
elif Destino == "2":
    print("<" + SoftwareName + "\Região Nordeste> O preço da passagem de ida custa R$ " + Nordeste_Ida)
    print("<" + SoftwareName + "\Região Nordeste> O preço das passagens de ida e volta é R$ " + Nordeste_Ida_Volta)
elif Destino == "3":
    print("<" + SoftwareName + "\Região Norte> O preço da passagem de ida custa R$ " + Norte_Ida)
    print("<" + SoftwareName + "\Região Norte> O preço das passagens de ida e volta é R$ " + Norte_Ida_Volta)
elif Destino == "4":
    print("<" + SoftwareName + "\Região Sudeste> O preço da passagem de ida custa R$ " + Sudeste_Ida)
    print("<" + SoftwareName + "\Região Sudeste> O preço das passagens de ida e volta é R$ " + Sudeste_Ida_Volta)
elif Destino == "5":
    print("<" + SoftwareName + "\Região Sul> O preço da passagem de ida custa R$ " + Sul_Ida)
    print("<" + SoftwareName + "\Região Sul> O preço das passagens de ida e volta é R$ " + Sul_Ida_Volta)
else:
    print("<" + SoftwareName + "> " + "A empresa X não trabalha com essa rota")
    Sugestao = str(input("<" + SoftwareName + "> " + "Gostaria de deixar uma sugestão de destino?[Y/N] "))
    if Sugestao == "Y" or Sugestao == "y" or Sugestao == "1" or Sugestao == "S" or Sugestao == "s":
        UserType = str(input("<" + SoftwareName + "> " + "Use este campo para enviar a sua sugestão: "))
        print("<" + SoftwareName + "> " + "Preparando envio da sugestão...")
        sleep(3)
        print("<" + SoftwareName + "> " + "Sua sugestão é: '" + UserType + "'")
        sleep(1)
        ConfirmEnvio = str(input("<" + SoftwareName + "> " + "Confirmar envio? [Y/N] "))
        if ConfirmEnvio == "Y" or ConfirmEnvio == "y" or ConfirmEnvio == "1" or ConfirmEnvio == "S" or ConfirmEnvio == "s":
            print("<" + SoftwareName + "> " + "Sua sugestão foi enviada com sucesso!")
            sleep(1)
            print("<" + SoftwareName + "> " + "A empresa X agradece a preferência!")
        elif ConfirmEnvio == "N" or ConfirmEnvio == "n" or ConfirmEnvio == "0":
            print("<" + SoftwareName + "> " + "Envio de sugestão Cancelado!")
        else:
            print("<" + SoftwareName + "> " + "Operação Cancelada")
            print("<" + SoftwareName + "> " + "A empresa X agradece a preferência")
    elif Sugestao == "N" or Sugestao == "n" or Sugestao == "0":
        print("<" + SoftwareName + "> " + "Obrigado por utilizar nossos serviços. A empresa X agradece a sua preferência!")
    else:
        print("<" + SoftwareName + "> " + "A empresa X agradece a preferência!")
