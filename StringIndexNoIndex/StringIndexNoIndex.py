SArray = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ]

UserInput = str(input(">> Escreva aqui: "))

def Index():
    Codigo = ''
    Count = 0
    for i in UserInput.upper():
        for j in SArray:
            Count += 1
            if i == j:
                Codigo += str(Count-1)
                Count = 0
                break
    print(f'>> Retorno (De acordo com o index): {Codigo}')

def NoIndex():
    Codigo = ''
    Count = 0
    for i in UserInput.upper():
        for j in SArray:
            Count += 1
            if i == j:
                Codigo += str(Count)
                Count = 0
                break
    print(f'>> Retorno (Não depende do index): {Codigo}')


Index()
NoIndex()
