ContadorIndex = 0
CustoArray = []
DespesaArray = []
LucroArray = []
i = 0

def App():
    print("################################################################################")
    print("##                      Módulo: LucroDespesa.py                               ##")
    print("##                      Versão: 2.0.2                                         ##")
    print("################################################################################")
    print("=" * 80)
    print(">> Inicio da Consulta")
    print("=" * 80)
    print("Dia:", ContadorIndex+1)
    Custo = float(input(">> INFORME O VALOR DO CUSTO DE PRODUÇÃO: R$ "))

    MsgAddDespesa = str(input("\n>> GOSTARIA DE INSERIR O VALOR DAS DESPESAS PARA CÁLCULO?\n>> CASO 'NÃO', AS DESPESAS TERÃO O VALOR IGUAIS A ZERO - [S/N]: "))
    if MsgAddDespesa == "S" or MsgAddDespesa == "s" or MsgAddDespesa == "1":
        DespesaSemanal = float(input(">> INFORME O VALOR DAS DESPESAS: R$ "))
        Despesa = DespesaSemanal
    elif MsgAddDespesa == "N" or MsgAddDespesa == "n" or MsgAddDespesa == "0" or MsgAddDespesa == "2":
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
    print("=" * 80)
    print(">> Final da Consulta")
    print("=" * 80)
    

    ValoresSemanais()

def ValoresSemanais():
    print()
    print("=" * 80)
    print(">> Valores Semanais")
    print("=" * 80)
    
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
    #print()
    
    for Despesa in DespesaArray:
        ContadorDespesa += 1
        ValoresSemanais.DespesaSemanal += Despesa
        print(f'>> {ContadorDespesa}º Despesa: R$', DespesaArray[ContadorDespesa-1])
    #print()

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
    print("=" * 80)
    print(">> Valores Semanais")
    print("=" * 80)
    
    
def ValoresMensais():
    print()
    print("=" * 80)
    print(">> Valores Mensais")
    print("=" * 80)
    
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
    print("=" * 80)
    print(">> Valores Mensais")
    print("=" * 80)
    

def Projecao():
    print()
    print("=" * 80)
    print(">> Projeção de Valores")
    print("=" * 80)
    
    ContadorProjecao = 0

    Projecao.Lucro = 0
    
    PrPeriodo = int(input("Digite o período da projeção (em dias): "))
    for Lucro in LucroArray:
        ContadorProjecao += 1
        Projecao.Lucro += Lucro
    PrLucro = (Projecao.Lucro/i) * PrPeriodo
    
    print(f'>> Projeção de valores totais do periodo: R$', PrLucro)
    print(f'>> Projeção de valores totais do periodo: R$', PrLucro)
    print("=" * 80)
    print(">> Projeção de Valores")
    print("=" * 80)
    
while i < 3:
    i += 1
    try:
        Periodo = ContadorIndex + 1
        App()
        ContadorIndex += 1
        if Periodo == 7:
            ValoresSemanais()
        elif Periodo == 30:
            ValoresMensais()
    except Exception as ex:
        print(">> VOCÊ INSERIU UM CARACTERE INVÁLIDO:", ex)
        print("=" * 10, "Final da Consulta", "=" * 10)
