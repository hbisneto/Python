from datetime import date
CurrentYear = date.today().year
SoftwareName = "Copyright App"
Version = "1.0.0.0"
CopyrightName = "Heitor Bisneto."

print("Nome:", SoftwareName)
print("Versão:", Version)
print("Criado por:", CopyrightName)
if CurrentYear == 2020:
    print("Copyright ©", CurrentYear, "|", CopyrightName, "All rights reserved.")
else:
    print("Copyright © 2020 -", CurrentYear, "|", CopyrightName, "All rights reserved.")
print("")
