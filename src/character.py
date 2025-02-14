import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.sprites = []
        for img in range(0, 24 ):
            self.sprites.append(pygame.image.load(f'src/assets/ladino/actions/crouched/{img}.png'))
        self.image = self.sprites[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = (100, 100)