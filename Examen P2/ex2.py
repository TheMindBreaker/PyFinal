ejemplo = [15,30,4,2]
def divide(lista):
    regreso = []
    minimos = []
    for i in range(3):
        var = min(lista)
        minimos.append(var)
        lista.remove(var)
        print(var)
        print (minimos,lista)
    regreso.append(minimos)
    regreso.append(lista)
    return(regreso)
print(divide(ejemplo))

def valida_con_rango(rango1,rango2):
