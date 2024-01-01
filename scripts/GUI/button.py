import pygame, variables as var

class Button:
    def __init__(self, gui, size, color, coords):
        self.gui = gui

        self.size = size
        self.color = color
        self.coords = coords

        self.image = pygame.surface.Surface(self.size)
        self.image.fill(self.color)

        self.rect = self.image.get_rect()
        self.rect.topleft = self.coords

        self.clicked = False
    

    def update(self):
        if pygame.mouse.get_pressed()[0] and not self.clicked:
            mouvePosition = tuple(t1 - t2 for t1, t2 in zip(pygame.mouse.get_pos(), (var.GAME_SCREEN_SIZE[0], 0)))
            if self.rect.collidepoint(mouvePosition):
                self.clicked = True
                self.gui.game.startGame()

        if not pygame.mouse.get_pressed()[0] and self.clicked:
            self.clicked = False