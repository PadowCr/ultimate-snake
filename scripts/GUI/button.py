import pygame, variables as var

class Button:
    def __init__(self, gui, size, color, coords):
        self.gui = gui

        self.size = size
        self.color = color
        self.coords = coords

        self.font_size = 24

        self.image = pygame.surface.Surface(self.size)
        
        self.rect = self.image.get_rect()
        self.rect.topleft = self.coords

        self.clicked = False

        self.createButton()

    def update(self):
        if pygame.mouse.get_pressed()[0] and not self.clicked:
            mouvePosition = tuple(t1 - t2 for t1, t2 in zip(pygame.mouse.get_pos(), (var.GAME_SCREEN_SIZE[0], 0)))
            if self.rect.collidepoint(mouvePosition):
                self.clicked = True
                self.updateGame()

        if not pygame.mouse.get_pressed()[0] and self.clicked:
            self.clicked = False


    def createButton(self):
        self.image.fill(self.color)

        font = pygame.font.Font(None, self.font_size)
        text_surface = font.render(str("Commencer"), True, var.GUI_COLOR)
        self.image.blit(text_surface, (self.image.get_width()//2 - text_surface.get_width()//2, self.image.get_height()//2 - text_surface.get_height()//2))


    def updateButton(self):
        self.image.fill(pygame.Color(185, 28, 28, 1))

        font = pygame.font.Font(None, self.font_size)
        text_surface = font.render(str("Arrêter"), True, var.GUI_COLOR)
        self.image.blit(text_surface, (self.image.get_width()//2 - text_surface.get_width()//2, self.image.get_height()//2 - text_surface.get_height()//2))


    def updateGame(self):
        self.gui.game.isPlaying = not self.gui.game.isPlaying

        if self.gui.game.isPlaying:
            self.updateButton()
            self.gui.game.startGame()

        else:
            self.createButton()
            self.gui.game.loseGame()