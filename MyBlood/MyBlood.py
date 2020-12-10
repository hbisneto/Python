from datetime import date
AnoAtual = date.today().year
SoftwareName = "MYBLOOD"

print("Nome:", SoftwareName)
print("Versão: 1.1")
print("Criado por: Heitor Bisneto")
print("Copyright © 2020 -", AnoAtual, "Bisneto. All rights reserved.")
print("")

AppName = "MyBlood"
TypeA = "Indivíduos têm o antígeno A na superfície de suas hemácias, e o soro sanguíneo\ncontido na Imunoglobulina M são anticorpos contra o antígeno B.\nAssim, uma pessoa do grupo A pode receber sangue só de pessoas dos grupos A ou O\n(com A preferível), e só pode doar sangue para indivíduos com o tipo A ou AB."
TypeB = "Indivíduos têm o antígeno B na superfície de suas hemácias, e o soro sanguíneo\ncontido na Imunoglobulina M são anticorpos contra o antígeno A.\nAssim, alguém do grupo B pode receber sangue só de indivíduos de grupos B ou O\n(com B preferível), e pode doar sangue para indivíduos com o tipo B ou AB."
TypeAB = "Indivíduos têm tanto antígenos A quanto B na superfície de suas hemácias, e o\nsoro sanguíneo deles não contem quaisquer anticorpos dos antígenos\nA ou B. Assim, alguém com tipo de sangue AB pode receber sangue de qualquer\ngrupo (com AB preferível), mas só pode doar sangue para outros com o tipo AB."
TypeO = "Indivíduos não possuem antígenos nem A ou B na superfície de suas hemácias\n(dai o 0 usado por alguns autores), mas o soro sanguíneo deles contém\nImunoglobulina M com anticorpos anti-A e anti-B contra os antígenos A e B.\nPortanto, alguém do grupo O pode receber sangue só de alguém do grupo O, mas pode doar sangue para pessoas com qualquer grupo ABO (ou seja, A, B, O ou AB).\nSe alguém precisar de uma transfusão de sangue em uma emergência, e se o tempo necessário para testar o tipo de sangue causaria um atraso prejudicial, o sangue O- (O Negativo) pode ser administrado."

UserName = str(input("<" + AppName + "> Insira o seu nome: "))
if UserName == "":
    UserName = "Usuário Não Identificado"

BloodType = str(input("<" + AppName + "> Qual o seu tipo sanguineo: "))

# Tipo sanguineo A+:
# Pode Doar Para: AB+ e A+
# Pode Receber de: A+, A-, O+ e O-

if BloodType == "A":
    print("<" + AppName + "> Seu tipo sanguineo é " + BloodType + "+ ou " + BloodType + "-?")
    print("<" + AppName + "> [A]: " + BloodType + "+?")
    print("<" + AppName + "> [B]: " + BloodType + "-?")
    BloodProtein = str(input("<" + UserName + "> "))
    if BloodProtein == "A":
        BloodProtein = "+"
        print()
        print("Seu tipo sanguíneo é: " + BloodType + BloodProtein)
        print()
        print("Grupo sanguíneo A+:")
        print(TypeA)
        print()
        print("Pode Doar Para:")
        print("A+")
        print("AB+")
        print()
        print("Pode Receber Doação de:")
        print("A+")
        print("A-")
        print("O+")
        print("O-")
        
# Tipo sanguineo A-:
# Pode doar para: A+, A-, AB+ e AB-
# Pode receber de: A- e O-

    elif BloodProtein == "B":
        BloodProtein = "-"
        print()
        print("Seu tipo sanguíneo é: " + BloodType + BloodProtein)
        print()
        print("Grupo sanguíneo A-:")
        print(TypeA)
        print()
        print("Pode Doar Para:")
        print("A+")
        print("A-")
        print("AB+")
        print("AB-")
        print()
        print("Pode Receber Doação de:")
        print("A-")
        print("O-")

# Tipo sanguineo B+:
# Pode doar para: B+ e AB+
# Pode receber de: B+, B-, O+ e O-

if BloodType == "B":
    print("<" + AppName + "> Seu tipo sanguineo é " + BloodType + "+ ou " + BloodType + "-?")
    print("<" + AppName + "> [A]: " + BloodType + "+?")
    print("<" + AppName + "> [B]: " + BloodType + "-?")
    BloodProtein = str(input("<" + UserName + "> "))
    if BloodProtein == "A":
        BloodProtein = "+"
        print()
        print("Seu tipo sanguíneo é: " + BloodType + BloodProtein)
        print()
        print("Grupo sanguíneo B+:")
        print(TypeB)
        print()
        print("Pode Doar Para:")
        print("B+")
        print("AB+")
        print()
        print("Pode Receber Doação de:")
        print("B+")
        print("B-")
        print("O+")
        print("O-")

# Tipo sanguineo B-:
# Pode doar para: B+, B-, AB+ e AB-
# Pode receber de: B- e O-
        
    elif BloodProtein == "B":
        BloodProtein = "-"
        print()
        print("Seu tipo sanguíneo é: " + BloodType + BloodProtein)
        print()
        print("Grupo sanguíneo B-:")
        print(TypeB)
        print()
        print("Pode Doar Para:")
        print("B+")
        print("B-")
        print("AB+")
        print("AB-")
        print()
        print("Pode Receber Doação de:")
        print("B-")
        print("O-")
        
# Tipo sanguineo AB+:
# Pode doar para: AB+
# Pode receber doação de: A+, B+, O+, AB+, A-, B-, O- e AB-

if BloodType == "AB":
    print("<" + AppName + "> Seu tipo sanguineo é " + BloodType + "+ ou " + BloodType + "-?")
    print("<" + AppName + "> [A]: " + BloodType + "+?")
    print("<" + AppName + "> [B]: " + BloodType + "-?")
    BloodProtein = str(input("<" + UserName + "> "))
    if BloodProtein == "A":
        BloodProtein = "+"
        print()
        print("Seu tipo sanguíneo é: " + BloodType + BloodProtein)
        print()
        print("Grupo sanguíneo AB+:")
        print(TypeAB)
        print()
        print("Pode Doar Para:")
        print("AB+")
        print()
        print("Pode Receber Doação de:")
        print("A+")
        print("A-")
        print("B+")
        print("B-")
        print("AB+")
        print("AB-")
        print("O+")
        print("O-")

# Tipo sanguineo AB-:
# Pode doar para: AB+ e AB-
# Pode receber doação de: A-, B-, O- e AB-

    elif BloodProtein == "B":
        BloodProtein = "-"
        print()
        print("Seu tipo sanguíneo é: " + BloodType + BloodProtein)
        print()
        print("Grupo sanguíneo AB-:")
        print(TypeAB)
        print()
        print("Pode Doar Para:")
        print("AB+")
        print("AB-")
        print()
        print("Pode Receber Doação de:")
        print("A-")
        print("B-")
        print("AB-")
        print("O-")


# Tipo sanguineo O+:
# Pode doar para: A+, B+, O+ e AB+
# Pode receber doação de: O+ e O-

if BloodType == "O":
    print("<" + AppName + "> Seu tipo sanguineo é " + BloodType + "+ ou " + BloodType + "-?")
    print("<" + AppName + "> [A]: " + BloodType + "+?")
    print("<" + AppName + "> [B]: " + BloodType + "-?")
    BloodProtein = str(input("<" + UserName + "> "))
    if BloodProtein == "A":
        BloodProtein = "+"
        print()
        print("Seu tipo sanguíneo é: " + BloodType + BloodProtein)
        print()
        print("Grupo sanguíneo O+:")
        print(TypeO)
        print()
        print("Pode Doar Para:")
        print("A+")
        print("B+")
        print("AB+")
        print("O+")
        print()
        print("Pode Receber Doação de:")
        print("O+")
        print("O-")

# Tipo sanguineo O-:
# Pode doar para: A+, B+, O+, AB+, A-, B-, O- e AB-
# Pode receber doação de: O-

    elif BloodProtein == "B":
        BloodProtein = "-"
        print()
        print("Seu tipo sanguíneo é: " + BloodType + BloodProtein)
        print()
        print("Grupo sanguíneo O-:")
        print(TypeO)
        print()
        print("Pode Doar Para:")
        print("A+")
        print("A-")
        print("B+")
        print("B-")
        print("AB+")
        print("AB-")
        print("O+")
        print("O-")
        print()
        print("Pode Receber Doação de:")
        print("O-")
        
print()
print()
print("Você não poderá doar sangue se:")
print()
print("» Tiver idade inferior a 16 anos ou superior a 69 anos.")
print()
print("Obs: O limite superior para a primeira doação é 60 anos. Quem tem 61 anos ou mais e nunca doou está inapto.")
print()
print("» Tiver peso inferior a 50 quilos.")
print("» Estiver com anemia no teste realizado imediatamente antes da doação.")
print("» Estiver com hipertensão ou hipotensão arterial no momento da doação.")
print("» Estiver com aumento ou diminuição dos batimentos cardíacos no momento da doação.")
print("» Estiver com febre no dia da doação.")
print("» Estiver grávida.")
print("» Estiver amamentando, a menos que o parto tenha ocorrido há mais de 12 meses.")
print()
print("Obs: O doador não poderá doar se vier acompanhado de crianças menores de 13 anos sem a presença de um outro adulto para cuidar delas.")
