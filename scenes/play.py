from globals import *
from PPlay.gameimage import GameImage

def Play():
    # Configurações iniciais do player
    player.set_position(janela.width / 2 - player.width / 2, janela.height / 2 - player.height / 2)

    while True:
        # Movimento do player
        if teclado.key_pressed("W") and ((player.y>limite_arena_vertical["superior"]\
                and (player.x>180 and player.x<janela.width-player.width-180)) or(player.y>limite_arena_vertical["superior"]+120 and \
                                            (player.x<180 or player.x>janela.width-180))):
            player.y -= velocidade
        if teclado.key_pressed("S") and ((player.y<limite_arena_vertical["inferior"]-120 and (player.x<180 or player.x>janela.width-180)) \
            or (player.y<limite_arena_vertical["inferior"]\
                and (player.x>180 and player.x<janela.width-180))):
            player.y += velocidade
        if teclado.key_pressed("A") and (((player.y<=janela.height-player.height-175 and player.y>=175) and (player.x>limite_arena_horizontal["esquerdo"])) or \
                                         ((player.y<175 or player.y>janela.height-player.height-175) and player.x>limite_arena_horizontal["esquerdo"]+130)):
            player.x -= velocidade
        if teclado.key_pressed("D") and (((player.y<=janela.height-player.height-175 and player.y>=175) and (player.x<limite_arena_horizontal["direito"])) or \
                                         ((player.y<175 or player.y>janela.height-player.height-175) and player.x<limite_arena_horizontal["direito"]-130)):
            player.x += velocidade

        # Condição para voltar ao menu
        if teclado.key_pressed("ESC"):
            return "Menu"  # Retorna ao menu

        # Desenho na tela
        arena.draw()
        player.draw()
        janela.update()
