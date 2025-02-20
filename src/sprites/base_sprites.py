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