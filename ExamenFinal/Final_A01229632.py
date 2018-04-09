def valida_num(string):
    string += " => "
    while True:
        try:
            validate = int(input(string))
        except ValueError:
            print("Error el dato no es un numero")
            continue
        else:
            return validate
            break
valida_num("Inresa tu num")
def mayor_Ingresado():
    biggest = 0
    number = valida_num("Ingresa un numero")
    while(number>0):
        number = valida_num("Ingresa un numero")
        if(number>biggest):
            biggest = number

    return biggest

def palabras(string,number):
    import re
    total = 0
    string_list = re.findall(r'[^,;\s]+', string)
    for i in string_list:
        if len(i) == number:
            total +=1
    return total

def extension_frecuente(string_list):
    import os
    import collections
    extension_list = []
    for i in string_list:
        filename, file_extension = os.path.splitext(i)
        extension_list.append(file_extension)
    count = collections.Counter(extension_list).most_common(1)
    return(count[0][0])

def duplica_lista(re_list):
    return_list = []
    return_list += re_list
    return_list += re_list
    return(return_list)

def ganador(list1,list2):
    all_total = []
    for j,i in enumerate(list2):
        time = 0
        for k in i:
            time +=k
        all_total.append(time)
    win_pos = all_total.index(min(all_total))
    return(list1[win_pos])

def con_prefijo(string,prefix):
    import re
    m = [word for word in string.split() if word.startswith(prefix)]
    return m

def nomenclatura(string,num1,num2):
    return_list = []
    for i in range(num1):
        return_list.append([])
        build = i
        for k in range(num2):
            read= string+str(build)+'-'+str(k)
            return_list[i].append(read)
    return(return_list)
