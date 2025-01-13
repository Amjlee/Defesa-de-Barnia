from globals import *
from PPlay.gameimage import GameImage
from player import Player

def Play():
    player = Player(janela.width / 2, janela.height / 2)

    while True:
        delta_time = janela.delta_time()

        # Movimento do player
        if teclado.key_pressed("W"):
            player.move("W", limites_W, limites_S, limites_A, limites_D, delta_time)
        if teclado.key_pressed("S"):
            player.move("S", limites_W, limites_S, limites_A, limites_D, delta_time)
        if teclado.key_pressed("A"):
            player.move("A", limites_W, limites_S, limites_A, limites_D, delta_time)
        if teclado.key_pressed("D"):
            player.move("D", limites_W, limites_S, limites_A, limites_D, delta_time)

        # Condição para voltar ao menu
        if teclado.key_pressed("ESC"):
            return "Menu"  # Retorna ao menu

        # Desenho na tela
        arena.draw()
        player.draw()
        janela.update()