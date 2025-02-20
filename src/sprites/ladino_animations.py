from src.sprites.base_sprites import GenericSprite

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

