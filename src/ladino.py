import pygame
from src.moves_player import Player, PlayerRunning, PlayerJump

class Ladino(Player):
    def __init__(self):
        super().__init__()
        self.load_sprites('ladino/actions/crouched', 24)
        self.rect.topleft = (100, 112)
        self.rect.size = (72, 68)

    def update(self):
        super().update()


class LadinoRunningJump(Player):
    def __init__(self):
        super().__init__()
        self.load_sprites('ladino/actions/run', 9)
        self.rect.topleft = (200, 400)
        self.rect.size = (72, 68)
        self.jump_height = 20
        self.gravity = 1.5
        self.velocity_y = 0
        self.jumping = False
        self.on_ground = True
        self.start_y = None
        self.max_jump_height = 50

    def update(self):
        super().update()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

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