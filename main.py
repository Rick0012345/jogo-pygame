from src.game import *
from src.character import Player
lista = pygame.sprite.Group()
player = Player()
lista.add(player)

jogo = Game(800, 600, title="Jogo Pygame")

jogo.run(todas_as_sprites=lista)
