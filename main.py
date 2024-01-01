import pygame, sys
import variables as var

from scripts.game import Game
from scripts.gui import GUI

class Main:
    def __init__(self):
        pygame.init()
        pygame.display.init()
        pygame.font.init()

        pygame.display.set_caption(var.SCREEN_TITLE)
        self.screen = pygame.display.set_mode(var.SCREEN_SIZE)
        self.screen.fill(var.SCREEN_COLOR)
        
        self.game = Game()
        self.gui = GUI(self.game)


    def update(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.screen.blit(self.game.game_screen, (0, 0))
            self.screen.blit(self.gui.gui_screen, (var.GAME_SCREEN_SIZE[0], 0))

            self.game.update()
            self.gui.update()

            pygame.display.update()
            self.game.clock.tick(120)



"""  Lancement du programme """
if __name__ == '__main__':
    main = Main()
    main.update()