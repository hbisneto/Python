import Copyright
import LucroVenda

Run = int()

def App():
    print()
    print(">> Menu")
    print("-" * 80)
    print(">> 1. Calculadora de Lucros")
    print("- Calcula o lucro de acordo com o valor de um produto")
    print(">> 2. Calculadora de Lucros II")
    print("- Calcula o lucro de acordo com as despesas de fabricação")
    print("-" * 80)
    OptApp = int(input(">> Qual app gostaria de abrir: "))
    Run = OptApp
    print("-" * 80)

    if Run == 1:
        LucroVenda.App()
    elif Run == 2:
        import LucroDespesa
App()
