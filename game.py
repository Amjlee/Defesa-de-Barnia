# game.py
from scenes.menu import Menu
from scenes.play import Play
from globals import *

def Game(estado):
    while True:
        if estado == "Menu":
            estado = Menu(estado)  # Atualiza o estado com o retorno de Menu

        if estado == "Play":
            estado = Play()  # Atualiza o estado com o retorno de Play

        if teclado.key_pressed("ESC"):
            janela.close()
            break
