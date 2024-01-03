import pygame, random, variables as var, json

from scripts.player.player import Player
from scripts.powerups.apple import Apple


class Game:
    def __init__(self):
        self.isPlaying = False

        self.clock = pygame.time.Clock()
        self.gameInterval = var.GAME_INTERVAL

        self.game_screen = pygame.surface.Surface(var.GAME_SCREEN_SIZE)
        self.player = Player(self, (var.GAME_CELL_SIZE, var.GAME_CELL_SIZE))
        self.powerups = pygame.sprite.Group()
        
        self.initalizeGame()

        self.data = []


    def update(self):
        if self.isPlaying:
            current_time = pygame.time.get_ticks()
            self.player.update()

            if current_time - self.last_move_time >= self.gameInterval:
                self.initializeGrid()

                self.powerups.draw(self.game_screen)

                for powerUp in self.powerups.sprites():
                    powerUp.check_collision()

                self.player.advance()
                self.player.body.draw(self.game_screen)

                self.last_move_time = current_time
    

    def startGame(self):
        self.isPlaying = True
        self.initalizeGame()

    def loseGame(self):
        self.isPlaying = False

        if self.score > self.highscore:
            with open('./assets/settings.json', 'w') as file:
                self.data["highscore"] = self.score
                json.dump(self.data, file, indent=4)


    def initalizeGame(self):
        with open('./assets/settings.json', 'r') as file:
            self.data = json.load(file)

        self.last_move_time = pygame.time.get_ticks()
        self.initializeGrid()

        self.score = 0
        self.highscore = self.data["highscore"]
        self.powerups.empty()
        self.createPowerup()

        x, y = random.randint(0, var.GAME_COLS-1), random.randint(0, var.GAME_ROWS-1)
        self.player.coords = (x * var.GAME_CELL_SIZE, y * var.GAME_CELL_SIZE)
        self.player.initializePlayer()


    def initializeGrid(self):
        self.game_screen.fill(var.GAME_COLOR)

        for i in range(1, var.GAME_ROWS + 1):
            x = i * var.GAME_CELL_SIZE
            pygame.draw.line(self.game_screen, var.GAME_TILE_COLOR, (x, 0), (x, var.GAME_SCREEN_SIZE[1]))
            pygame.draw.line(self.game_screen, var.GAME_TILE_COLOR, (0, x), (var.GAME_SCREEN_SIZE[0], x))


    def createPowerup(self):
        x, y = random.randint(0, var.GAME_COLS-1), random.randint(0, var.GAME_ROWS-1)

        newPowerUp = Apple(self, (x*var.GAME_CELL_SIZE, y*var.GAME_CELL_SIZE))
        self.powerups.add(newPowerUp)

    
    def addScore(self):
        self.score += var.GAME_SCORE