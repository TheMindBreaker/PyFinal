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


#////////////////////////////////////////////////////////////////CODE HERE /////////////////////////
while True:#Input
    try:
        number = float(input("Ingresa las Cantidad: "))
        div = int(input("Ingresa el divisor: "))
    except ValueError:
        print("Error valor no es cerrado .")
        continue
    else:
        break
#Input EXIT ///////////////////////
divis = number % div
if (divis == 0):
    print ("El numero ", number," es divisible entre ",div)
else:
    print("El numero ", number," NO es divisible entre ",div)






#///////////////////////////////////////////////////////NOT HERE ////////////////////////////////////
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
