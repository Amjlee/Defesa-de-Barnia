from PPlay.window import Window
from PPlay.gameimage import GameImage
from PPlay.keyboard import Keyboard
from PPlay.mouse import Mouse

janela = Window(900, 600)
janela.set_title("Tombshifter")
background = GameImage("templates/background.png")
teclado = Keyboard()
mouse = Mouse()
