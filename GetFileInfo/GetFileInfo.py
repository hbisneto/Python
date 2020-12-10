import time
import os
from datetime import date
AnoAtual = date.today().year
SoftwareName = "GetFileInfo"

print("Nome:", SoftwareName)
print("Versão: 1.2")
print("Criado por: Heitor Bisneto")
print("Copyright © 2020 -", AnoAtual, "Bisneto. All rights reserved.")
print("")
Separator = ("=" * 20)
print(Separator + " " + SoftwareName + " " + Separator)
print()

MyDir = 'C:/'
with os.scandir(MyDir) as entries:
    for entry in entries:
        if entry.is_file():
            Criado = time.strftime('%d %m %Y', time.gmtime(os.stat(entry).st_ctime))
            Modificado = time.strftime('%d %m %Y', time.gmtime(os.path.getmtime(entry)))

            print("Nome do arquivo: ", entry.name)
            print("Criado em: ", Criado)
            print("Modificado em: ", Modificado)
            print()
