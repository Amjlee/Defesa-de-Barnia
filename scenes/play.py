from globals import *
from PPlay.sprite import Sprite
from Personagens.player import Player
from Personagens.fantasgua import Fantasgua
from Personagens.pingoso import Pingoso
from Personagens.arena import Arena
from Personagens.tiro import Tiro

import random

def create_enemies(level):
    enemies = []
    num_enemies = quantidade_inimigos(level)  # Obtém o número de inimigos com base no nível
    quantidade_pingoso = random.randint(0, num_enemies)
    quantidade_fantasgua = num_enemies - quantidade_pingoso

    for _ in range(quantidade_pingoso):
        x = random.randint(0, janela.width)
        y = janela.height // 2
        enemies.append(Pingoso(x, y))

    for _ in range(quantidade_fantasgua):
        x = random.randint(0, janela.width)
        y = janela.height // 2
        enemies.append(Fantasgua(x, y))

    return enemies

def Play():
    player = Player((janela.width / 2) - 60, (janela.height / 2) + 60)  # Ajusta a posição inicial do player
    level = 1
    enemies = create_enemies(level)  # Começa com inimigos no nível 1
    porta = False  # Porta não aparece inicialmente
    porta_sprite = Sprite("templates/porta.png")
    porta_sprite.set_position((janela.width / 2) - 60, (janela.height / 5) * 1)  # Define a posição inicial da porta
    musica.load("Eric Skiff - A Night Of Dizzy Spells.ogg")
    arena = Arena()  # Cria uma instância da classe Arena
    last_key = ""  # Variável para guardar a última tecla pressionada
    win_image = GameImage("templates/Win.png")
    lose_image = GameImage("templates/Lose.png")
    
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

        # Verifica se não há inimigos
        if len(enemies) == 0:
            porta = True
        else:
            porta = False

        # Movimento dos inimigos
        for enemy in enemies:
            enemy.follow_player(player, delta_time)

        # Verifica colisão com inimigos
        player.verificar_colisao_com_inimigo(enemies, delta_time)

        # Condição para voltar ao menu
        if teclado.key_pressed("ESC"):
            return "Menu"  # Retorna ao menu

        # Passar de Fase - Lógica para nível 1
        if level == 1 and player.colide_porta(porta_sprite):
            level += 1
            player.current_sprite.x = (janela.width / 2) - (player.current_sprite.width / 2)
            player.current_sprite.y = (janela.height / 2) - (player.current_sprite.height / 2)
            print(f"Avançou para o nível {level}")

            # Gera inimigos para o nível 2
            enemies = create_enemies(level)

        # Passar de Fase - A partir do nível 2
        if level > 1 and player.colide_porta(porta_sprite) and porta and level < 11:
            level += 1
            arena.set_current_arena(level)
            player.current_sprite.x = (janela.width / 2) - (player.current_sprite.width / 2)
            player.current_sprite.y = (janela.height / 2) - (player.current_sprite.height / 2)
            print(f"Avançou para o nível {level}")

            # Gera inimigos para o próximo nível
            enemies = create_enemies(level)

        # Verifica se o jogador venceu
        if level > 10:
            win_image.draw()
            janela.update()
            time.sleep(5)
            return "Menu"  # Volta ao menu após a vitória

        # Verifica se o jogador perdeu
        if player.vida <= 0:
            lose_image.draw()
            janela.update()
            time.sleep(5)
            return "Menu"  # Volta ao menu após a derrota

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
            
        # Renderiza a porta se porta == True
        if porta:
            porta_sprite.draw()

        janela.update()
