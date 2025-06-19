from PPlay.window import Window
from PPlay.gameimage import GameImage
from PPlay.sprite import *
from PPlay.keyboard import Keyboard
from PPlay.mouse import Mouse
from PPlay.sound import Sound
from Personagens import pingoso
from Personagens import fantasgua
import random

janela = Window(900, 600)
janela.set_title("Tombshifter")

velocidade = 0.2

background = GameImage("templates/defesa de barnia.jpg")

musica = Sound("AdhesiveWombat - Night Shade NO COPYRIGHT 8-bit Music [TubeRipper.cc].ogg")
teclado = Keyboard()
mouse = Mouse()
estado = "Menu"


def limites_W(player: Sprite):
    global janela
    limite_arena_vertical = {"inferior": janela.height-player.height-60,
                             "superior": 120}
    return ((player.y > limite_arena_vertical["superior"]
            and (120 < player.x < janela.width-player.width-120)) or (player.y > limite_arena_vertical["superior"]+120 and
            (player.x <= 120 or player.x >= janela.width-player.width-120)))


def limites_S(player: Sprite):
    global janela
    limite_arena_vertical = {
        "inferior": janela.height-player.height-60, "superior": 120}
    return ((player.y < limite_arena_vertical["inferior"]-120 and (player.x < 135 or player.x > janela.width-player.width-135))
            or (player.y < limite_arena_vertical["inferior"]
            and (135 <= player.x <= janela.width-player.width-135)))


def limites_A(player: Sprite):
    global janela
    limite_arena_horizontal = {"esquerdo": -10,
                               "direito": janela.width-player.width-60}
    return (((238 < player.y < janela.height-player.height-175) and (player.x > limite_arena_horizontal["esquerdo"])) or
            ((player.y <= 238 or player.y >= janela.height-player.height-175)
            and player.x > limite_arena_horizontal["esquerdo"]+150))


def limites_D(player: Sprite):
    global janela
    limite_arena_horizontal = {"esquerdo": -10,
                               "direito": janela.width-player.width-10}
    return (((240 <= player.y <= janela.height-player.height-175) and (player.x < limite_arena_horizontal["direito"])) or
            ((player.y < 240 or player.y > janela.height-player.height-175) and
            player.x < limite_arena_horizontal["direito"]-150))


def create_fantasgua():
    fantasgua.Fantasgua(janela.width / 4, janela.height / 4)


def quantidade_inimigos(level):
    if level == 1:
        return 0

    if level in [2, 3]:
        return 1

    if level in [4, 5]:
        return 2

    if level in [6, 7]:
        return 3

    if level in [8, 9, 10]:
        return 4
    if level == 11:
        return 0


def set_position_enemies():
    x = random.randint(140, janela.width-175)
    y = random.randint(120, janela.height-60)
    return x, y


def create_enemies(level: int):
    enemies = []
    qtdd_fantasgua = 0
    qtdd_pingoso = 0

    qtdd_fantasgua = random.randint(0, quantidade_inimigos(level))
    qtdd_pingoso = quantidade_inimigos(level) - qtdd_fantasgua

    for i in range(qtdd_fantasgua):
        x, y = set_position_enemies()
        enemies.append(fantasgua.Fantasgua(x, y))

    for j in range(qtdd_pingoso):
        x, y = set_position_enemies()
        enemies.append(pingoso.Pingoso(x, y))
    
    return enemies

def get_spawn_position():
    # Limites da área onde os inimigos podem surgir, baseados na sua função set_position_enemies
    left_bound = 140
    right_bound = janela.width - 175  # Resultado: 725
    top_bound = 120
    bottom_bound = janela.height - 60   # Resultado: 540

    # Escolhe aleatoriamente um dos quatro lados para o inimigo surgir
    side = random.randint(0, 3)

    if side == 0:  # Borda superior
        x = random.randint(left_bound, right_bound)
        y = top_bound
    elif side == 1:  # Borda inferior
        x = random.randint(left_bound, right_bound)
        y = bottom_bound
    elif side == 2:  # Borda esquerda
        x = left_bound
        y = random.randint(top_bound, bottom_bound)
    else:  # Borda direita
        x = right_bound
        y = random.randint(top_bound, bottom_bound)

    return x, y