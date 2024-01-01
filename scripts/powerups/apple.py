import pygame, variables as var

class Apple(pygame.sprite.Sprite):
    def __init__(self, game, coords):
        super().__init__()
        self.game = game
        self.coords = coords

        self.image = pygame.surface.Surface((var.GAME_CELL_SIZE, var.GAME_CELL_SIZE))
        self.image.fill(var.APPLE_COLOR)

        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = self.coords

    
    def check_collision(self):
        if self.rect.colliderect(self.game.player.body.sprites()[0].rect):
            self.game.powerups.remove(self)
            self.game.addScore()
            self.game.player.addBodyPart()
            self.game.createPowerup()