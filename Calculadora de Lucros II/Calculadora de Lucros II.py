#PrecoVenda = float(input("Informe o valor da venda: "))

# Valores Semanais
# CustoSemanal = 0
#DespesaSemanal = 0
#LucroSemanal = 0
# Valores Mensais
#CustoMensal = 0
# Valores Mensais (Com projeção)

from datetime import date
AnoAtual = date.today().year
SoftwareName = "CALCULADORA DE LUCROS II"

print("Nome:", SoftwareName)
print("Versão: 2.0")
print("Criado por: Heitor Bisneto")
print("Copyright © 2020 -", AnoAtual, "Bisneto. All rights reserved.")
print("")

ContadorIndex = 0
CustoArray = []
DespesaArray = []
LucroArray = []
i = 0


def Application():
    print()
    print("=" * 10, "Inicio da Consulta", "=" * 10)
    print("Dia:", ContadorIndex+1)
    Custo = float(input(">> INFORME O VALOR DO CUSTO DE PRODUÇÃO: R$ "))

    MsgAddDespesa = str(input("\n>> GOSTARIA DE INSERIR O VALOR DAS DESPESAS PARA CÁLCULO?\n>> CASO 'NÃO', AS DESPESAS TERÃO O VALOR IGUAIS A ZERO - [S/N]: "))
    if MsgAddDespesa == "S" or MsgAddDespesa == "s" or MsgAddDespesa == "1":
        DespesaSemanal = float(input(">> INFORME O VALOR DAS DESPESAS: R$ "))
        Despesa = DespesaSemanal
    elif MsgAddDespesa == "N" or MsgAddDespesa == "n" or MsgAddDespesa == "0" or MsgAddDespesa == "2":
        #Despesa = Custo/2
        Despesa = 0
    else:
        print(">> NÃO FOI POSSÍVEL CALCULAR O VALOR INFORMADO!")

    MsgAddLucro = str(input("\n>> GOSTARIA DE INFORMAR VALOR DA VENDA?\n>> CASO 'NÃO', O VALOR DA VENDA SERÁ IGUAL AO VALOR DO CUSTO - [S/N]: "))
    if MsgAddLucro == "S" or MsgAddLucro == "s" or MsgAddLucro == "1":
        LucroSemanal = float(input(">> INFORME O VALOR DA VENDA DO PRODUTO: R$ "))
        Lucro = LucroSemanal - (Custo + Despesa)
    elif MsgAddLucro == "N" or MsgAddLucro == "n" or MsgAddLucro == "0" or MsgAddLucro == "2":
        Lucro = Custo - Despesa
    else:
        print(">> NÃO FOI POSSÍVEL CALCULAR O VALOR INFORMADO!")

    CustoArray.append(Custo)
    DespesaArray.append(Despesa)
    LucroArray.append(Lucro)
    print("=" * 10, "Final da Consulta", "=" * 10)

def ValoresSemanais():
    print()
    print("=" * 10, "Valores Semanais", "=" * 10)
    ContadorCusto = 0
    ContadorDespesa = 0
    ContadorLucro = 0

    ValoresSemanais.CustoSemanal = float()
    ValoresSemanais.DespesaSemanal = float()
    ValoresSemanais.LucroSemanal = float()

    for Custo in CustoArray:
        ContadorCusto += 1
        ValoresSemanais.CustoSemanal += Custo
        print(f'>> {ContadorCusto}º Custo: R$', CustoArray[ContadorCusto-1])
    print()
    
    for Despesa in DespesaArray:
        ContadorDespesa += 1
        ValoresSemanais.DespesaSemanal += Despesa
        print(f'>> {ContadorDespesa}º Despesa: R$', DespesaArray[ContadorDespesa-1])
    print()

    for Lucro in LucroArray:
        ContadorLucro += 1
        ValoresSemanais.LucroSemanal += Lucro
        print(f'>> {ContadorLucro}º Lucro: R$', LucroArray[ContadorLucro-1])
    print()
    
    print(">> Custos Semanais: R$", ValoresSemanais.CustoSemanal)
    print(">> Despesas Semanais: R$", ValoresSemanais.DespesaSemanal)
    if ValoresSemanais.LucroSemanal < 0:
        print(">> Lucros Semanais: R$", ValoresSemanais.LucroSemanal, "<< PREJUÍZO")
    else:
        print(">> Lucros Semanais: R$", ValoresSemanais.LucroSemanal)
    print("=" * 10, "Valores Semanais", "=" * 10)
    
def ValoresMensais():
    print()
    print("=" * 10, "Valores Mensais", "=" * 10)
    ContadorCusto = 0
    ContadorDespesa = 0
    ContadorLucro = 0

    ValoresMensais.CustoMensal = float()
    ValoresMensais.DespesaMensal = float()
    ValoresMensais.LucroMensal = float()

    for Custo in CustoArray:
        ContadorCusto += 1
        ValoresMensais.CustoMensal += Custo
        print(f'>> {ContadorCusto}º Custo: R$', CustoArray[ContadorCusto-1])
    print()
    
    for Despesa in DespesaArray:
        ContadorDespesa += 1
        ValoresMensais.DespesaMensal += Despesa
        print(f'>> {ContadorDespesa}º Despesa: R$', DespesaArray[ContadorDespesa-1])
    print()

    for Lucro in LucroArray:
        ContadorLucro += 1
        ValoresMensais.LucroMensal += Lucro
        print(f'>> {ContadorLucro}º Lucro: R$', LucroArray[ContadorLucro-1])
    print()
    
    print(">> Custos Mensais: R$", ValoresMensais.CustoMensal)
    print(">> Despesas Mensais: R$", ValoresMensais.DespesaMensal)
    if ValoresMensais.LucroMensal < 0:
        print(">> Lucros Mensais: R$", ValoresMensais.LucroMensal, "<< PREJUÍZO")
    else:
        print(">> Lucros Mensais: R$", ValoresMensais.LucroMensal)
    print("=" * 10, "Valores Mensais", "=" * 10)

def Projecao():
    print()
    print("=" * 10, "Projeção de Valores", "=" * 10)
    ContadorProjecao = 0

    Projecao.Lucro = 0
    
    PrPeriodo = int(input("Digite o período da projeção (em dias): "))
    for Lucro in LucroArray:
        ContadorProjecao += 1
        Projecao.Lucro += Lucro
    PrLucro = (Projecao.Lucro/i) * PrPeriodo
    
    print(f'>> Projeção de valores totais do periodo: R$', PrLucro)
    print(f'>> Projeção de valores totais do periodo: R$', PrLucro)
    print("=" * 10, "Projeção de Valores", "=" * 10)
    
while i < 3:
    i += 1
    try:
        Periodo = ContadorIndex + 1
        Application()
        ContadorIndex += 1
        if Periodo == 7:
            ValoresSemanais()
        elif Periodo == 30:
            ValoresMensais()
    except Exception as ex:
        print(">> VOCÊ INSERIU UM CARACTERE INVÁLIDO:", ex)
        print("=" * 10, "Final da Consulta", "=" * 10)
