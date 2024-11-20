from PPlay.window import *
from PPlay.gameimage import *
from PPlay.keyboard import *
from PPlay.mouse import *

janela = Window(900,600)
janela.set_title("Tombshifter")
teclado = Keyboard()
mouse = Mouse()

background = GameImage("templates/background.png")
estado = "menu"


while True:
    if estado == "menu":        
        background.draw()
        janela.update()
        if teclado.key_pressed("ESC"):
            break