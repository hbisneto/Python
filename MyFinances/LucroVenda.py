def App():
    print("################################################################################")
    print("##                      Módulo: LucroVenda.py                                 ##")
    print("##                      Versão: 1.2                                           ##")
    print("################################################################################")
    # Use somente números no campo. Não use vírgulas. Use Ponto final no lugar de vírgulas.
    ValorTotal = float(input("<Valor Total do Produto> "))
    # Use somente números. Não use sinal de porcentagem
    Margem = float(input("<Margem de Lucro> "))
    Calculo = (((ValorTotal/100)* Margem) + ValorTotal)

    print("<Valor de Venda> R$", Calculo)
