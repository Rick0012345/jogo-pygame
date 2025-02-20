from src.game import *
from src.sprites.base_sprites import Ladino, LadinoRunningJump

lista = pygame.sprite.Group()

ladino = Ladino()
ladino_running_jump = LadinoRunningJump()

lista.add(ladino)
lista.add(ladino_running_jump)

jogo = Game(800, 600, title="Jogo Pygame")
jogo.run(todas_as_sprites=lista, tela=jogo.screen)
