from globals import *
from PPlay.sprite import Sprite
from Personagens.player import Player
from Personagens.fantasgua import Fantasgua
from Personagens.pingoso import Pingoso

import random

def Play():
    player = Player((janela.width / 2) - 60, (janela.height / 5)+60)
    level = 0
    enemies = [Pingoso((janela.width/2), (janela.height/3))]
    porta = False
    porta_sprite = Sprite("templates/porta.png")
    porta_sprite.set_position((janela.width / 2) - 60, (janela.height / 5) * 1)  # Define a posição inicial da porta
    musica.load("Eric Skiff - A Night Of Dizzy Spells.ogg")
    last_key = ""  # Variável para guardar a última tecla pressionada / Auxiliará no ataque
    
    while True:
        musica.set_volume(10)
        musica.play()
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


        # Verifica se não há inimigos
        if len(enemies) == 0:
            porta = True

        # Movimento dos inimigos
        for enemy in enemies:
            enemy.follow_player(player, delta_time)

        # Condição para voltar ao menu
        if teclado.key_pressed("ESC"):
            return "Menu"  # Retorna ao menu
        
        # Passar de Fase
        if player.colide_porta(porta_sprite) and porta:
            level += 1
            player.current_sprite.x = (janela.width / 2) - (player.current_sprite.width / 2)
            player.current_sprite.y = (janela.height / 2) - (player.current_sprite.height / 2)
            print("colide")
            print(level)

        # Desenho na tela
        arena.draw()
        player.draw()
        for enemy in enemies:
            enemy.draw()
        
        # Renderiza a porta se porta == True
        if porta:
            porta_sprite.draw()

        janela.update()
        musica.set_repeat(repeat=True)