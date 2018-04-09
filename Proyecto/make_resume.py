def work():
    import clean
    import week_control
    while True:
        clean.clear()
        open_file = open(("files/week_report"+"-"+week_control.primer_dia()+'-'+week_control.ultimo_dia()+'.txt'),'w+')
        open_file2 = open("files/LOG.txt",'r')
        print("""
        +=========================================+
        |Se genero un reporte de semana con exito |
        +=========================================+
        """)

        if((input('Desea generar el Resumen => ')).upper()=='Y'):
            array = open_file2.read().splitlines()
            open_file.write("Semana del "+str(week_control.primer_dia())+' al '+ str(week_control.ultimo_dia()))
            for i in array:
                array2 = i.split(',')
                open_file.write('---------------------')
                open_file.write("Turno = "+array2[0])
                open_file.write("linea = "+array2[1])
            break
        else:
            break
