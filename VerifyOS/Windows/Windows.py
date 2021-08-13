# Windows File
import platform

def Windows(SystemArray = []):
    OSName = str()
    OSVersionMajor = str()
    OSVersion = str()
    OSServicePack = str()
    
    Platform = platform.platform()
    PlatFormat = Platform.split('-')
    
    Count = 0
    for Data in PlatFormat:
        Count += 1
        SystemArray.append(Data)
        
        if Count == 1:
            OSName = SystemArray[Count-1]
        elif Count == 2:
             OSVersionMajor = SystemArray[Count-1]
        elif Count == 3:
             OSVersion = SystemArray[Count-1]
        elif Count == 4:
             OSServicePack = SystemArray[Count-1]

    print("="*80)
    print(f'>> {OSName} <<')
    print("="*80)
    print(f'>> Nome do Sistema Operacional: {OSName} {OSVersionMajor}')
    print(f'>> Versão do Sistema Operacional: {OSVersion}')
    print(f'>> Service Pack: {OSServicePack}')

    ## Start App for Windows
    from Windows import WindowsApp
