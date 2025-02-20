from src.game import *
from src.sprites.ladino_animations import Player, PlayerRunning

lista = pygame.sprite.Group()

ladino = Player()
ladino_run = PlayerRunning()

lista.add(ladino)
lista.add(ladino_run)

jogo = Game(800, 600, title="Jogo Pygame")
jogo.run(todas_as_sprites=lista, tela=jogo.screen)
