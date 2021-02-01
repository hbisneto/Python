from datetime import date
CurrentYear = date.today().year
SoftwareName = "SetCarModels"
Version = "1.0.0.0"
CopyrightName = "Heitor Bisneto."

print(f'Nome: {SoftwareName}')
print(f'Versão: {Version}')
print(f'Criado por: {CopyrightName}')

if CurrentYear == 2021:
    print(f'Copyright © {CurrentYear} | {CopyrightName} All Rights Reserved.')
else:
    print(f'Copyright © 2021 - {CurrentYear} | {CopyrightName} All Rights Reserved.')
print()

MarcaCarro = str(input("Digite a marca de um carro: "))

# Funções que serão chamadas de acordo com a escolha do usuário
def Ford():
    Ford.Marca = "Ford"
    Ford.Carros = {"Fusion", "Focus", "Ka", "Edge", "Mustang"}
    print(f'>> Carros da {Ford.Marca}: {Ford.Carros}')

def Audi():
    Audi.Marca = "Audi"
    Audi.Carros = {"A3", "A4", "Q3", "Q5", "TT"}
    print(f'>> Carros da {Audi.Marca}: {Audi.Carros}')

def Volkswagen():
    Volkswagen.Marca = "Volkswagen"
    Volkswagen.Carros = {"Polo", "Gol", "Golf", "Nivus", "Voyage"}
    print(f'>> Carros da {Volkswagen.Marca}: {Volkswagen.Carros}')

def Ferrari():
    Ferrari.Marca = "Ferrari"
    Ferrari.Carros = {"Portofino", "488", "Roma", "812", "GTC4"}
    print(f'>> Carros da {Ferrari.Marca}: {Ferrari.Carros}')

# Tomada de decisão (Estrutura de Seleção)
if MarcaCarro == "1" or MarcaCarro == "Ford" or MarcaCarro == "ford":
    Ford()
elif MarcaCarro == "2" or MarcaCarro == "Audi" or MarcaCarro == "audi":
    Audi()
elif MarcaCarro == "3" or MarcaCarro == "Volkswagen" or MarcaCarro == "volkswagen":
    Volkswagen()
elif MarcaCarro == "4" or MarcaCarro == "Ferrari" or MarcaCarro == "ferrari":
    Ferrari()
