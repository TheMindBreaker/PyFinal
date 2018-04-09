import cleaner
_file ='log.txt'
try:
    open_file = open(_file,'x')
except IOError:
    print('El archivo no esta disponible')
cleaner.clear()
print("""

""")
