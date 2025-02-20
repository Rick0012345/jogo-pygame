import pygame

class GenericSprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.sprites = []
        self.atual = 0
        self.image = None
        self.rect = None

    def load_sprites(self, path_pattern, sprites_number):
        for img in range(sprites_number):
            image = pygame.image.load(path_pattern.format(img))
            self.sprites.append(image)

        self.image = self.sprites[self.atual]
        self.rect = self.image.get_rect()

class Player(GenericSprite):
    def __init__(self):
        super().__init__()
        self.load_sprites('src/assets/ladino/actions/crouched/{}.png', sprites_number=24)
        self.rect.topleft = (100, 112)

    def update(self):
        self.atual += 0.05
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]

class PlayerRunning(GenericSprite):
    def __init__(self):
        super().__init__()
        self.load_sprites('src/assets/ladino/actions/run/{}.png', sprites_number=9)
        self.rect.topleft = (200, 400)

    def update(self):
        self.atual += 0.1
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]

