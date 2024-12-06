from globals import *
from PPlay.gameimage import GameImage

def Play():
    # Configurações iniciais do player
    player.set_position(janela.width / 2 - player.width / 2, janela.height / 2 - player.height / 2)

    while True:
        # Movimento do player
        if teclado.key_pressed("W") and player.y>limite_arena_vertical["superior"]:
            player.y -= velocidade
        if teclado.key_pressed("S") and player.y<limite_arena_vertical["inferior"]:
            player.y += velocidade
        if teclado.key_pressed("A") and player.x>limite_arena_horizontal["esquerdo"]:
            player.x -= velocidade
        if teclado.key_pressed("D") and player.x<limite_arena_horizontal["direito"]:
            player.x += velocidade

        # Condição para voltar ao menu
        if teclado.key_pressed("ESC"):
            return "Menu"  # Retorna ao menu

        # Desenho na tela
        arena.draw()
        player.draw()
        janela.update()
