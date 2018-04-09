
def MENU():
    import os
    clear = lambda: os.system('cls')
    clear()
    print("""
    LOGO
    """)
    while True:
        chose = input("Ingresa una de las opciones del menu: ")
        if (chose == "1"):
            user = input("Ingresa el numero de cantidades a sumar: ")
            print(ej1(user))

def ej1(n):
    result = 0
    for i in range(n):
        while True:
            try:
                add = int(input("Ingresa el "+ i +" numero: "))
            except ValueError:
                msg = "Este no es un numero."
                continue
            else:
                break
        result = result + add
    return result
MENU()
