def minutos_usuario(user):
    from datetime import datetime
    from datetime import timedelta
    open_file = 'log.csv'
    try:
        openfile = open(open_file)
    except IOError:
        print('El archivo no se pudo abrir')
    if openfile:
        array_file = openfile.read().splitlines()
        connected_time = datetime(year=2017, month=01, day=01, hour=0, minute=0, second=0)
        show_time = []

        for stage1 in array_file:
                data = stage1.split(',')
                print(data)
                if(user in data):
                    time = data[7]
                    time = time.lstrip('(').rstrip(')').split(':')
                    d = timedelta(seconds=int(time[1]))
                    connected_time = connected_time+d
        time = connected_time
        return(time.strftime("%H Horas %I Minutos %S Segundos"))
    openfile.close()
def vacios(sensors):
    free_spaces = []
    positions = ['a','b','c','d','e','f','g','h','i','j',]
    for pos,row in enumerate(sensors):
        for pos2,status in enumerate(row):
            if(int(status)==0):
                for pos3,row3 in enumerate(positions):
                    current = positions[pos]
                    current +=str(pos2)
                free_spaces.append(current)
    return(free_spaces)


def tres_mayores(array):
    array =  list(map(int, array))
    biggest = []
    for data in array:
        biggest.append(max(array))
        array.remove(max(array))
    return(biggest)


def coincidencias(array1,array2):
    count = 0
    condition = min(array1, array2, key=len)
    array1 = list(array1)
    array2 = list(array2)
    i = 0

    while i<len(condition):
        if array1[i]==array2[i]:
            count+=1
        else:
             pass
        i+=1
    return(count)
print(coincidencias('pez','pecera'))
