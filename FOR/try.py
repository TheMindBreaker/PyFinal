lista = [[-5,-1,1,2,3,4,5,6],[8,16,20,35]]

def cuentaPares (lista):
    total = 0
    for i in lista:
        print(i)
        for k in i:
            print(k)
            if((k%2)==0):
                total +=1
    print("El numero de pares = ",total)
cuentaPares(lista)
print ('=====================')

def sumaMatriz(lista):
    resultado = 0
    for i in lista:
        for k in i:
            resultado = resultado + k
            resultado += k
    print('El resultado de la suma = ',resultado)
sumaMatriz(lista)
print ('=====================')
def cambiaNegativos(lista):
    for i,k in enumerate(lista):
        print(i,'=',k)
        for j,m in enumerate(k):
            print(j,'=',m)
            if(m<0):
                lista[i][j]=0
    print(lista)
cambiaNegativos(lista)
