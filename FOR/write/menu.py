import cleaner
import logo
def menu():
    cleaner.clear()
    logo.logo()
    print("""
Opciones disponibles:
    1 => Ingresar datos de la línea
    2 => Hacer resumen
    3 => Reiniciar semana
    4 => Consultas parciales
    5 => Salir
    """)
    option = input("Ingresa alguna de las opciones =>")
    if(option == '1'):
        import addData
    elif(option == '2'):
        import makeSumary
    elif(option == '3'):
        import rebootWeek
    elif(option == '4'):
        import partialConsult
    elif(option == '5'):
        pass
        return 'false'
    else:
        print("No existe ninguna opcion para esto")
