from globals import *
from PPlay.gameimage import GameImage
from Personagens.player import Player
from Personagens.fantasgua import Fantasgua

import random



def Play():
    player = Player(janela.width / 2, janela.height / 2)
    fantasgua = Fantasgua(janela.width / 4, janela.height / 4)  # Cria o Fantasgua

    last_key = ""  # Variável para guardar a última tecla pressionada
    level = 1
    
    while True:
        delta_time = janela.delta_time()

        # Movimento do player
        if teclado.key_pressed("W"):
            player.move("W", limites_W, limites_S, limites_A, limites_D, delta_time)
            last_key = "W"
        
        if teclado.key_pressed("S"):
            player.move("S", limites_W, limites_S, limites_A, limites_D, delta_time)
            last_key = "S"
        
        if teclado.key_pressed("A"):
            player.move("A", limites_W, limites_S, limites_A, limites_D, delta_time)
            last_key = "A"

        if teclado.key_pressed("D"):
            player.move("D", limites_W, limites_S, limites_A, limites_D, delta_time)
            last_key = "D"

        # Movimento do Fantasgua
        fantasgua.follow_player(player, delta_time)

        # Condição para voltar ao menu
        if teclado.key_pressed("ESC"):
            return "Menu"  # Retorna ao menu

        # Desenho na tela
        arena.draw()
        player.draw()
        fantasgua.draw()
        janela.update()