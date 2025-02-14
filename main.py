from src.game import *
from src.character import Player, PlayerRunning

lista = pygame.sprite.Group()
player_run = PlayerRunning()
player = Player()
sp = [player, player_run]
for s  in sp:
    lista.add(s)

jogo = Game(800, 600, title="Jogo Pygame")

jogo.run(todas_as_sprites=lista, tela=jogo.screen)
