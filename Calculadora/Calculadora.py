from datetime import date
AnoAtual = date.today().year
SoftwareName = "CALCULADORA"
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

try: 
    N1 = float(input("Insira o primeiro número: "))
    print()

    print("-" * 10, "Lista de operações", "-" * 10)
    print("Potência = **")
    print("Raiz Quadrada = R ou r")
    print("Multiplicação = *")
    print("Divisão = /")
    print("Adição = +")
    print("Subtração = -")
    print("-" * 10, "Lista de operações", "-" * 10)
    print()
    try:
        Operacao = str(input("Digite o simbolo da operação de acordo com o exemplo acima: "))
        if Operacao == "R" or Operacao == "r":
            N2 = 0.5
            Calculo = N1 ** N2
            print("\nA Raiz Quadrada de", N1, "é", Calculo)
        else:
            try:
                N2 = float(input("Insira o segundo número: "))
                if Operacao == "+":
                    Calculo = N1+N2
                    print("\nResultado da Adição:", Calculo)
                elif Operacao == "-":
                    Calculo = N1-N2
                    print("\nResultado da Subtração:", Calculo)
                elif Operacao == "*":
                    Calculo = N1*N2
                    print("\nResultado da Multiplicação:", Calculo)
                elif Operacao == "/":
                    Calculo = N1/N2
                    print("\nResultado da Divisão:", Calculo)
                elif Operacao == "**":
                    Calculo = N1**N2
                    print("\nResultado da Potênciação:", Calculo)
            except:
                print("\n>> SEGUNDO CARACTERE INCORRETO:")
                print("O segundo caractere digitado não é um número. Verifique o digito inserido e execute o programa novamente")
    except:
        print("\n>> OPERADOR INVÁLIDO:")
        print("Operação digitada incorretamente")
except:
    print("\n>> PRIMEIRO CARACTERE INCORRETO:")
    print("O primeiro caractere digitado não é um número. Verifique o digito inserido e execute o programa novamente")
