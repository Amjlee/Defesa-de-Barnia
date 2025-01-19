from PPlay.sprite import Sprite
from PPlay.gameimage import GameImage

class Arena:
    def __init__(self):
        # Inicializa o sprite do Fantasgua com 4 frames de animação
        self.arenas = {
            1: GameImage("templates/Arenas/arena_2.png"),
            2: GameImage("templates/Arenas/arena_1.png"),
            3: GameImage("templates/Arenas/arena_3.png"),
        }
        self.current_arena = self.arenas[1]
        # Define a posição inicial do sprite
        # self.sprite.set_position(x, y)
        # Define a duração total da animação do sprite
        # self.sprite.set_total_duration(500)
        # Define a velocidade base do Fantasgua
        # self.velocidade = 70

    def set_current_arena(self, level):
        self.current_arena = self.arenas[level]

    def draw(self):
        # Desenha o sprite do Fantasgua na tela
        self.current_arena.draw()