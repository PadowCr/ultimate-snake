import pygame, variables as var

class PlayerPart(pygame.sprite.Sprite):
    def __init__(self, state, size, color, coords):
        super().__init__()

        self.state = state
        self.size = size
        self.color = color
        self.coords = coords

        self.image = pygame.surface.Surface(self.size)
        self.image.fill(self.color)
        
        self.rect = self.image.get_rect()
        self.move(self.coords)


    def move(self, coords):
        self.coords = coords
        self.rect.topleft = self.coords