from PPlay.sprite import Sprite

class Player:
    def __init__(self, x, y):
        # Inicializa os sprites do jogador para cada direção
        self.sprites = {
            "frente": Sprite("templates/Player/cavemia_frente.png", 4),
            "esquerda": Sprite("templates/Player/cavemia_esquerda.png", 4),
            "tras": Sprite("templates/Player/cavemia_tras.png", 4),
            "direita": Sprite("templates/Player/cavemia_direita.png", 4)
        }
        # Define o sprite atual como o sprite de frente
        self.current_sprite = self.sprites["frente"]
        # Define a posição inicial do sprite
        self.current_sprite.set_position(x, y)
        # Define a duração total da animação do sprite
        self.current_sprite.set_total_duration(500)
        # Define a velocidade base do jogador
        self.velocidade = 160
        
        # 
        # ADICIONAR VIDA
        # 

    def move(self, direction, limites_W, limites_S, limites_A, limites_D, delta_time):
        # Calcula a distância de movimento com base na velocidade e delta time
        move_distance = self.velocidade * delta_time

        # Move o jogador na direção especificada se dentro dos limites
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
        # Altera o sprite atual para o sprite da direção especificada
        x, y = self.current_sprite.x, self.current_sprite.y
        self.current_sprite = self.sprites[direction]
        self.current_sprite.set_position(x, y)
        self.current_sprite.set_total_duration(500)
        self.current_sprite.update()

    def draw(self):
        # Desenha o sprite atual na tela
        self.current_sprite.draw()

    def colide_porta(self, porta: Sprite):
        area_porta = [porta.x - porta.width/2 - 10, porta.y - porta.height/2 - 10, \
                    porta.x+porta.width/2, porta.y + porta.height/2]
        return (area_porta[0] <= self.current_sprite.x <= area_porta[2] and \
            area_porta[1] <= self.current_sprite.y <= area_porta[3])