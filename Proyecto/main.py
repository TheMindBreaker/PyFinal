import clean
while True:
    clean.clear()
    import week_control
    print("""
    +-------------------------------------------+
    | Welcome to XETU Manage System V 2.0       |
    +-------------------------------------------+
    -> 1.	Ingresar datos de la línea
    -> 2.	Hacer resumen
    -> 3.	Reiniciar semana
    -> 4.	Consultas parciales
    -> 6.	Salir
    +-------------------------------------------+
    ""","Fecha en el sistema:",week_control.dia(),"""
    +===========================================+
    """)

    enter_to = input("Ingresa alguna opción =>")
    if(enter_to=="1"):
        import add_data
        add_data.work()
    elif(enter_to=="2"):
        import make_resume
        make_resume.work()
    elif(enter_to=="3"):
        import reboot_week
    elif(enter_to=="4"):
        import partial_consult
    elif(enter_to=="6"):
        clean.clear()
        print("""
        ====================
        +Cession Cerrada   +
        ====================
        """)
        break
