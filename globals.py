from PPlay.window import Window
from PPlay.gameimage import GameImage
from PPlay.keyboard import Keyboard
from PPlay.mouse import Mouse

janela = Window(900, 600)
janela.set_title("Tombshifter")

velocidade = 0.2

background = GameImage("templates/background.png")

arena = GameImage("templates/arena.png")
player = GameImage("templates/player.png")
teclado = Keyboard()
mouse = Mouse()
estado = "Menu"

limite_arena_horizontal = {"esquerdo": 60, "direito": janela.width-player.width-60}
limite_arena_vertical = {"inferior": janela.height-player.height-60,\
                        "superior": 60}