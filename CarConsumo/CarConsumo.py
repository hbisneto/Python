from time import sleep
from datetime import date
AnoAtual = date.today().year
SoftwareName = "CARCONSUMO"

print("Nome:", SoftwareName)
print("Versão: 1.1")
print("Criado por: Heitor Bisneto")
print("Copyright © 2020 -", AnoAtual, "Bisneto. All rights reserved.")
print("")
ProgressBar = "❚"
ProgressBarSep = "*"

QtdTanque = float(input("<" + SoftwareName + "\Capacidade do Tanque> "))
GasPreco = float(input("<" + SoftwareName + "\Preco da Gasolina por Litro> "))
EtaPreco = float(input("<" + SoftwareName + "\Preco do Etanol por Litro> "))
print()
print("===============================")

if GasPreco > EtaPreco:
    MaisCaro = (GasPreco - EtaPreco)
    Preco = (EtaPreco * QtdTanque)
    print("<" + SoftwareName + "> Gasolina é R$", MaisCaro, "mais cara")
    print("<" + SoftwareName + "> Necessário R$", Preco, "para completar o tanque com etanol")
    print("===============================")
    print()
elif GasPreco < EtaPreco:  
    MaisCaro = (EtaPreco - GasPreco)
    Preco = (GasPreco * QtdTanque)
    print("<" + SoftwareName + "> Etanol é R$", MaisCaro, "mais caro")
    print("<" + SoftwareName + "> Necessário R$", Preco, "para completar o tanque com gasolina")
    print("===============================")
    print()
else:
    MaisCaro = (EtaPreco - GasPreco)
    Preco = (GasPreco * QtdTanque)
    print("<" + SoftwareName + "> Os combustíveis têm o mesmo preço. Escolha o da sua preferência")
    print("<" + SoftwareName + "> Necessário R$", Preco, "para completar o tanque")
    print("===============================")
    print()

Question = str(input("<" + SoftwareName + "> Gostaria de fazer os calculos de abastecimento? [Y or N]> "))
if Question == "N" or Question == "n" or Question == "0":
    print("O App '" + SoftwareName + "' foi encerrado corretamente...")
elif Question == "Y" or Question == "y" or Question == "1":
    print()
    print("===============================")
    print("Preparando programa de calulos")
    print("===============================")
    sleep(3)
    QtdAbastecimento = float(input("<" + SoftwareName + "> Quantos litros serão abastecidos? "))
    VeiculoConsumo = float(input("<" + SoftwareName + "> Insira o consumo do veículo por litro: "))
    DistanciaPrevista = float(input("<" + SoftwareName + "> Insira a distância que irá percorrer: "))
    VeiculoConsumo = (DistanciaPrevista/QtdAbastecimento)
    print()
    print("===============================")
    print("<" + SoftwareName + "> O veículo consumirá em média", VeiculoConsumo, "litros por KM" )
    print("===============================")

    
    print()
    if QtdAbastecimento > QtdTanque:
        print("<" + SoftwareName + ">A quantidade de abastecimento não pode ser maior que a capacidade do tanque")
    else:
        Abastecido = ((QtdAbastecimento / QtdTanque) * 100)
        DispoTanqueLitros = (QtdTanque - QtdAbastecimento)
        DispoTanque = (100 - (QtdAbastecimento / QtdTanque) * 100)
        sleep(1)
        print("<" + SoftwareName + "> Necessários ", DispoTanqueLitros, " litros para completar o tanque")
        sleep(1)
        print("<" + SoftwareName + "\Abastecimento em tanque> " + (ProgressBar * int(Abastecido)), int(Abastecido), "%")
        sleep(1)
        print("<" + SoftwareName + "\Espaço disponível em tanque> " + (ProgressBar * int(DispoTanque)), int(DispoTanque), "%")
else:
    if Question == "":
        print("<" + SoftwareName + "\MENSAGEM>\nNenhuma opção selecionada. Execute o programa novamente.")
    else:
        print("<" + SoftwareName + "\MENSAGEM>\n'" + Question + "' não é uma opção válida. Execute o programa novamente.")
