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

