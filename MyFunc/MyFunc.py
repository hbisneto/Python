### MyFunc - String Exemple

def Func1(msg, nome):
    print(f'{msg}, {nome}!')

Func1("Olá", "Fulano")

def Func2(nome = 'Fulano', msg = 'Olá'):
    print('{}, {}!'.format(msg, nome))

Func2()
    
def Func3(nome, msg = 'Olá'):
    print(f'{msg}, {nome}!')

Func3("Fulano")
