import Copyright

try: 
    N1 = float(input(">> Insira o primeiro número: "))
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
        Operacao = str(input(">> Digite o simbolo da operação de acordo com o exemplo acima: "))
        if Operacao == "R" or Operacao == "r":
            N2 = 0.5
            Calculo = N1 ** N2
            print("\n>> A Raiz Quadrada de", N1, "é", Calculo)
        else:
            try:
                N2 = float(input(">> Insira o segundo número: "))
                if Operacao == "+":
                    Calculo = N1+N2
                    print("\n>> Resultado da Adição:", Calculo)
                elif Operacao == "-":
                    Calculo = N1-N2
                    print("\n>> Resultado da Subtração:", Calculo)
                elif Operacao == "*":
                    Calculo = N1*N2
                    print("\n>> Resultado da Multiplicação:", Calculo)
                elif Operacao == "/":
                    Calculo = N1/N2
                    print("\n>> Resultado da Divisão:", Calculo)
                elif Operacao == "**":
                    Calculo = N1**N2
                    print("\n>> Resultado da Potênciação:", Calculo)
            except:
                print("\n>> SEGUNDO CARACTERE INCORRETO:")
                print("> O segundo caractere digitado não é um número. Verifique o digito inserido e execute o programa novamente")
    except:
        print("\n>> OPERADOR INVÁLIDO:")
        print("> Operação digitada incorretamente")
except:
    print("\n>> PRIMEIRO CARACTERE INCORRETO:")
    print("> O primeiro caractere digitado não é um número. Verifique o digito inserido e execute o programa novamente")
