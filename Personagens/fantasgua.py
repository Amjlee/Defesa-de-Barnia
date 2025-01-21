from PPlay.sprite import Sprite

class Fantasgua:
    def __init__(self, x, y):
        # Inicializa o sprite do Fantasgua com 4 frames de animação
        self.current_sprite = Sprite("templates/Inimigos/fantasgua.png", 4)
        # Define a posição inicial do current_sprite
        self.current_sprite.set_position(x, y)
        # Define a duração total da animação do current_sprite
        self.current_sprite.set_total_duration(500)
        # Define a velocidade base do Fantasgua
        self.velocidade = 70
        self.hp = 1

    def follow_player(self, player, delta_time):
        # Calcula a distância de movimento com base na velocidade e delta time
        move_distance = self.velocidade * delta_time

        # Calcula a direção para o jogador
        direction_x = (player.current_sprite.x + player.current_sprite.width / 2) - (self.current_sprite.x + self.current_sprite.width / 2)
        direction_y = (player.current_sprite.y + player.current_sprite.height / 2) - (self.current_sprite.y + self.current_sprite.height / 2)
        
        # Normaliza a direção
        distance = (direction_x**2 + direction_y**2)**0.5
        if distance != 0:
            direction_x /= distance
            direction_y /= distance

        # Move o Fantasgua na direção do jogador
        self.current_sprite.x += direction_x * move_distance
        self.current_sprite.y += direction_y * move_distance

        # Atualiza a animação do current_sprite
        self.current_sprite.update()

    def draw(self):
        # Desenha o current_sprite do Fantasgua na tela
        self.current_sprite.draw()