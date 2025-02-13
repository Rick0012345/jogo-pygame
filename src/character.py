import pygame
import os

class Player(pygame.sprite.Sprite):
    def __init__(self, sprite_folder, position, animation_speed=0.1):
        super().__init__()
        
        # Carrega todas as sprites da pasta
        self.sprites = []
        for filename in sorted(os.listdir(os.path.join(sprite_folder, 'assets', 'ladino', 'actions', 'crouched'))):
            if filename.endswith('.png'):  # Supondo que as sprites são arquivos PNG
                sprite = pygame.image.load(os.path.join(sprite_folder, 'assets', 'ladino', 'actions', 'crouched', filename)).convert_alpha()
                self.sprites.append(sprite)
        
        # Define a imagem inicial
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect(topleft=position)
        
        # Configurações da animação
        self.animation_speed = animation_speed
        self.last_update = pygame.time.get_ticks()
    
    def update(self):
        # Atualiza a animação
        now = pygame.time.get_ticks()
        if now - self.last_update > self.animation_speed * 1000:  # Converte para milissegundos
            self.last_update = now
            self.current_sprite = (self.current_sprite + 1) % len(self.sprites)
            self.image = self.sprites[self.current_sprite]

