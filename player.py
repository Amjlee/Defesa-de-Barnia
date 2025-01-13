from PPlay.sprite import Sprite

class Player:
    def __init__(self, x, y):
        self.sprites = {
            "frente": Sprite("templates/cavemia_frente.png", 4),
            "esquerda": Sprite("templates/cavemia_esquerda.png", 4),
            "tras": Sprite("templates/cavemia_tras.png", 4),
            "direita": Sprite("templates/cavemia_direita.png", 4)
        }
        self.current_sprite = self.sprites["frente"]
        self.current_sprite.set_position(x, y)
        self.current_sprite.set_total_duration(500)
        self.velocidade = 100  # Velocidade base do jogador

    def move(self, direction, limites_W, limites_S, limites_A, limites_D, delta_time):
        move_distance = self.velocidade * delta_time
        if direction == "W" and limites_W(self.current_sprite):
            self.current_sprite.y -= move_distance
            self.change_sprite("tras")
        elif direction == "S" and limites_S(self.current_sprite):
            self.current_sprite.y += move_distance
            self.change_sprite("frente")
        elif direction == "A" and limites_A(self.current_sprite):
            self.current_sprite.x -= move_distance
            self.change_sprite("esquerda")
        elif direction == "D" and limites_D(self.current_sprite):
            self.current_sprite.x += move_distance
            self.change_sprite("direita")

    def change_sprite(self, direction):
        x, y = self.current_sprite.x, self.current_sprite.y
        self.current_sprite = self.sprites[direction]
        self.current_sprite.set_position(x, y)
        self.current_sprite.set_total_duration(500)
        self.current_sprite.update()

    def draw(self):
        self.current_sprite.draw()