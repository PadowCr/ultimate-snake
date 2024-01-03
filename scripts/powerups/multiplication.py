import pygame, variables as var

class Multiplication(pygame.sprite.Sprite):
    def __init__(self, game, coords):
        super().__init__()
        self.game = game
        self.coords = coords

        self.image = pygame.surface.Surface((var.GAME_CELL_SIZE, var.GAME_CELL_SIZE))
        self.image.fill(var.MULTI_COLOR)

        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = self.coords

    
    def check_collision(self):
        if self.rect.colliderect(self.game.player.body.sprites()[0].rect):
            self.game.powerups.remove(self)
            self.game.addScore()
            self.game.player.multiplyBody()
            self.game.createPowerup()