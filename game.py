from scenes.menu import *
from main import estado, teclado
while True:
    if estado == "menu":
        Menu()
        if teclado.key_pressed("ESC"):
            break