import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.sprites = []
        self.atual = 0
        self.image = None
        self.rect = pygame.Rect(0, 0, 72, 68)
        self.posicao_inicial = (0, 0)
        self.animation_speed = 0.09

    def load_sprites(self, sprite_folder, num_images):
        self.sprites = []
        for img in range(num_images):
            self.sprites.append(pygame.image.load(f'src/assets/{sprite_folder}/{img}.png'))
        
        if self.sprites:
            self.image = self.sprites[0]
            self.rect = self.image.get_rect()
            self.posicao_inicial = self.rect.topleft

    def update(self):
        if self.sprites:
            self.atual += self.animation_speed
            if self.atual >= len(self.sprites):
                self.atual = 0
            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image, self.rect.size)

class PlayerRunning(Player):
    def __init__(self):
        super().__init__()
        self.speed = 5

    def move(self, x, y):
        self.rect.x += x * self.speed
        self.rect.y += y * self.speed

class PlayerJump(Player):
    def __init__(self):
        super().__init__()
        self.jump_height = 20
        self.gravity = 1.5
        self.velocity_y = 0
        self.jumping = False
        self.on_ground = True
        self.start_y = None
        self.max_jump_height = 50

    def update(self):
        super().update()

        if int(self.atual) == 6 and self.on_ground and not self.jumping:
            self.velocity_y = -self.jump_height
            self.jumping = True
            self.on_ground = False
            self.start_y = self.rect.y

        if self.jumping:
            self.rect.y += self.velocity_y

            if self.rect.y <= self.start_y - self.max_jump_height:
                self.velocity_y = self.gravity
            
            if self.rect.y >= self.start_y:
                self.rect.y = self.start_y
                self.jumping = False
                self.on_ground = True

        if self.jumping:
            if int(self.atual) == 6:
                self.image = self.sprites[6]
            if int(self.atual) == 7:
                self.image = self.sprites[7]
        if self.on_ground:
            if int(self.atual) == 5:
                self.image = self.sprites[5]
            if int(self.atual) == 8:
                self.image = self.sprites[8]
            else:
                self.image = self.sprites[0]

        super().update()
