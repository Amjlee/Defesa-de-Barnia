from globals import *
from PPlay.gameimage import GameImage

def Play():
    # Configurações iniciais do player
    player.set_position(janela.width / 2 - player.width / 2, janela.height / 2 - player.height / 2)

    while True:
        # Movimento do player
        if teclado.key_pressed("W"):
            player.y -= velocidade
        if teclado.key_pressed("S"):
            player.y += velocidade
        if teclado.key_pressed("A"):
            player.x -= velocidade
        if teclado.key_pressed("D"):
            player.x += velocidade

        # Condição para voltar ao menu
        if teclado.key_pressed("ESC"):
            return "Menu"  # Retorna ao menu

        # Desenho na tela
        arena.draw()
        player.draw()
        janela.update()
