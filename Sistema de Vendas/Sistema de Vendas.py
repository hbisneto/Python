# Biblioteca que possibilita o retorno do nome de login do usuário
import getpass
#import datetime
from datetime import date
from datetime import datetime
DiaAtual = date.today().day
MesAtual = date.today().month
AnoAtual = date.today().year

# Sobre o App
SoftwareName = "Sistema de Vendas"
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

# Atribui o retorno da função getuser() dentro da variável UserName
UserName = getpass.getuser().upper()

# Cria arquivos de métrica para cada funcionário
Nome = str(input("Digite o seu nome: "))

# Extensão Padrão
ArquivoExtensao = ".py"
ArquivoLog = Nome + ArquivoExtensao
# Extesão JSON
ArquivoExtensaoJSON = ".json"
ArquivoLogJSON = Nome + ArquivoExtensaoJSON
# Entensão XML
ArquivoExtensaoXML = ".xml"
ArquivoLogXML = Nome + ArquivoExtensaoXML    

# Entrada do Funcionário
HoraInicial = int(input("Hora inicial: "))
MinInicial = int(input("Minuto inicial: "))
HoraFinal = int(input("Hora Final: "))
MinutoFinal = int(input("Minuto Final: "))

# Repetidores
Conta = 0
Loop = 1
Conta2 = 0
Loop2 = 1

# Vendas
TotalDeVendas = int(0)
ValorTotalVendas = float(0)
ValorCadaVenda = []

# Conversão de Horar para Minuto
HoraInitToMin = HoraInicial * 60
HoraFinalToMin = HoraFinal * 60
# Calcula a Hora Inicial mais o Minuto Inicial (Em minutos)
HoraToMin = float(HoraInitToMin + MinInicial)
# Calcula a Hora Final mais o Minuto Final (Em minutos)
MinutosCalc = float(HoraFinalToMin + MinutoFinal)
# Converte o calculo dos minutos em Horas
HorasTrabalhadas = float(abs(MinutosCalc - HoraToMin)) / 60

# Função Sobre o Sistema
def SistemaSobre():
    WindowName = ">>OPÇÕES DO SISTEMA<<"
    WindowLength = len(WindowName)
    SeparadorAux = 50
    SeparadorStr = "-"
    Separador = SeparadorStr * 73
    print()
    print(Separador)
    print(SeparadorStr * int(abs(SeparadorAux/2)), ">>OPÇÕES DO SISTEMA<<", SeparadorStr * int(abs(SeparadorAux/2)))
    print(Separador)
    print(">> INSIRA SOMENTE O NÚMERO DA OPÇÃO OU O NOME DA OPÇÃO:")
    print(Separador)
    print()
    print(Separador)
    print(">> ARQUIVO")
    print(Separador)
    print("(1) PrintRel = Imprimir Relatório")
    print("(2) SalvarRel = Salvar Relatório")
    print("(3) LerRel = Ler Relatório")
    print(Separador)
    print(">> CONVERTER")
    print(Separador)
    print("(4) ConvertToJSON = Converte o arquivo para JSON.")
    print("(5) ConvertToXML = Converte o arquivo para XML.")
    print("(6) LerJSON = Ler arquivo JSON.")
    print("(7) LerXML =	Ler arquivo XML.")
    print(Separador)
    print(Separador)
    print()

# Função que obtém as métricas de vendas
def Relatorio():
    print()
    print("-" * 10, "Relatório Diário", "-" * 10)
    # Horas Trabalhadas
    if HorasTrabalhadas == 0:
        print("Não Houve Horas Trabalhadas:", HorasTrabalhadas)
    elif HorasTrabalhadas == 1:
        print("Horas Trabalhadas:", HorasTrabalhadas, "hora")
    else:
        print("Horas Trabalhadas:", HorasTrabalhadas, "hora(s)")
    # Total de Vendas
    print("Total de Vendas:", TotalDeVendas, "Venda(s)")
    #Valor de Cada venda
    print("Valor de Cada Venda:", ValorCadaVenda)
    # Valor total de Vendas
    print("Valor Total de Vendas: R$", ValorTotalVendas)
    # Média de Vendas por hora
    try:
        MediaVendasHora = float(TotalDeVendas / HorasTrabalhadas)
        print("Média de Vendas por Hora:", MediaVendasHora, "vendas por hora")
    except:
        print("Não foi possível calcular a média de vendas por hora!")
    print("-" * 10, "Relatório Diário", "-" * 10)
    print()

# Função que salva o relatório em um arquivo .py
## Para alterar a extensão do arquivo basta mudar a entrada "ArquivoExtensao"
def SalvarRelatorio():
    F = open(ArquivoLog, "a")
    F.write("")
    F.write("---------- Relatório Diário ----------\n")
    # Horas Trabalhadas
    if HorasTrabalhadas == 0:
        F.write(f'Não Houve Horas Trabalhadas: {HorasTrabalhadas}\n')
    elif HorasTrabalhadas == 1:
        F.write(f'Horas Trabalhadas: {HorasTrabalhadas} hora(s)\n')
    else:
        F.write(f'Horas Trabalhadas: {HorasTrabalhadas} hora(s)\n')
    # Total de Vendas
    F.write(f'Total de Vendas: {TotalDeVendas} Venda(s)\n')
    #Valor de Cada venda
    F.write(f'Valor de Cada Venda: {ValorCadaVenda}\n')
    # Valor total de Vendas
    F.write(f'Valor Total de Vendas: R$ {ValorTotalVendas}\n')
    # Média de Vendas por hora
    try:
        MediaVendasHora = float(TotalDeVendas / HorasTrabalhadas)
        F.write(f'Média de Vendas por Hora: {MediaVendasHora} vendas por hora\n')
    except:
        F.write("Não foi possível calcular a média de vendas por hora!\n")
    F.write("---------- Relatório Diário ----------\n\n")
    F.write("")
    F.close()

# Função salva as métricas em um arquivo JSON 
def ConverterJSON():
    try:
        JSON = open(ArquivoLogJSON, "x")
        JSON.write("//\n")
        JSON.write(f'//  Criado por {UserName} on {DiaAtual}/{MesAtual}/{AnoAtual}.\n')
        JSON.write(f'//  Copyright © {AnoAtual} {UserName}. Todos os direitos reservados.\n')
        JSON.write("//\n")
        JSON.write(f'//  Esse arquivo foi convertido em JSON com o "Sistema de Vendas"\n')
        JSON.write(f'//  Dúvidas ou sugestões: http://github.com/hbisneto/\n')
        JSON.write("//\n\n")
        JSON.write("{\n")
        JSON.write('    "RelatorioDiario": {\n')
        # Horas Trabalhadas
        if HorasTrabalhadas == 0:
            JSON.write(f'       "HorasTrabalhadas": "{HorasTrabalhadas} hora(s)",\n')
        elif HorasTrabalhadas == 1:
            JSON.write(f'       "HorasTrabalhadas": "{HorasTrabalhadas} hora(s)",\n')
        else:
            JSON.write(f'       "HorasTrabalhadas": "{HorasTrabalhadas} hora(s)",\n')
        # Total de Vendas
        JSON.write(f'       "TotalDeVendas": "{TotalDeVendas} Venda(s)",\n')
        #Valor de Cada venda
        JSON.write(f'       "ValorDeCadaVenda": "{ValorCadaVenda}",\n')
        # Valor total de Vendas
        JSON.write(f'       "ValorTotalDeVendas": "R$ {ValorTotalVendas}",\n')
        # Média de Vendas por hora
        try:
            MediaVendasHora = float(TotalDeVendas / HorasTrabalhadas)
            JSON.write(f'       "MediaVendasHora": "{MediaVendasHora} vendas por hora"\n')
        except:
            JSON.write(f'       "MediaVendasHora": "Não foi possivel calcular a média de vendas por hora"\n')
        JSON.write("   }\n")
        JSON.write("}\n\n")
        JSON.close()
    except:
        JSON = open(ArquivoLogJSON, "a")
        JSON.write("{\n")
        JSON.write('    "RelatorioDiario": {\n')
        # Horas Trabalhadas
        if HorasTrabalhadas == 0:
            JSON.write(f'       "HorasTrabalhadas": "{HorasTrabalhadas} hora(s)",\n')
        elif HorasTrabalhadas == 1:
            JSON.write(f'       "HorasTrabalhadas": "{HorasTrabalhadas} hora(s)",\n')
        else:
            JSON.write(f'       "HorasTrabalhadas": "{HorasTrabalhadas} hora(s)",\n')
        # Total de Vendas
        JSON.write(f'       "TotalDeVendas": "{TotalDeVendas} Venda(s)",\n')
        #Valor de Cada venda
        JSON.write(f'       "ValorDeCadaVenda": "{ValorCadaVenda}",\n')
        # Valor total de Vendas
        JSON.write(f'       "ValorTotalDeVendas": "R$ {ValorTotalVendas}",\n')
        # Média de Vendas por hora
        try:
            MediaVendasHora = float(TotalDeVendas / HorasTrabalhadas)
            JSON.write(f'       "MediaVendasHora": "{MediaVendasHora} vendas por hora"\n')
        except:
            JSON.write(f'       "MediaVendasHora": "Não foi possivel calcular a média de vendas por hora"\n')
        JSON.write("   }\n")
        JSON.write("}\n\n")
        JSON.close()

# Função salva as métricas em um arquivo XML
def ConverterXML():
    try:
        XML = open(ArquivoLogXML, "x")
        XML.write("<!--\n")
        XML.write(f'    Criado por {UserName} on {DiaAtual}/{MesAtual}/{AnoAtual}.\n')
        XML.write(f'    Copyright © {AnoAtual} {UserName}. Todos os direitos reservados.\n')
        XML.write("\n")
        XML.write(f'    Esse arquivo foi convertido em XML com o "Sistema de Vendas"\n')
        XML.write(f'    Dúvidas ou sugestões: http://github.com/hbisneto/\n')
        XML.write("-->\n\n")
        
        XML.write('<?xml version="1.0" encoding="UTF-8"?>\n')

        XML.write('<RelatorioDiario>\n')
        XML.write(f'       <HorasTrabalhadas> {HorasTrabalhadas} </HorasTrabalhadas>\n')
        XML.write(f'       <TotalDeVendas> {TotalDeVendas} </TotalDeVendas>\n')
        XML.write(f'       <ValorCadaVenda> {ValorCadaVenda} </ValorCadaVenda>\n')
        XML.write(f'       <ValorTotalVendas> {ValorTotalVendas} </ValorTotalVendas>\n')
        try:
            MediaVendasHora = float(TotalDeVendas / HorasTrabalhadas)
            XML.write(f'       <MediaVendasHora> {MediaVendasHora} </MediaVendasHora>\n')
        except:
            XML.write(f'       <MediaVendasHora> Não foi possivel calcular a média de vendas por hora </MediaVendasHora>\n')
        XML.write('</RelatorioDiario>\n\n')
        XML.close()
    except:
        XML = open(ArquivoLogXML, "a")

        XML.write('<RelatorioDiario>\n')
        XML.write(f'       <HorasTrabalhadas> {HorasTrabalhadas} </HorasTrabalhadas>\n')
        XML.write(f'       <TotalDeVendas> {TotalDeVendas} </TotalDeVendas>\n')
        XML.write(f'       <ValorCadaVenda> {ValorCadaVenda} </ValorCadaVenda>\n')
        XML.write(f'       <ValorTotalVendas> {ValorTotalVendas} </ValorTotalVendas>\n')
        try:
            MediaVendasHora = float(TotalDeVendas / HorasTrabalhadas)
            XML.write(f'       <MediaVendasHora> {MediaVendasHora} </MediaVendasHora>\n')
        except:
            XML.write(f'       <MediaVendasHora> Não foi possivel calcular a média de vendas por hora </MediaVendasHora>\n')
        XML.write('</RelatorioDiario>\n\n')
        XML.close()

# "Primeiro Loop": para saber se o usuário gostaria de vender um produto
while (Conta < Loop):
    VenderProduto = str(input("Gostaria de vender um produto? [S ou N]: "))
    # Se o usuário quiser vender um produto
    if VenderProduto == "S" or VenderProduto == "s" or VenderProduto == "1":
        Loop += 1
        Conta += 1
        PrecoProduto = float(input("Qual o valor do produto? "))
        ValorCadaVenda.append(PrecoProduto)
        TotalDeVendas = TotalDeVendas + 1
        ValorTotalVendas = ValorTotalVendas + PrecoProduto
    else:
        # Se o usuário não quiser vender um produto
        if VenderProduto == "N" or VenderProduto == "n" or VenderProduto == "2" or VenderProduto == "0":
            print()
            # "Segundo Loop": para habilitar ações do sistema
            while (Conta2 < Loop2):
                # Chamar a função SistemaSobre() para obter informações de entrada para o usuário
                SistemaSobre()
                OpcaoSistema = str(input("O que deseja fazer agora? "))

                # Opção do sistema 1
                if OpcaoSistema == "1" or OpcaoSistema == "PrintRel":
                    Loop2 += 1
                    Conta2 += 1
                    Relatorio()
                    print("Relatório impresso com sucesso!")
                # Opção do sistema 2
                elif OpcaoSistema == "2" or OpcaoSistema == "SalvarRel":
                    Loop2 += 1
                    Conta2 += 1
                    SalvarRelatorio()
                    print("Salvando Relatório...")
                    print("Arquivo salvo com sucesso")
                # Opção do sistema 3
                elif OpcaoSistema == "3" or OpcaoSistema == "LerRel":
                    Loop2 += 1
                    Conta2 += 1
                    Relatorio = open(Nome+ArquivoExtensao, "r")
                    for Linha in Relatorio:
                        print(Linha)
                # Opção do sistema 4
                elif OpcaoSistema == "4" or OpcaoSistema == "ConvertToJSON":
                    Loop2 += 1
                    Conta2 += 1
                    ConverterJSON()
                    print("Convertendo Arquivo JSON...\nSalvando arquivo convertido...")
                    print("Arquivo convertido com sucesso")
                # Opção do sistema 5
                elif OpcaoSistema == "5" or OpcaoSistema == "ConvertToXML":
                    Loop2 += 1
                    Conta2 += 1
                    ConverterXML()
                    print("Convertendo Arquivo XML...\nSalvando arquivo convertido...")
                    print("Arquivo convertido com sucesso")
                elif OpcaoSistema == "6" or OpcaoSistema == "LerJSON":
                    Loop2 += 1
                    Conta2 += 1
                    JSONArquivo = open(ArquivoLogJSON, "r")
                    for Linha in JSONArquivo:
                        print(Linha)
                elif OpcaoSistema == "7" or OpcaoSistema == "LerXML":
                    Loop2 += 1
                    Conta2 += 1
                    XMLArquivo = open(ArquivoLogXML, "r")
                    for Linha in XMLArquivo:
                        print(Linha)
                else:
                    # Para o segundo Loop
                    break
        # Para o primeiro Loop
        break
