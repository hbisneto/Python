from datetime import date
AnoAtual = date.today().year
SoftwareName = "CALCULADORA DE LUCROS"

print("Nome:", SoftwareName)
print("Versão: 1.1")
print("Criado por: Heitor Bisneto")
print("Copyright © 2020 -", AnoAtual, "Bisneto. All rights reserved.")
print("")
# Use somente números no campo. Não use vírgulas. Use Ponto final no lugar de vírgulas.
ValorTotal = float(input("<Valor Total do Produto> "))
# Use somente números. Não use sinal de porcentagem
Margem = float(input("<Margem de Lucro> "))
Calculo = (((ValorTotal/100)* Margem) + ValorTotal)

print("<Valor de Venda> R$", Calculo)
