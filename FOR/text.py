import math
import cmath
archivo = None
def cuadraticawpos(pos,a,b,c):
    if(a==0):
        if(b == 0):
            print('favor de verificar que el valor b no sea = a 0')
        else:
            print("El valor de X es "(-c/b))
    else:
        if(((b**2)-(4*a*c))<0):

            x1 = ((-b) + cmath.sqrt((b**2)-(4*a*c)))/ (2 * a)
            x2 = ((-b) - cmath.sqrt((b**2)-(4*a*c)))/ (2 * a)
        else:
            x1= ((-b) + math.sqrt((b**2)-(4*a*c)))/ (2 * a)
            x2= ((-b) - math.sqrt((b**2)-(4*a*c)))/ (2 * a)
    print('+===========================================')
    print('El valor del dato ',pos,' de x1= ',x1,' y de x2= ',x2)


try:
    archivo = open('text.txt')
except IOError:
  print ("ERROR este archivo no existe")

if archivo:
    file_opened = archivo.read().splitlines()
    for pos,line in enumerate(file_opened):
        splited = line.split('-')
        a = float(splited[0])
        b = float(splited[1])
        c = float(splited[2])
        cuadraticawpos(pos,a,b,c)
    archivo.close()
