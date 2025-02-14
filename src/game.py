import pygame
from pygame.locals import *
from sys import exit
from src.static.style.cores import Cores

class Game:
    def __init__(self, width, height, title):
        # Inicializa o Pygame
        pygame.init()

        # Configurações da tela
        self.width = width
        self.height = height
        self.title = title

        # Cria a tela
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)

    def run(self,todas_as_sprites):
        # Loop principal do jogo
        while True:
            self.handle_events()  # Trata os eventos
            self.update()         # Atualiza o estado do jogo
            self.render()        # Desenha tudo na tela
            todas_as_sprites.draw(self.screen)
            todas_as_sprites.update()
    def handle_events(self):
        # Trata os eventos do Pygame
        for event in pygame.event.get():
            if event.type == QUIT:
                self.quit()

    def update(self):
        # Atualiza o estado do jogo (neste exemplo, não há nada para atualizar)
        pass

    def render(self):
        # Preenche a tela com a cor preta
        self.screen.fill(Cores.PRETO)

        # Atualiza a tela
        pygame.display.flip()

    def quit(self):
        # Encerra o Pygame e sai do programa
        pygame.quit()
        exit()

# Cria uma instância do jogo e executa
if __name__ == "__main__":
    game = Game( 800, 600, title="Jogo Pygame")
    game.run()