from PPlay.sprite import Sprite
from PPlay.gameimage import GameImage

class Arena:
    def __init__(self):
        # Inicializa o sprite do Fantasgua com 4 frames de animação
        self.arenas = {
            1: GameImage("templates/Arenas/arena_2.png"),
            2: GameImage("templates/Arenas/arena_2.png"),
            3: GameImage("templates/Arenas/arena_2.png"),
            4: GameImage("templates/Arenas/arena_2.png"),
            5: GameImage("templates/Arenas/arena_1.png"),
            6: GameImage("templates/Arenas/arena_1.png"),
            7: GameImage("templates/Arenas/arena_1.png"),
            8: GameImage("templates/Arenas/arena_3.png"),
            9: GameImage("templates/Arenas/arena_3.png"),
            10: GameImage("templates/Arenas/arena_3.png"),
            11: GameImage("templates/Lose.png"),
            11: GameImage("templates/Win.png"),
        }
        self.current_arena = self.arenas[1]

    def set_current_arena(self, level):
        self.current_arena = self.arenas[level]

    def draw(self):
        # Desenha o sprite do Fantasgua na tela
        self.current_arena.draw()