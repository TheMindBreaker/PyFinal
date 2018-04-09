import clean

def validate(turn,line):
    validate = []
    open_file=open("files/LOG.txt","r")
    import week_control
    open_file.seek(0)
    array = open_file.read().splitlines()
    for i in array:
        array2 = i.split(',')
        if (str(turn)==array2[0] and str(line)==array2[1] and week_control.dia()==array2[2]):
            validate.append(True)
        else:
            validate.append(False)
    if(True in validate):
        return True
    else:
        return False

def add(turn,line,product,stopped):
    open_file=open("files/LOG.txt","a+")
    validating=True
    import week_control
    data_to_add=''
    data_to_add = (str(turn)+','+str(line)+','+str(week_control.dia())+','+str(product)+','+str(stopped)+'\n')
    if validate(turn,line)==True:
        print('Ya existe la informacion')
    else:
        open_file.write(data_to_add)
    open_file.close

def work():
    while True:
        clean.clear()
        global open_file
        print("""
        ==============================================
        WELCOME IT IS TIME TO ADD DATA TO THE SYSTEM
        ==============================================
        """)

        try:
            add_line = int(input("Ingresa la linea => "))
            print("============>")
            add_turn = int(input("Ingresa turno (1= Mañana, 2= Tarde, 3=Noche) => "))
            print("============>")
            add_total_num_prod = int(input("Total de Productos => "))
            print("============>")
            add_total_stopped = int(input("Total de detenciones => "))
            print("======================================>")
        except ValueError:
            print("Dato invalido ingresa solo numeros")
        add(add_turn,add_line,add_total_num_prod,add_total_stopped)

        next_pass = input("¿Agregar otro dato? (Y/N) =>")
        if next_pass.upper()=='N':
            break
