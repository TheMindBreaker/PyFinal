def combina_listas(list1,list2):

    return [val for pair in zip(list1, list2) for val in pair]


def numeros_rango(val_min,val_max):
    inputs = []

    while True:
        try:
            val = int(input("Ingrese un valor => "))
        except ValueError:
            print('Ingrese solo numeros')
        if(val>val_max or val<val_min):
            break
        else:
            inputs.append(val)
    return inputs
def numeros_Suman(val):
    import random
    numbers = []
    add = 0
    while add<val:
        val2 = random.randint(1,(val/2))
        add+=val2
        numbers.append(val2)
    return numbers

def cuenta_palabras(lista,palabra):
    import re
    returns = []
    print(palabra)
    for i in lista:
        print(i)
        for k in i:
            print(k)
            total = 0
            array = re.findall(r'[^,;\s]+', k)
            for j in array:
                print(j)
                if(j==palabra):
                    total +=1
                print(total)
            returns.append(total)
    return returns
def multiplos_de_5(lista):
     returns = []
     for i in lista:
         for k in i:
             if((k%5)==0):
                 returns.append(k)
     return returns
def ordena_ABC(lista):
    orden = [[],[],[],[]]
    for i in lista:
        for k in i:
            if(k.startswith('a') or k.startswith('A')):
                orden[0].append(k)
            elif(k.startswith('b') or k.startswith('B')):
                orden[1].append(k)
            elif(k.startswith('c') or k.startswith('C')):
                orden[2].append(k)
            else:
                orden[3].append(k)
    return orden
