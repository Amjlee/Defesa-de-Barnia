from PPlay.sprite import Sprite

class Pingoso:
    def __init__(self, x, y):
        # Inicializa o sprite do Fantasgua com 4 frames de animação
        self.sprites = {
            "frente": Sprite("templates/Inimigos/Pingoso/pingoso_frente.png", 4),
            "esquerda": Sprite("templates/Inimigos/Pingoso/pingoso_esquerda.png", 4),
            "tras": Sprite("templates/Inimigos/Pingoso/pingoso_costa.png", 4),
            "direita": Sprite("templates/Inimigos/Pingoso/pingoso_direita.png", 4)
        }
        
        # Define a posição inicial do sprite
        self.sprite.set_position(x, y)
        # Define a duração total da animação do sprite
        self.sprite.set_total_duration(500)
        # Define a velocidade base do Fantasgua
        self.velocidade = 50

    def follow_player(self, player, delta_time):
        # Calcula a distância de movimento com base na velocidade e delta time
        move_distance = self.velocidade * delta_time
        
        # Calcula a direção para o jogador
        direction_x = player.current_sprite.x - self.sprite.x
        direction_y = player.current_sprite.y - self.sprite.y
        
        # Normaliza a direção
        distance = (direction_x**2 + direction_y**2)**0.5
        if distance != 0:
            direction_x /= distance
            direction_y /= distance
        
        # Move o Fantasgua na direção do jogador
        self.sprite.x += direction_x * move_distance
        self.sprite.y += direction_y * move_distance
        
        # Atualiza a animação do sprite
        self.sprite.update()

    def update_sprite_direction(self, direction_x, direction_y):
        if abs(direction_x) > abs(direction_y):
            if direction_x > 0:
                self.sprite = self.sprites["direita"]
            else:
                self.sprite = self.sprites["esquerda"]
        else:
            if direction_y > 0:
                self.sprite = self.sprites["frente"]
            else:
                self.sprite = self.sprites["tras"]

    def follow_player(self, player, delta_time):
        # Calcula a distância de movimento com base na velocidade e delta time
        move_distance = self.velocidade * delta_time
        
        # Calcula a direção para o jogador
        direction_x = player.current_sprite.x - self.sprite.x
        direction_y = player.current_sprite.y - self.sprite.y
        
        # Normaliza a direção
        distance = (direction_x**2 + direction_y**2)**0.5
        if distance != 0:
            direction_x /= distance
            direction_y /= distance
        
        # Move o Fantasgua na direção do jogador
        self.sprite.x += direction_x * move_distance
        self.sprite.y += direction_y * move_distance
        
        # Atualiza a animação do sprite
        self.sprite.update()
        
        # Atualiza a direção do sprite
        self.update_sprite_direction(direction_x, direction_y)