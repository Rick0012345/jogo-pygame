import pygame
from pygame.locals import *
from sys import exit

class Game:
    def __init__(self, width=640, height=480, title="Spring"):
        # Inicializa o Pygame
        pygame.init()

        # Configurações da tela
        self.width = width
        self.height = height
        self.title = title

        # Cria a tela
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)

    def run(self):
        # Loop principal do jogo
        while True:
            self.handle_events()  # Trata os eventos
            self.update()         # Atualiza o estado do jogo
            self.render()        # Desenha tudo na tela

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
        self.screen.fill((0, 0, 0))

        # Atualiza a tela
        pygame.display.flip()

    def quit(self):
        # Encerra o Pygame e sai do programa
        pygame.quit()
        exit()

# Cria uma instância do jogo e executa
if __name__ == "__main__":
    game = Game()
    game.run()