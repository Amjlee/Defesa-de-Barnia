from PPlay.sprite import Sprite

class Fantasgua:
    def __init__(self, x, y):
        self.current_sprite = Sprite("templates/Inimigos/fantasgua.png", 4)
        self.current_sprite.set_position(x, y)
        self.current_sprite.set_total_duration(500)
        self.vida = 1  # Vida inicial do Fantasgua

    def tomar_dano(self, dano):
        self.vida -= dano
        if self.vida <= 0:
            self.morrer()

    def morrer(self):
        # Lógica para quando o Fantasgua morrer (pode ser removido do jogo, etc.)
        print("Fantasgua morreu")
        self.current_sprite = None  # Remove o sprite do Fantasgua
        
    def follow_player(self, player, delta_time):
        if self.current_sprite is None:
            return  # Não faz nada se o sprite for None

        move_distance = 100 * delta_time
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
        if self.current_sprite is not None:
            # Desenha o current_sprite do Fantasgua na tela
            self.current_sprite.draw()

