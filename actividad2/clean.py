import os
def clear():
    clear=''
    if (os.name=='posix'):
        clear = lambda:os.system('clear')
    else:
        clear = lambda:os.system('cls')
    clear()
