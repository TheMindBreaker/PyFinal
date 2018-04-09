import math
import cmath

logo = """

T)tttttt h)                  M)mm mmm  ##              d) B)bbbb                           k)                           X)    xx Y)    yy Z)zzzzzz
   T)    h)                 M)  mm  mm                 d) B)   bb                          k)                            X)  xx   Y)  yy        Z)
   T)    h)HHHH  e)EEEEE    M)  mm  mm i) n)NNNN   d)DDDD B)bbbb    r)RRR  e)EEEEE a)AAAA  k)  KK e)EEEEE  r)RRR          X)xx     Y)yy       Z)
   T)    h)   HH e)EEEE     M)  mm  mm i) n)   NN d)   DD B)   bb  r)   RR e)EEEE   a)AAA  k)KK   e)EEEE  r)   RR         X)xx      Y)       Z)
   T)    h)   HH e)         M)      mm i) n)   NN d)   DD B)    bb r)      e)      a)   A  k) KK  e)      r)         **  X)  xx     Y)     Z)
   T)    h)   HH  e)EEEE    M)      mm i) n)   NN  d)DDDD B)bbbbb  r)       e)EEEE  a)AAAA k)  KK  e)EEEE r)         ## X)    xx    Y)    Z)zzzzzz
===================================================================================================================================================
"""

print(logo)
while True:
    try:
        a = float(input("Ingresa valor A: "))
        b = float(input("Ingresa valor B: "))
        c = float(input("Ingresa valor C: "))
    except ValueError:
        print("Error valor no es un INT .")
        continue
    else:
        break
if(a==0):
    if(b == 0):
        print("No es una ecuacion")
        b = float(input("Favor de ingresar B nuevamente: "))
    else:
        print("El valor de X es "(-c/b))
else:
    if(((b**2)-(4*a*c))<0):

        x1 = ((-b) + cmath.sqrt((b**2)-(4*a*c)))/ (2 * a)
        x2 = ((-b) - cmath.sqrt((b**2)-(4*a*c)))/ (2 * a)
    else:
        x1= ((-b) + math.sqrt((b**2)-(4*a*c)))/ (2 * a)
        x2= ((-b) - math.sqrt((b**2)-(4*a*c)))/ (2 * a)



    print("|============================================================|")
    print("Los valores dados son || A ==>",a," y B ==>",b," y C ==>",c)
    print("Primer valor  ==>",x1)
    print("Segundo valor  ==>",x2)

print("""

======================================================
                F)ffffff I)iiii N)n   nn
                F)         I)   N)nn  nn
                F)fffff    I)   N) nn nn
                F)         I)   N)  nnnn
                F)         I)   N)   nnn
                F)       I)iiii N)    nn
========================================================
""")
