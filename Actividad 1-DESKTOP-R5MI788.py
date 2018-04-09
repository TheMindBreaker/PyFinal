def busqueda_binaria(lista, x):
	lista = list(map(int, lista))
	x = int(x)
	print(lista)
	izq = 0
	der = len(lista) -1
	while izq <= der:
		medio = (izq+der)//2
		if lista[medio] == x:
			return medio
		elif lista[medio] > x:
			der = medio-1
		else:
			izq = medio+1
			return -1

def elimina_duplicados(lista):
	lista_nueva = []
	for i in lista:
		if i not in lista_nueva:
			lista_nueva.append(i)
	return(lista_nueva)
def con_duplicados(lista):
	respuesta = False
	j = 0
	k = 0
	for j in range(len(myList)):
    	for k in range(len(myList)):
	        if myList[j] == myList[k]:
	            print "found a duplicate!"
	            return
