import pygame, variables as var

from scripts.GUI.button import Button

class GUI:
    def __init__(self, game):
        self.game = game
        self.gui_screen = pygame.surface.Surface(var.GUI_SIZE)

        self.startButton = Button(self, (120, 50), pygame.Color(109, 40, 217, 1), (50, 600))
        
    def update(self):
        self.gui_screen.fill(var.SCREEN_COLOR)

        self.writeText("Score", 36, var.GUI_COLOR, 30)
        self.writeText(self.game.score, 48, var.GUI_COLOR, 80)

        self.writeText("High Score", 36, var.GUI_COLOR, 200)
        self.writeText(self.game.score, 48, var.GUI_COLOR, 250)

        self.gui_screen.blit(self.startButton.image, self.startButton.rect)
        self.startButton.update()

    def writeText(self, text,  size, color, height):
        font = pygame.font.Font(None, size)
        text_surface = font.render(str(text), True, color)
        self.gui_screen.blit(text_surface, (var.GUI_SIZE[0]//2 - text_surface.get_width()//2, height))