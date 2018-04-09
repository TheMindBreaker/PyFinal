from menu import menu as menu
import cleaner

while True:
    if menu()=='false':
        cleaner.clear()
        break
