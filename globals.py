from PPlay.window import Window
from PPlay.gameimage import GameImage
from PPlay.sprite import *
from PPlay.keyboard import Keyboard
from PPlay.mouse import Mouse

janela = Window(900, 600)
janela.set_title("Tombshifter")

velocidade = 0.2

background = GameImage("templates/background.png")

arena = GameImage("templates/arena.png")
player_direita = Sprite("templates/cavemia_direita.png", 4)
player_esquerda = Sprite("templates/cavemia_esquerda.png", 4)
player_frente = Sprite("templates/cavemia_frente.png", 4)
player_tras = Sprite("templates/cavemia_tras.png", 4)
teclado = Keyboard()
mouse = Mouse()
estado = "Menu"

def limites_A(player: Sprite):
    global janela
    limite_arena_horizontal = {"esquerdo": 60, "direito": janela.width-player.width-60}
    limite_arena_vertical = {"inferior": janela.height-player.height-60,\
                            "superior": 60}
    return (((player.y<=janela.height-player.height-175 and player.y>=175) and (player.x>limite_arena_horizontal["esquerdo"])) or \
                                         ((player.y<175 or player.y>janela.height-player.height-175)\
                                           and player.x>limite_arena_horizontal["esquerdo"]+130))

def limites_S(player: Sprite):
    global janela
    limite_arena_horizontal = {"esquerdo": 60, "direito": janela.width-player.width-60}
    limite_arena_vertical = {"inferior": janela.height-player.height-60,\
                            "superior": 60}
    return ((player.y<limite_arena_vertical["inferior"]-120 and (player.x<180 or player.x>janela.width-180)) \
            or (player.y<limite_arena_vertical["inferior"]\
                and (player.x>180 and player.x<janela.width-180)))
    
def limites_D(player: Sprite):
    global janela
    limite_arena_horizontal = {"esquerdo": 60, "direito": janela.width-player.width-60}
    limite_arena_vertical = {"inferior": janela.height-player.height-60,\
                            "superior": 60}
    return (((player.y<=janela.height-player.height-175 and player.y>=175) and (player.x<limite_arena_horizontal["direito"]+40)) or \
                                         ((player.y<175 or player.y>janela.height-player.height-175) and player.x<limite_arena_horizontal["direito"]-90))
    
def limites_W(player: Sprite):
    global janela
    limite_arena_horizontal = {"esquerdo": 60, "direito": janela.width-player.width-60}
    limite_arena_vertical = {"inferior": janela.height-player.height-60,\
                            "superior": 60}
    return ((player.y>limite_arena_vertical["superior"]\
                and (player.x>180 and player.x<janela.width-player.width-180)) or(player.y>limite_arena_vertical["superior"]+120 and \
                                            (player.x<180 or player.x>janela.width-180)));