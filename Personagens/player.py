from PPlay.sprite import Sprite
import sys
from PPlay.gameimage import GameImage
from PPlay.collision import Collision
from Personagens.tiro import Tiro  # Corrigir o caminho de importação

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
        
        self.vida = 10  # Vida inicial do jogador
        self.coracao = [] # coração para contagem de vidas do player
        self.invulneravel = False  # Flag para invulnerabilidade temporária
        self.invulnerabilidade_tempo = 3.0  # Duração da invulnerabilidade (em segundos)
        self.invulnerabilidade_timer = 0  # Timer para controlar o estado
        self.tiros = []  # Lista para armazenar os tiros do jogador
        self.tempo_recarga = 0.5  # Tempo de recarga entre os tiros (em segundos)
        self.tempo_ultimo_tiro = 0  # Timer para controlar o tempo desde o último tiro

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

    def tomar_dano(self):
        # Verifica se o jogador pode tomar dano
        if not self.invulneravel:
            self.vida -= 1
            self.invulneravel = True
            self.invulnerabilidade_timer = self.invulnerabilidade_tempo
            if self.vida <= 0:
                self.game_over()
                
    def game_over(self):
        print("Game Over")
        sys.exit()  # Encerra o programa

    def verificar_colisao_com_inimigo(self, inimigos, delta_time):
        for inimigo in inimigos:
            if inimigo.current_sprite is not None and Collision.collided(self.current_sprite, inimigo.current_sprite):
                self.tomar_dano()
                print("Colidiu")
                print("Vida: ", self.vida)
                break  # Adiciona um break para evitar múltiplas colisões no mesmo frame

        # Atualiza o estado de invulnerabilidade
        if self.invulneravel:
            self.invulnerabilidade_timer -= delta_time
            if self.invulnerabilidade_timer <= 0:
                self.invulneravel = False

    def colide_porta(self, porta: Sprite):
        return Collision.collided(self.current_sprite, porta)

    def atirar(self, direction, delta_time):
        # Verifica se o tempo de recarga já passou
        if self.tempo_ultimo_tiro >= self.tempo_recarga:
            print(f"Atirando na direção: {direction}")  # Adiciona print para depuração
            x = self.current_sprite.x + self.current_sprite.width / 2
            y = self.current_sprite.y + self.current_sprite.height / 2
            tiro = Tiro(x, y, direction)
            self.tiros.append(tiro)
            print(f"Tiro adicionado na posição: ({x}, {y})")  # Adiciona print para depuração
            self.tempo_ultimo_tiro = 0  # Reseta o timer de recarga

    def update_tiros(self, delta_time, inimigos):
        self.tempo_ultimo_tiro += delta_time  # Atualiza o timer de recarga
        for tiro in self.tiros[:]:
            tiro.move(delta_time)
            if tiro.colide_com_inimigo(inimigos):
                self.tiros.remove(tiro)

    def draw_tiros(self):
        for tiro in self.tiros:
            tiro.draw()

    def draw(self):
        # Desenha o sprite atual na tela
        self.current_sprite.draw()
    
    def lista_coracao(self): # cria lista de corações que são os contadores de vida do player
        x, y = 12, 20
        self.coracao = []
        for _ in range(self.vida):
            coure = GameImage("templates/contador_de_vida.png")
            coure.set_position(x, y)
            self.coracao.append(coure)
            x+=20

    def draw_vidas(self): # Desenha o númro de corações correspondente ao número de vidas restantes
        self.lista_coracao()
        for i in self.coracao:
            i.draw()
