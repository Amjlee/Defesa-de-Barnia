from globals import *
from PPlay.gameimage import GameImage
from PPlay.sprite import Sprite

def Play():
    player = player_direita
    # Configurações iniciais do player
    player.set_position(janela.width / 2 - player.width / 2, janela.height / 2 - player.height / 2)
    player.set_total_duration(500)

    # Carregar sprites
    cavemia_frente = Sprite("templates/cavemia_frente.png", 4)
    cavemia_esquerda = Sprite("templates/cavemia_esquerda.png", 4)
    cavemia_tras = Sprite("templates/cavemia_tras.png", 4)
    cavemia_direita = Sprite("templates/cavemia_direita.png", 4)

    while True:
        # Movimento do player
        if teclado.key_pressed("W") and limites_W(player):
            player.y -= velocidade
            player.set_curr_frame(cavemia_tras.get_curr_frame())
            player = cavemia_tras
            player.set_total_duration(500)
            player.update()
        elif teclado.key_pressed("S") and limites_S(player):
            player.y += velocidade
            player.set_curr_frame(cavemia_frente.get_curr_frame())
            player = cavemia_frente
            player.set_total_duration(500)
            player.update()
        elif teclado.key_pressed("A") and limites_A(player):
            player.x -= velocidade
            player.set_curr_frame(cavemia_esquerda.get_curr_frame())
            player = cavemia_esquerda
            player.set_total_duration(500)
            player.update()
        elif teclado.key_pressed("D") and limites_D(player):
            player.x += velocidade
            player.set_curr_frame(cavemia_direita.get_curr_frame())
            player = cavemia_direita
            player.set_total_duration(500)
            player.update()

        # Condição para voltar ao menu
        if teclado.key_pressed("ESC"):
            return "Menu"  # Retorna ao menu

        # Desenho na tela
        arena.draw()
        player.draw()
        janela.update()
