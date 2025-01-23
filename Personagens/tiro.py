from PPlay.sprite import Sprite
from PPlay.collision import Collision

class Tiro:
    def __init__(self, x, y, direction):
        # Seleciona o sprite correto com base na direção
        if direction == "W":
            self.sprite = Sprite("templates/tiro_cima.png", 4)
        elif direction == "S":
            self.sprite = Sprite("templates/tiro_baixo.png", 4)
        elif direction == "A":
            self.sprite = Sprite("templates/tiro_esquerda.png", 4)
        elif direction == "D":
            self.sprite = Sprite("templates/tiro_direita.png", 4)
        
        self.sprite.set_position(x, y)
        self.sprite.set_total_duration(500)
        self.direction = direction
        self.velocidade = 300

    def colide_com_inimigo(self, inimigos):
        for inimigo in inimigos:
            if inimigo.current_sprite is not None and Collision.collided(self.sprite, inimigo.current_sprite):
                inimigo.tomar_dano(1)
                return True
        return False

    def move(self, delta_time):
        move_distance = self.velocidade * delta_time
        if self.direction == "W":
            self.sprite.y -= move_distance
        elif self.direction == "S":
            self.sprite.y += move_distance
        elif self.direction == "A":
            self.sprite.x -= move_distance
        elif self.direction == "D":
            self.sprite.x += move_distance

        self.sprite.update()

    def draw(self):
        self.sprite.draw()
