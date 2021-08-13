from datetime import date
AnoAtual = date.today().year
SoftwareName = "CALCULADORA - DEMO"
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

# Adição: DEMO
print("=" * 35)
print("=" * 10, "Adição - Demo", "=" * 10)
print("=" * 35)
try: 
    N1 = 9
    print("Insira o primeiro número: 9")
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
        Operacao = "+"
        print("Digite o simbolo da operação de acordo com o exemplo acima: +")
        if Operacao == "R" or Operacao == "r":
            N2 = 0.5
            Calculo = N1 ** N2
            print("\nA Raiz Quadrada de", N1, "é", Calculo)
        else:
            try:
                N2 = 1
                print("Insira o segundo número: 1")
                if Operacao == "+":
                    Calculo = N1+N2
                    print("\nResultado da Adição:", Calculo)
                    print()
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

# Subtração: DEMO
print("=" * 38)
print("=" * 10, "Subtração - Demo", "=" * 10)
print("=" * 38)
try: 
    N1 = 9
    print("Insira o primeiro número: 9")
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
        Operacao = "-"
        print("Digite o simbolo da operação de acordo com o exemplo acima: -")
        if Operacao == "R" or Operacao == "r":
            N2 = 0.5
            Calculo = N1 ** N2
            print("\nA Raiz Quadrada de", N1, "é", Calculo)
        else:
            try:
                N2 = 1
                print("Insira o segundo número: 1")
                if Operacao == "+":
                    Calculo = N1+N2
                    print("\nResultado da Adição:", Calculo)
                elif Operacao == "-":
                    Calculo = N1-N2
                    print("\nResultado da Subtração:", Calculo)
                    print()
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
    
# Multiplicação: DEMO
print("=" * 42)
print("=" * 10, "Multiplicação - Demo", "=" * 10)
print("=" * 42)
try: 
    N1 = 9
    print("Insira o primeiro número: 9")
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
        Operacao = "*"
        print("Digite o simbolo da operação de acordo com o exemplo acima: *")
        if Operacao == "R" or Operacao == "r":
            N2 = 0.5
            Calculo = N1 ** N2
            print("\nA Raiz Quadrada de", N1, "é", Calculo)
        else:
            try:
                N2 = 1
                print("Insira o segundo número: 1")
                if Operacao == "+":
                    Calculo = N1+N2
                    print("\nResultado da Adição:", Calculo)
                elif Operacao == "-":
                    Calculo = N1-N2
                    print("\nResultado da Subtração:", Calculo)
                elif Operacao == "*":
                    Calculo = N1*N2
                    print("\nResultado da Multiplicação:", Calculo)
                    print()
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
    
# Divisão: DEMO
print("=" * 36)
print("=" * 10, "Divisão - Demo", "=" * 10)
print("=" * 36)
try: 
    N1 = 9
    print("Insira o primeiro número: 9")
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
        Operacao = "/"
        print("Digite o simbolo da operação de acordo com o exemplo acima: /")
        if Operacao == "R" or Operacao == "r":
            N2 = 0.5
            Calculo = N1 ** N2
            print("\nA Raiz Quadrada de", N1, "é", Calculo)
        else:
            try:
                N2 = 1
                print("Insira o segundo número: 1")
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
                    print()
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
# Potenciação: DEMO
print("=" * 40)
print("=" * 10, "Potênciação - Demo", "=" * 10)
print("=" * 40)
try: 
    N1 = 9
    print("Insira o primeiro número: 9")
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
        Operacao = "**"
        print("Digite o simbolo da operação de acordo com o exemplo acima: R")
        if Operacao == "R" or Operacao == "r":
            N2 = 0.5
            Calculo = N1 ** N2
            print("\nA Raiz Quadrada de", N1, "é", Calculo)
        else:
            try:
                N2 = 1
                print("Insira o segundo número: 1")
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
                    print()
            except:
                print("\n>> SEGUNDO CARACTERE INCORRETO:")
                print("O segundo caractere digitado não é um número. Verifique o digito inserido e execute o programa novamente")
    except:
        print("\n>> OPERADOR INVÁLIDO:")
        print("Operação digitada incorretamente")
except:
    print("\n>> PRIMEIRO CARACTERE INCORRETO:")
    print("O primeiro caractere digitado não é um número. Verifique o digito inserido e execute o programa novamente")
# Radiciação: DEMO
print("=" * 39)
print("=" * 10, "Radiciação - Demo", "=" * 10)
print("=" * 39)
try: 
    N1 = 9
    print("Insira o primeiro número: 9")
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
        Operacao = "R"
        print("Digite o simbolo da operação de acordo com o exemplo acima: R")
        if Operacao == "R" or Operacao == "r":
            N2 = 0.5
            Calculo = N1 ** N2
            print("\nA Raiz Quadrada de", N1, "é", Calculo)
            print()
        else:
            try:
                N2 = 1
                print("Insira o segundo número: 1")
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
