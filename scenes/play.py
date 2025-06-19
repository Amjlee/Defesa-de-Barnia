# scenes/play.py - VERSÃO ATUALIZADA

from globals import *
from PPlay.sprite import Sprite
from Personagens.player import Player
from Personagens.fantasgua import Fantasgua
from Personagens.pingoso import Pingoso
from Personagens.arena import Arena
from Personagens.tiro import Tiro

import random
import time # Importando a biblioteca time

def create_enemies(level):
    enemies = []
    num_enemies = quantidade_inimigos(level)  # Obtém o número de inimigos com base no nível
    if num_enemies > 0:
        quantidade_pingoso = random.randint(0, num_enemies)
    else:
        quantidade_pingoso = 0
    quantidade_fantasgua = num_enemies - quantidade_pingoso

    for _ in range(quantidade_pingoso):
        x, y = get_spawn_position()
        enemies.append(Pingoso(x, y))

    for _ in range(quantidade_fantasgua):
        x, y = get_spawn_position()
        enemies.append(Fantasgua(x, y))

    return enemies

def Play():
    player = Player((janela.width / 2) - 60, (janela.height / 2) + 60)
    level = 1
    enemies = create_enemies(level)
    musica.load("AdhesiveWombat - Night Shade NO COPYRIGHT 8-bit Music [TubeRipper.cc].ogg")
    arena = Arena()
    last_key = ""
    # win_image = GameImage("templates/Win.png")
    # lose_image = GameImage("templates/Lose.png")
    
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

        # Lança o tiro na direção da última tecla pressionada
        if teclado.key_pressed("SPACE"):
            player.atirar(last_key, delta_time)

        # Verifica se não há inimigos para avançar de fase automaticamente
        if len(enemies) == 0 and level <= 10:
            level += 1
            print(f"Avançou para o nível {level}")
            
            # Pequena pausa antes de iniciar a próxima fase
            janela.update()
            time.sleep(1)

            if level <= 10:
                arena.set_current_arena(level)
                player.current_sprite.x = (janela.width / 2) - (player.current_sprite.width / 2)
                player.current_sprite.y = (janela.height / 2) - (player.current_sprite.height / 2)
                
                # Gera inimigos para o próximo nível
                enemies = create_enemies(level)

        # Movimento dos inimigos
        for enemy in enemies:
            enemy.follow_player(player, delta_time)

        # Verifica colisão com inimigos
        player.verificar_colisao_com_inimigo(enemies, delta_time)

        # Condição para voltar ao menu
        if teclado.key_pressed("ESC"):
            return "Menu"

        # Verifica se o jogador venceu
        if level > 10:
            # win_image.draw()
            # janela.update()
            # time.sleep(5)
            return "Menu"

        # Verifica se o jogador perdeu
        if player.vida <= 0:
            # lose_image.draw()
            # janela.update()
            # time.sleep(5)
            return "Menu"

        # Desenho na tela
        arena.draw()
        player.draw()
        for enemy in enemies[:]:
            if enemy.current_sprite is None:
                enemies.remove(enemy)
            else:
                enemy.draw()
        
        # Atualiza e desenha os tiros
        player.update_tiros(delta_time, enemies)
        player.draw_tiros()
        player.draw_vidas()
            
        janela.update()