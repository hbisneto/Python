print("=" * 15, "PyGame Copyright", "=" * 15)
from pygame import mixer
print("=" * 15, "PyGame Copyright", "=" * 15)
print()

from datetime import date
AnoAtual = date.today().year
SoftwareName = "PLAY SONG"
Version = "1.1"
CopyrightName = "Heitor Bisneto."

print("Nome:", SoftwareName)
print("Versão:", Version)
print("Criado por:", CopyrightName)
if AnoAtual == 2021:
    print("Copyright ©", AnoAtual, "|", CopyrightName, "All rights reserved.")
else:
    print("Copyright © 2021 -", AnoAtual, "|", CopyrightName, "All rights reserved.")
print("")

print("=" * 15, "Play Song", "=" * 15)
Song = int()

def Opcoes():    
    print(">> Opções de sons:\n")
    print(">> 1. Boing")
    print(">> 2. Ding")
    print(">> 3. Drop")
    print(">> 4. Here You Go")
    print(">> 5. Hi")
    print(">> 6. Incoming Call")
    print(">> 7. Knock Brush")
    print(">> 8. Plink")
    print(">> 9. Tada")
    print(">> 10. Whoa")
    print(">> 11. Wow")
    print(">> 12. Yoink")
    print()

def PlaySong():
    mixer.init()
        
    if Song == 1:
        print("> Tocando 'Boing'...")
        mixer.music.load('Notification/Boing.mp3')
        mixer.music.play()
        print()
        
    elif Song == 2:
        print("> Tocando 'Ding'...")
        mixer.music.load('Notification/Ding.mp3')
        mixer.music.play()
        print()
        
    elif Song == 3:
        print("> Tocando 'Drop'...")
        mixer.music.load('Notification/Drop.mp3')
        mixer.music.play()
        print()
        
    elif Song == 4:
        print("> Tocando 'Here You Go'...")
        mixer.music.load('Notification/HereYouGo.mp3')
        mixer.music.play()
        print()
        
    elif Song == 5:
        print("> Tocando 'Hi'...")
        mixer.music.load('Notification/Hi.mp3')
        mixer.music.play()
        print()
        
    elif Song == 6:
        print("> Tocando 'Incoming Call'...")
        mixer.music.load('Notification/IncomingCall.mp3')
        mixer.music.play()
        print()
        
    elif Song == 7:
        print("> Tocando 'Knock Brush'...")
        mixer.music.load('Notification/KnockBrush.mp3')
        mixer.music.play()
        print()
        
    elif Song == 8:
        print("> Tocando 'Plink'...")
        mixer.music.load('Notification/Plink.mp3')
        mixer.music.play()
        print()
        
    elif Song == 9:
        print("> Tocando 'Tada'...")
        mixer.music.load('Notification/Tada.mp3')
        mixer.music.play()
        print()
        
    elif Song == 10:
        print("> Tocando 'Whoa'...")
        mixer.music.load('Notification/Whoa.mp3')
        mixer.music.play()
        print()
        
    elif Song == 11:
        print("> Tocando 'Wow'...")
        mixer.music.load('Notification/Wow.mp3')
        mixer.music.play()
        print()
        
    elif Song == 12:
        print("> Tocando 'Yoink'...")
        mixer.music.load('Notification/Yoink.mp3')
        mixer.music.play()
        print()

    else:
        print(">> Opção não disponível no momento.")
        
Opcoes()
while True:
    Opcao = int(input(">> Escolha um número: "))
    Song = Opcao
    print()
    PlaySong()
    Opcoes()
