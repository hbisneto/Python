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
