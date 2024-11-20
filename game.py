from scenes.menu import Menu
from globals import janela, teclado

estado = "Menu"

def Game():
    while True:
        if estado == "Menu":
            Menu()
        
        if teclado.key_pressed("ESC"):
            janela.close()
            break