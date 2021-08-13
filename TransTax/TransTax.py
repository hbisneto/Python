from datetime import date
AnoAtual = date.today().year
SoftwareName = "TRANSTAX"

print("Nome:", SoftwareName)
print("Versão: 1.1")
print("Criado por: Heitor Bisneto")
print("Copyright © 2020 -", AnoAtual, "Bisneto. All rights reserved.")
print("")

Separator = ("=")*30
BusTax = 0
TrainTax = 0
MetroTax = 0
AddService = 0
ConfirmAddService = 0

BusConfirmation = str(input("<" + SoftwareName + "> Você usa ônibus? [Y/N]: "))
if BusConfirmation == "Y" or BusConfirmation == "y" or BusConfirmation == "1":
    BusTax = float(input("<" + SoftwareName + "> Insira o preço da tarifa do ônibus: R$ "))

TrainConfirmation = str(input("<" + SoftwareName + "> Você usa trêm? [Y/N]: "))
if TrainConfirmation == "Y" or TrainConfirmation == "y" or TrainConfirmation == "1":
    TrainTax = float(input("<" + SoftwareName + "> Insira o preço da tarifa do trêm: R$ "))

MetroConfirmation = str(input("<" + SoftwareName + "> Você usa metrô? [Y/N]: "))
if MetroConfirmation == "Y" or MetroConfirmation == "y" or MetroConfirmation == "1":
    MetroTax = float(input("<" + SoftwareName + "> Insira o preço da tarifa do metrô: R$ "))

AddTax = str(input("<" + SoftwareName + "> Você usa algum serviço de transporte adicional? [Y/N]: "))
if AddTax == "Y" or AddTax == "y" or AddTax == "1":
    AddService = float(input("<" + SoftwareName + "> Insira o preço médio da tarifa paga em serviços de transportes adicionais: R$ "))


TotalGoing = (BusTax + TrainTax + MetroTax)
print()
print(Separator)
print("Resumo de Cálculo")
print(Separator)
print("<" + SoftwareName + "> Tarifa paga em ônibus: R$", BusTax)
print("<" + SoftwareName + "> Tarifa paga em trem: R$", TrainTax)
print("<" + SoftwareName + "> Tarifa paga em metrô: R$", MetroTax)
print("<" + SoftwareName + "> Tarifa paga em serviços adicionais: R$", AddService)
print("<" + SoftwareName + "> Tarifas totais sem taxa de serviços adicionais: R$", TotalGoing)
print("<" + SoftwareName + "> Tarifas totais somente ida: R$", TotalGoing + AddService)
print(Separator)
print("Fim de Resumo de Cálculo")
print(Separator)
print()

print(Separator)
print("Tarifas de Volta")
print(Separator)
BackTax = str(input("<" + SoftwareName + "> Gostaria de calcular os valores de volta usando as mesmas configurações? [Y/N]: "))
if BackTax == "Y" or BackTax == "y" or BackTax == "1":
    print("<" + SoftwareName + "> Para melhor precisão de resultados, confirmaremos alguns dados:")
    print("<" + SoftwareName + "> Sua tarifa de serviços de transportes adicionais foram de R$ " + str(AddService))
    ConfirmAddService = float(input("<" + SoftwareName + "> Insira o valor da tarifa adicional de transporte de volta: R$ "))
    TotalTaxes = ((TotalGoing * 2) + AddService + ConfirmAddService)
    print("<" + SoftwareName + "> Tarifas totais ida e volta: R$ ", TotalTaxes)

print()
print(Separator)
print("Projeção")
print(Separator)
Projection = str(input("<" + SoftwareName + "> Gostaria de fazer uma projeção de gastos por período? [Y/N]: "))
if Projection == "Y" or Projection == "y" or Projection == "1":
    Period = int(input("<" + SoftwareName + "> Gostaria de uma média baseada em quantos dias? [1 - 31]: "))
    if Period < 1 or Period > 31:
        print("<" + SoftwareName + "> Não foi possível calcular o periodo. Execute o " + SoftwareName + " novamente")
    else:
        TotalPeriod = (((TotalGoing * 2) + AddService + ConfirmAddService) * Period)
        print("<" + SoftwareName + "> O calculo total do periodo estimado é R$:", TotalPeriod)
        print(Separator)
        print("Fim da Projeção")
        print(Separator)
