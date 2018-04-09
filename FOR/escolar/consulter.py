import os
archivo = None
clear = lambda: os.system('clear')
try:
    clear()
    archivo = open('students.txt')
except IOError:
  print ("ERROR este archivo no existe")
if archivo:
    file_opened = archivo.read().splitlines()
    for f1 in file_opened:
        result = 0
        f1splited = f1.split(':')
        print('+=====================================================+')
        print('+===============Matricula: ',f1splited[0],' ===============+')
        print('+=====================================================+')
        name= f1splited[1].split(' ')
        numname = (len(name))-1
        print ('Nombre: ',name[numname],', ',name[0])
        print('Carrera: ', f1splited[2],' - ',f1splited[5])
        print('Semetre: ', f1splited[3])
        year = list(f1splited[4])
        dates= 'Not defined'
        if((''.join(year[4:6]))=='13'):
            dates = 'Agosto Diciembre'
        elif((''.join(year[4:6]))=='11'):
            dates = 'Enero Mayo'
        elif((''.join(year[4:6]))=='12'):
            dates = 'Verano'
        print('Periodo: ', ''.join(year[0:4]),' ',dates)
        gradessplit = f1splited[6].split(',')
        num = len(gradessplit)
        for grades in gradessplit:
            grades = float(grades)
            result+=grades
        result = result/num
        print('Promedio: ',"%.2f" % result)
