import pygame

## VERY IMPORTANT, CRIAR UMA CLASSE PLAYER GENÉRICA, DEPOIS HERDAR ELA PRA CADA AÇÃO DO PERSONAGEM

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.sprites = []
        for img in range(0, 24 ):
            self.sprites.append(pygame.image.load(f'src/assets/ladino/actions/crouched/{img}.png'))
        self.atual = 0
        self.image = self.sprites[0]
        self.image = pygame.transform.scale(self.image, (72, 68))
        self.rect = self.image.get_rect()
        self.rect.topleft = (100, 112)
    
    def update(self):
        self.atual += 0.05
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (72, 68))


class PlayerRunning(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.sprites = []
        for img in range(0, 24 ):
            self.sprites.append(pygame.image.load(f'src/assets/ladino/actions/run/{img}.png'))
        self.atual = 0
        self.image = self.sprites[0]
        
        self.rect = self.image.get_rect()
        self.rect.topleft = (200, 100)
    
    def update(self):
        self.atual += 0.1
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        
