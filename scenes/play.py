from globals import *
from PPlay.gameimage import GameImage

def Play():
    player = player_direita
    # Configurações iniciais do player
    player.set_position(janela.width / 2 - player.width / 2, janela.height / 2 - player.height / 2)
    player.set_total_duration(500)
    while True:
        # Movimento do player
        if teclado.key_pressed("W") and limites_W(player):
            player.y -= velocidade
            x = player.x
            y = player.y
            player = player_tras
            player.set_total_duration(500)
            player.set_position(x, y)
            player.update()
        if teclado.key_pressed("S") and limites_S(player):
            player.y += velocidade
            x = player.x
            y = player.y
            player = player_frente
            player.set_total_duration(500)
            player.set_position(x, y)
            player.update()
        if teclado.key_pressed("A") and limites_A(player):
            player.x -= velocidade
            x = player.x
            y = player.y
            player = player_direita
            player.set_total_duration(500)
            player.set_position(x, y)
            player.update()
        if teclado.key_pressed("D") and limites_D(player):
            player.x += velocidade
            x = player.x
            y = player.y
            player = player_esquerda
            player.set_total_duration(500)
            player.set_position(x, y)
            player.update()

        # Condição para voltar ao menu
        if teclado.key_pressed("ESC"):
            return "Menu"  # Retorna ao menu

        # Desenho na tela
        arena.draw()
        player.draw()
        janela.update()
