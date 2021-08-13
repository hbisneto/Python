# VerifyOS

O sistema verifica o Sistema Operacional (Linux, Mac e Windows) e executa a função de acordo com o Sistema Operacional em que o Script está sendo executado.

- O programa também retorna as seguintes informações:

## Sobre o Sistema Operacional

- Nome do Sistema Operacional;
- Versão do Sistema Operacional;
- Arquitetura do Sistema Operacional;

## Sobre o Processador

- Nome do Processador;
- Modelo do Processador;
- Clock do Processador;
- Arquitetura do Processador;


> Observação: O programa ainda está em constante mudança no ambiente **Windows**. Por esse motivo, algumas informações sobre o Sistema Operacional e Processador ainda não foram implementadas.
O módulo de informações **sobre o Sistema Windows** será atualizada o mais breve possível.
<br> Para mais informações, fique atento às atualizações desse documento.

#

## Código de verificação de Sistema Operacional:

- Script responsável por detectar o ambiente em que o Script está sendo executado.

```
try:
    # Imported Libraries
    from sys import platform
    # Local Libraries
    from Linux import Linux
    from Mac import Mac
    from Windows import Windows
    from ErrorReport import ErrorList

    Platform = platform
except:
    ErrorList.ImportLib()

def Main():
    
    if Platform == "linux" or Platform == "linux2":
        # Linux
        Linux.Linux()
        
    elif Platform == "darwin":
        # Mac
        Mac.Mac()
        
    elif Platform == "win32":
        # Windows
        Windows.Windows()
        
Main()
```

## Windows

- Código executado caso o Sistema Operacional seja **Windows**:

```
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
```

Output:

```
Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 11:29:23)
[MSC v.1927 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
============= RESTART: C:\Users\Heitor\Desktop\Verify OS\VerifyOS.py =============
================================================================================
>> Windows <<
================================================================================
>> Nome do Sistema Operacional: Windows 10
>> Versão do Sistema Operacional: 10.0.19041
>> Service Pack: SP0

================================================================================
[VerifyOS for Windows] - Em execução...
================================================================================
```

## macOS

- Código executado caso o Sistema Operacional seja **macOS**:

```
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
```

Output:

```
Python 3.9.0 (v3.9.0:9cf6752276, Oct  5 2020, 11:29:23) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
============= RESTART: /Users/heitor/Desktop/Verify OS/VerifyOS.py =============
================================================================================
>> Sobre o Sistema: macOS <<
================================================================================
>> Nome do Sistema Operacional: macOS 
>> Versão do Sistem Operacional: macOS 10.11.6
>> Arquitetura do Sistema: x86_64
================================================================================
>> Sobre o Processador (CPU) <<
================================================================================
>> Nome do Processador: Intel(R) 
>> Modelo do Processador: Core(TM)2 Duo
>> Clock do Processador: 2.40GHz
>> Arquitetura do Processador: i386

================================================================================
[VerifyOS for Mac] - Em execução...
================================================================================
```

## Linux

- Código executado caso o Sistema Operacional seja **Linux**:

```
import platform as p # Alias para o módulo plataforma
import pprint

def Linux():

    # Abre para leitura o arquivo que contém o nome do SO Linux
    with open("/etc/lsb-release", "r") as l:
        OSName = l.readlines()
    OSName = OSName[3].strip("DISTRIB_DESCRIPTION='")

    # Verifica a versão de Kernel do SO
    with open("/proc/version", "r") as l:
        OSInfoVersion = l.readlines()
    OSVersionKernel = OSInfoVersion[0].split()
    OSVersionKernel = OSVersionKernel[2]
    
    # Verfica a arquitetura do processador se é x86 ou x64
    OSArchitecture = p.architecture()[0]

    # Abre um arquivo de informações técnicas do processador, por exemplo: o nome
    with open("/proc/cpuinfo", "r")  as f:
        OSProcessors = f.readlines()

    # Retira a expressão model name e as tabulações
    OSProcessorsInfoAllInOne = OSProcessors[4].strip("model name  : 	:")

    # Retira espaços entre as informações do nome completo do processador e transforma em lista
    OSProcessors = OSProcessorsInfoAllInOne.strip("  ").split()

    # Pega o nome da marca do processador
    ProcessorName = OSProcessors[0]
    # Pega o nome da família e geração do processador
    ProcessorModel = OSProcessors[2]
    # Pega a informação de Frequência
    ProcessorClock = OSProcessors[-1]

    # Verifica a arquitetura do Sistema Operacional: x86, x64, x86_64
    OSMachine = p.machine()

    # OS Output
    print("="*80)
    print(f'>> Sobre o Sistema: {OSName}', end="")
    print("="*80)
    print(f'>> Nome do Sistema Operacional: {OSName}', end="")
    print(f'>> Versão do Kernel: {OSVersionKernel}')
    print(f'>> Arquitetura do Sistema: {OSMachine}')
    # Processor Output
    print("="*80)
    print(f'>> Sobre o Processador: {OSProcessorsInfoAllInOne}', end="")
    print("="*80)
    print(f'>> Nome do Processador: {ProcessorName}')
    print(f'>> Modelo do Processador: {ProcessorModel}')
    print(f'>> Clock do Processador: {ProcessorClock}')
    print(f'>> Arquitetura do Processador: {OSArchitecture}')

    ## Start App for Linux
    from Linux import LinuxApp
```

Output:

```
rot@Rot /information collapsed/Users/ROT/Desktop/Verify OS $ python3.9 VerifyOS.py
================================================================================
>> Sobre o Sistema: "Linux Lite 5.0"
================================================================================
>> Nome do Sistema Operacional: "Linux Lite 5.0"
>> Versão do Kernel: 5.4.0-65-generic
>> Arquitetura do Sistema: x86_64
================================================================================
>> Sobre o Processador: Intel(R) Core(TM) i5-3210M CPU @ 2.50GHz
================================================================================
>> Nome do Processador: Intel(R)
>> Modelo do Processador: i5-3210M
>> Clock do Processador: 2.50GHz
>> Arquitetura do Processador: 64bit

================================================================================
[VerifyOS for Linux] - Em execução...
================================================================================
```

# 

# Agradecimentos

- [Jonathan Batista de Oliveira](https://github.com/Vsg5662 "VSG5226 on Github"): Desenvolvedor da função **Linux()** em **["Linux.py"](https://github.com/hbisneto/Python/blob/main/Verify%20OS/Linux/Linux.py "Linux.py")**
- [Danilo Henrique](https://github.com/danilohbp "DaniloHBP on Github"): Desenvolvedor da função **Linux()** em **["Linux.py"](https://github.com/hbisneto/Python/blob/main/Verify%20OS/Linux/Linux.py "Linux.py")**