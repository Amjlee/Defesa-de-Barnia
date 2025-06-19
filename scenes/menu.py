# menu.py
from globals import *
from PPlay.gameimage import GameImage

def Menu(estado):
    # Botões
    botao_jogar = GameImage("templates/botao_jogar.png")
    botao_jogar.set_position(janela.width / 2 - botao_jogar.width / 2, 
                             janela.height / 2 - botao_jogar.height / 2 + 100)

    while True:
        # Verifica clique no botão
        if mouse.is_over_area((botao_jogar.x, botao_jogar.y), 
                              (botao_jogar.x + botao_jogar.width, 
                               botao_jogar.y + botao_jogar.height)):
            if mouse.is_button_pressed(1):  # Botão esquerdo do mouse
                estado = "Play"  # Atualiza o estado
                print(estado)
                return estado  # Retorna o estado atualizado para Game

        # Desenha os elementos na tela
        background.draw()
        botao_jogar.draw()
        janela.update()
