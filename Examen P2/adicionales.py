def coincidenVocales(array1,array2):
    vocales = ['a','e','i','o','u']
    count = 0
    condition = max(array1, array2, key=len)
    condition2 = min(array1, array2, key=len)
    arreglo = list(condition)
    vocales1 = []
    iguales = []
    while count<len(condition):
        if(condition[count] in vocales):
            if(condition[count] not in vocales1):
                vocales1.append(condition[count])
                if(condition[count] in condition2):
                    iguales.append(condition[count])
        count +=1
    return(iguales)

def aprobados(grupo):
    open_file = 'calificaciones.csv'
    print('+----------------------------------------------->')
    print('Los Alumnos Aprobados del grupo',grupo.upper())
    try:
        openfile = open(open_file)
    except IOError:
        print('El archivo no se pudo abrir')
    if openfile:
        array_file = openfile.read().splitlines()
        for pos,stage1 in enumerate(array_file):
            array_file2 = stage1.split(',')
            calificaciones = 0
            if(grupo.upper() in array_file2[0]):
                calificaciones= (float(array_file2[2])+float(array_file2[3])+float(array_file2[4]))/3
                if(calificaciones>=70):
                    print('______________')
                    print(array_file2[1])
    print('+----------------------------------------------->')
