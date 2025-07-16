from PPlay.sprite import Sprite

class Pingoso:
    def __init__(self, x, y):
        # Inicializa os sprites do Pingoso para cada direção
        self.sprites = {
            "esquerda": Sprite("templates/Inimigos/Pingoso/asa_esquerda.png", 3),
            "direita": Sprite("templates/Inimigos/Pingoso/asa_direita.png", 3)
        }
        
        self.current_sprite = self.sprites["esquerda"]
        # Define a posição inicial do sprite
        self.current_sprite.set_position(x, y)
        # Define a duração total da animação do current_sprite
        self.current_sprite.set_total_duration(500)
        # Define a velocidade base do Pingoso
        self.velocidade = 60
        self.hp = 2  # Vida inicial do Pingoso

    def tomar_dano(self, dano):
        self.hp -= dano
        if self.hp <= 0:
            self.morrer()

    def morrer(self):
        # Lógica para quando o Pingoso morrer (pode ser removido do jogo, etc.)
        print("Pingoso morreu")
        self.current_sprite = None  # Remove o sprite do Pingoso

    def follow_player(self, player, delta_time):
        if self.current_sprite is None:
            return  # Não faz nada se o sprite for None

        move_distance = self.velocidade * delta_time
        direction_x = (player.current_sprite.x + player.current_sprite.width / 2) - (self.current_sprite.x + self.current_sprite.width / 2)
        direction_y = (player.current_sprite.y + player.current_sprite.height / 2) - (self.current_sprite.y + self.current_sprite.height / 2)
        
        # Normaliza a direção
        distance = (direction_x**2 + direction_y**2)**0.5
        if distance != 0:
            direction_x /= distance
            direction_y /= distance

        # Move o Pingoso na direção do jogador
        self.current_sprite.x += direction_x * move_distance
        self.current_sprite.y += direction_y * move_distance

        # Atualiza o sprite atual com base na direção do movimento
        if direction_x > 0:
            new_sprite = self.sprites["direita"]
        else:
            new_sprite = self.sprites["esquerda"]
        
        # Reinicia a animação se o sprite mudou
        if new_sprite != self.current_sprite:
            new_sprite.set_position(self.current_sprite.x, self.current_sprite.y)
            new_sprite.set_total_duration(500)
            self.current_sprite = new_sprite


        
        # Atualiza a animação do current_sprite
        self.current_sprite.update()

    def draw(self):
        if self.current_sprite is not None:
            # Desenha o current_sprite do Pingoso na tela
            self.current_sprite.draw()

