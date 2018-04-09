import math

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
        X1 = float(input("Ingresa valos X1: "))
        Y1 = float(input("Ingresa valos Y1: "))
        X2 = float(input("Ingresa valos X2: "))
        Y2 = float(input("Ingresa valos Y2: "))
    except ValueError:
        print("Error valor no es un INT .")
        continue
    else:
        break
distancia = math.sqrt(((X2-X1)**2)+((Y2-Y1)**2))
print("|============================================================|")
print("Las coordenadas dadas son || (",X1,",",Y1,") y (",X2,",",Y2,")")
print("Distancia entre ellos son ==>",distancia)

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
