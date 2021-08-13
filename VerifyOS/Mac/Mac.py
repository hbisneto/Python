# Mac File
import platform
import os

def Mac(SystemArray = [], ProcessorArray = []):

    # System Info
    OSName = str()
    OSVersionMajor = str()
    OSArchitecture = str()

    # Processor Info
    command = '/usr/sbin/sysctl -n machdep.cpu.brand_string'
    ProcInfo = os.popen(command).read().strip()
    ProcName = str()
    ProcModel = str()
    ProcFamily = str()
    ProcType = str()
    ProcFrequency = str()
    ProcArchitecture = str()

    # Code References
    Platform = platform.platform()
    PlatFormat = Platform.split('-')
    Processor = ProcInfo.split(' ')

    # Counters
    Count = 0
    ProcCount = 0

    # System Array
    for Data in PlatFormat:
        Count += 1
        SystemArray.append(Data)
        
        if Count == 1:
            OSName = SystemArray[Count-1]
        elif Count == 2:
             OSVersionMajor = SystemArray[Count-1]
        elif Count == 3:
             OSArchitecture = SystemArray[Count-1]
        elif Count == 4:
             ProcArchitecture = SystemArray[Count-1]

    # Processor Array
    for Data in Processor:
        ProcCount += 1
        ProcessorArray.append(Data)

        if ProcCount == 1:
            ProcName = ProcessorArray[ProcCount-1]
        if ProcCount == 2:
            ProcModel = ProcessorArray[ProcCount-1]
        if ProcCount == 3:
            ProcFamily = ProcessorArray[ProcCount-1]
        if ProcCount == 4:
            ProcType = ProcessorArray[ProcCount-1]
        if ProcCount == 12:
            ProcFrequency = ProcessorArray[ProcCount-1]

    # OS Output
    print("="*80)
    print(f'>> Sobre o Sistema: {OSName} <<')
    print("="*80)
    print(f'>> Nome do Sistema Operacional: {OSName} ')
    print(f'>> Versão do Sistem Operacional: {OSName} {OSVersionMajor}')
    print(f'>> Arquitetura do Sistema: {OSArchitecture}')

    # Processor Output
    print("="*80)
    print(f'>> Sobre o Processador ({ProcType}) <<')
    print("="*80)
    print(f'>> Nome do Processador: {ProcName} ')
    print(f'>> Modelo do Processador: {ProcModel} {ProcFamily}')
    print(f'>> Clock do Processador: {ProcFrequency}')
    print(f'>> Arquitetura do Processador: {ProcArchitecture}')

    ## Start App for Mac
    from Mac import MacApp
