import pygame
from pygame.locals import *
from sys import exit
from src.static.style.cores import Cores

class Game:
    def __init__(self, width, height, title):
        pygame.init()
        
        self.width = width
        self.height = height
        self.title = title
        
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)
        
        # Carrega e redimensiona o background
        self.background = pygame.image.load('src/assets/background.jpg').convert()
        self.background = pygame.transform.scale(self.background, (width, height))
        
        self.clock = pygame.time.Clock()
        self.FPS = 30

    def run(self,todas_as_sprites, tela, i=0):
        
        while True:
            self.clock.tick(self.FPS)
            self.screen.blit(self.background, (0, 0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.quit() 
    
            todas_as_sprites.draw(tela)
            todas_as_sprites.update()
            
            
            pygame.display.flip()
            self.render()
            i += 1


    def render(self):
        # Preenche a tela com a cor preta
        self.screen.fill(Cores.PRETO)
        

    def quit(self):
        # Encerra o Pygame e sai do programa
        pygame.quit()
        exit()

