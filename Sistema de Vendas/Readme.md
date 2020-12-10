# Sistema de Vendas
O ***Sistema de Vendas***, É um pequeno sistema de gerenciamento de vendas e seus cálculos.
<br> O sistema pode obter os seguintes dados do usuário:

* Nome;
* Horário de entrada;
* Minuto do Horário de entrada;
* Horário de Sáida;
* Minuto do Horário de Saída;

O programa também verifica se o usuário gostaria de efetuar uma venda:

* Caso o usuário digite "S", o programa solicita que o usuário insira o valor do produto.
* Caso o usuário digite "N", o programa mostra as opções do sistema.

## Opções do sistema:
O sistema conta com 7 opções:

### - Arquivo
<strong> 1. Imprimir Relatório: </strong>
<br> Depois dos dados de vendas serem inseridos, é possível ver o histórico dos valores inseridos e cálculo de vendas durante o periodo trabalhado.
<br>
<br><strong> 2. Salvar Relatório: </strong>
<br> Um relatório, é um arquivo contendo todas as informações de vendas do dia e salvo com o nome do usuário responsável pela inserção dos dados na extensão .py
<br> Essa opção cria o arquivo de relatório caso ele não exista. Se o arquivo já existir, os dados são complementados no arquivo existente.
<br>
<br><strong> 3. Ler Relatório: </strong>
<br> Essa opção acessa o arquivo de relatório e mostra na tela o conteúdo do arquivo.
<br>

### - Converter
<strong> 4. Converter para JSON: </strong>
<br> Conversão em JSON: A quarta opção do sistema converte o relatório diário em um arquivo ```.json```
<br> Se o arquivo já for um arquivo existente, os dados serão complementados no momento da conversão. Assim como no processo de "Salvamento do Relatório".
<br>
<br><strong> 5. Converter para XML: </strong>
<br> Conversão em XML: Nessa opção, o sistema converte o relatório diário em um arquivo ```.xml```
<br> Se o arquivo já for um arquivo existente, os dados serão complementados no momento da conversão. Assim como nos processos de "Conversão para JSON" e "Salvamento do Relatório".
<br>
<br><strong> 6. Ler arquivo JSON: </strong>
<br> Essa opção acessa o arquivo JSON e mostra na tela o conteúdo do arquivo.
<br>
<br><strong> 7. Ler arquivo XML: </strong>
<br> Essa opção acessa o arquivo XML e mostra na tela o conteúdo do arquivo.


> Nesse repositório é possível ver os screenshots do programa em execução. Basta acessar os arquivos:
<br> - "SV.png"
<br> - "SV1.png"
<br> - "SV2.png"
<br> - "SV3.png"
<br> - "SV4.png"
<br> - "SV5.png"
<br> - "SV6.png"
<br> - "SV7.png"
<br><br>Você também pode continuar neste arquivo para as seções: 
<br> - **Sistema de Vendas - Coletando dados: Demo**
<br> - **Sistema de Vendas - Opções do Sistema: Demo**

## Sistema de Vendas - Coletando Dados: DEMO

Demonstração do programa em execução

```
Nome: Sistema de Vendas
Versão: 1.0
Criado por: Heitor Bisneto.
Copyright © 2020 | Heitor Bisneto. All rights reserved.

Digite o seu nome: Heitor
Hora inicial: 0
Minuto inicial: 0
Hora Final: 8
Minuto Final: 45
Gostaria de vender um produto? [S ou N]: S
Qual o valor do produto? 23.32
Gostaria de vender um produto? [S ou N]: S
Qual o valor do produto? 230.55
Gostaria de vender um produto? [S ou N]: N


-------------------------------------------------------------------------
------------------------- >>OPÇÕES DO SISTEMA<< -------------------------
-------------------------------------------------------------------------
>> INSIRA SOMENTE O NÚMERO DA OPÇÃO OU O NOME DA OPÇÃO:
-------------------------------------------------------------------------

-------------------------------------------------------------------------
>> ARQUIVO
-------------------------------------------------------------------------
(1) PrintRel = Imprimir Relatório
(2) SalvarRel = Salvar Relatório
(3) LerRel = Ler Relatório
-------------------------------------------------------------------------
>> CONVERTER
-------------------------------------------------------------------------
(4) ConvertToJSON = Converte o arquivo para JSON.
(5) ConvertToXML = Converte o arquivo para XML.
(6) LerJSON = Ler arquivo JSON.
(7) LerXML = Ler arquivo XML.
-------------------------------------------------------------------------
-------------------------------------------------------------------------

O que deseja fazer agora? |
```
## Sistema de Vendas - Opções do Sistema: Demo
Demonstração das opções do sistema após o sistema solicitar uma ação
<br><strong>1. Primeira Opção</strong>

```
O que deseja fazer agora? 1

---------- Relatório Diário ----------
Horas Trabalhadas: 8.75 hora(s)
Total de Vendas: 2 Venda(s)
Valor de Cada Venda: [23.32, 230.55]
Valor Total de Vendas: R$ 253.87
Média de Vendas por Hora: 0.22857142857142856 vendas por hora
---------- Relatório Diário ----------

Relatório impresso com sucesso!

-------------------------------------------------------------------------
------------------------- >>OPÇÕES DO SISTEMA<< -------------------------
-------------------------------------------------------------------------
>> INSIRA SOMENTE O NÚMERO DA OPÇÃO OU O NOME DA OPÇÃO:
-------------------------------------------------------------------------

-------------------------------------------------------------------------
>> ARQUIVO
-------------------------------------------------------------------------
(1) PrintRel = Imprimir Relatório
(2) SalvarRel = Salvar Relatório
(3) LerRel = Ler Relatório
-------------------------------------------------------------------------
>> CONVERTER
-------------------------------------------------------------------------
(4) ConvertToJSON = Converte o arquivo para JSON.
(5) ConvertToXML = Converte o arquivo para XML.
(6) LerJSON = Ler arquivo JSON.
(7) LerXML = Ler arquivo XML.
-------------------------------------------------------------------------
-------------------------------------------------------------------------

O que deseja fazer agora? |
```
<strong>2. Segunda Opção</strong>

```
O que deseja fazer agora? 2
Salvando Relatório...
Arquivo salvo com sucesso

-------------------------------------------------------------------------
------------------------- >>OPÇÕES DO SISTEMA<< -------------------------
-------------------------------------------------------------------------
>> INSIRA SOMENTE O NÚMERO DA OPÇÃO OU O NOME DA OPÇÃO:
-------------------------------------------------------------------------

-------------------------------------------------------------------------
>> ARQUIVO
-------------------------------------------------------------------------
(1) PrintRel = Imprimir Relatório
(2) SalvarRel = Salvar Relatório
(3) LerRel = Ler Relatório
-------------------------------------------------------------------------
>> CONVERTER
-------------------------------------------------------------------------
(4) ConvertToJSON = Converte o arquivo para JSON.
(5) ConvertToXML = Converte o arquivo para XML.
(6) LerJSON = Ler arquivo JSON.
(7) LerXML = Ler arquivo XML.
-------------------------------------------------------------------------
-------------------------------------------------------------------------

O que deseja fazer agora? |
```

<strong>3. Terceira Opção</strong>

```
---------- Relatório Diário ----------

Horas Trabalhadas: 8.75 hora(s)
Total de Vendas: 2 Venda(s)
Valor de Cada Venda: [23.32, 230.55]
Valor Total de Vendas: R$ 253.87
Média de Vendas por Hora: 0.22857142857142856 vendas por hora

---------- Relatório Diário ----------




-------------------------------------------------------------------------
------------------------- >>OPÇÕES DO SISTEMA<< -------------------------
-------------------------------------------------------------------------
>> INSIRA SOMENTE O NÚMERO DA OPÇÃO OU O NOME DA OPÇÃO:
-------------------------------------------------------------------------

-------------------------------------------------------------------------
>> ARQUIVO
-------------------------------------------------------------------------
(1) PrintRel = Imprimir Relatório
(2) SalvarRel = Salvar Relatório
(3) LerRel = Ler Relatório
-------------------------------------------------------------------------
>> CONVERTER
-------------------------------------------------------------------------
(4) ConvertToJSON = Converte o arquivo para JSON.
(5) ConvertToXML = Converte o arquivo para XML.
(6) LerJSON = Ler arquivo JSON.
(7) LerXML = Ler arquivo XML.
-------------------------------------------------------------------------
-------------------------------------------------------------------------

O que deseja fazer agora? |
```

<strong>4. Quarta Opção</strong>

```
O que deseja fazer agora? 4
Convertendo Arquivo JSON...
Salvando arquivo convertido...
Arquivo convertido com sucesso

-------------------------------------------------------------------------
------------------------- >>OPÇÕES DO SISTEMA<< -------------------------
-------------------------------------------------------------------------
>> INSIRA SOMENTE O NÚMERO DA OPÇÃO OU O NOME DA OPÇÃO:
-------------------------------------------------------------------------

-------------------------------------------------------------------------
>> ARQUIVO
-------------------------------------------------------------------------
(1) PrintRel = Imprimir Relatório
(2) SalvarRel = Salvar Relatório
(3) LerRel = Ler Relatório
-------------------------------------------------------------------------
>> CONVERTER
-------------------------------------------------------------------------
(4) ConvertToJSON = Converte o arquivo para JSON.
(5) ConvertToXML = Converte o arquivo para XML.
(6) LerJSON = Ler arquivo JSON.
(7) LerXML = Ler arquivo XML.
-------------------------------------------------------------------------
-------------------------------------------------------------------------

O que deseja fazer agora? |
```

<strong>5. Quinta Opção</strong>

```
O que deseja fazer agora? 5
Convertendo Arquivo XML...
Salvando arquivo convertido...
Arquivo convertido com sucesso

-------------------------------------------------------------------------
------------------------- >>OPÇÕES DO SISTEMA<< -------------------------
-------------------------------------------------------------------------
>> INSIRA SOMENTE O NÚMERO DA OPÇÃO OU O NOME DA OPÇÃO:
-------------------------------------------------------------------------

-------------------------------------------------------------------------
>> ARQUIVO
-------------------------------------------------------------------------
(1) PrintRel = Imprimir Relatório
(2) SalvarRel = Salvar Relatório
(3) LerRel = Ler Relatório
-------------------------------------------------------------------------
>> CONVERTER
-------------------------------------------------------------------------
(4) ConvertToJSON = Converte o arquivo para JSON.
(5) ConvertToXML = Converte o arquivo para XML.
(6) LerJSON = Ler arquivo JSON.
(7) LerXML = Ler arquivo XML.
-------------------------------------------------------------------------
-------------------------------------------------------------------------

O que deseja fazer agora? |
```

<strong>6. Sexta Opção</strong>

```
O que deseja fazer agora? 6

//
//  Criado por BISNETO on 3/8/2020.
//  Copyright © 2020 BISNETO. Todos os direitos reservados.
//
//  Esse arquivo foi convertido em JSON com o "Sistema de Vendas"
//  Dúvidas ou sugestões: http://github.com/hbisneto/
//

{
    "RelatorioDiario": {
       "HorasTrabalhadas": "8.75 hora(s)",
       "TotalDeVendas": "2 Venda(s)",
       "ValorDeCadaVenda": "[23.32, 230.55]",
       "ValorTotalDeVendas": "R$ 253.87",
       "MediaVendasHora": "0.22857142857142856 vendas por hora"
   }
}




-------------------------------------------------------------------------
------------------------- >>OPÇÕES DO SISTEMA<< -------------------------
-------------------------------------------------------------------------
>> INSIRA SOMENTE O NÚMERO DA OPÇÃO OU O NOME DA OPÇÃO:
-------------------------------------------------------------------------

-------------------------------------------------------------------------
>> ARQUIVO
-------------------------------------------------------------------------
(1) PrintRel = Imprimir Relatório
(2) SalvarRel = Salvar Relatório
(3) LerRel = Ler Relatório
-------------------------------------------------------------------------
>> CONVERTER
-------------------------------------------------------------------------
(4) ConvertToJSON = Converte o arquivo para JSON.
(5) ConvertToXML = Converte o arquivo para XML.
(6) LerJSON = Ler arquivo JSON.
(7) LerXML = Ler arquivo XML.
-------------------------------------------------------------------------
-------------------------------------------------------------------------

O que deseja fazer agora? |
```

<strong>7. Sétima Opção</strong>

```
O que deseja fazer agora? 7

<!--
    Criado por BISNETO on 3/8/2020.
    Copyright © 2020 BISNETO. Todos os direitos reservados.

    Esse arquivo foi convertido em XML com o "Sistema de Vendas"
    Dúvidas ou sugestões: http://github.com/hbisneto/
-->



<?xml version="1.0" encoding="UTF-8"?>
<RelatorioDiario>
       <HorasTrabalhadas> 8.75 </HorasTrabalhadas>
       <TotalDeVendas> 2 </TotalDeVendas>
       <ValorCadaVenda> [23.32, 230.55] </ValorCadaVenda>
       <ValorTotalVendas> 253.87 </ValorTotalVendas>
       <MediaVendasHora> 0.22857142857142856 </MediaVendasHora>
</RelatorioDiario>




-------------------------------------------------------------------------
------------------------- >>OPÇÕES DO SISTEMA<< -------------------------
-------------------------------------------------------------------------
>> INSIRA SOMENTE O NÚMERO DA OPÇÃO OU O NOME DA OPÇÃO:
-------------------------------------------------------------------------

-------------------------------------------------------------------------
>> ARQUIVO
-------------------------------------------------------------------------
(1) PrintRel = Imprimir Relatório
(2) SalvarRel = Salvar Relatório
(3) LerRel = Ler Relatório
-------------------------------------------------------------------------
>> CONVERTER
-------------------------------------------------------------------------
(4) ConvertToJSON = Converte o arquivo para JSON.
(5) ConvertToXML = Converte o arquivo para XML.
(6) LerJSON = Ler arquivo JSON.
(7) LerXML = Ler arquivo XML.
-------------------------------------------------------------------------
-------------------------------------------------------------------------

O que deseja fazer agora? |
```

#

Copyright © 2020 Heitor Bisneto. All rights reserved.
