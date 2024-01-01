import pygame, variables as var
from scripts.player.playerPart import PlayerPart

class Player(pygame.sprite.Sprite):
    def __init__(self, game, startPosition):
        super().__init__()
        self.game = game

        self.coords = startPosition
        self.direction = var.PlayerDirection.RIGHT

        self.body = pygame.sprite.Group()
        self.initializePlayer()

        self.body.add(PlayerPart(var.PlayerPartState.BODY, var.PLAYER_SIZE, var.PLAYER_COLOR_BODY, (self.coords[0] - var.PLAYER_SIZE[0], self.coords[1])))


    def initializePlayer(self):
        self.body.empty()

        playerHead = PlayerPart(var.PlayerPartState.HEAD, var.PLAYER_SIZE, var.PLAYER_COLOR_HEAD, self.coords)
        self.body.add(playerHead)
    

    def update(self):
        self.keys()
        self.check_collision()


    def advance(self):
        if(self.direction == var.PlayerDirection.LEFT):
            self.move_left()

        elif(self.direction == var.PlayerDirection.RIGHT):
            self.move_right()

        elif(self.direction == var.PlayerDirection.TOP):
            self.move_top()

        else:
            self.move_bottom()

        playerSprites = self.body.sprites()
        for i in range(1, len(playerSprites)):
            playerSprites[-i].move(playerSprites[-i-1].coords)

        playerSprites[0].move(self.coords)


    def addBodyPart(self):
        playerSprites = self.body.sprites()

        if self.direction == var.PlayerDirection.LEFT:
            newCoords = (playerSprites[-1].coords[0] + var.PLAYER_SIZE[0], playerSprites[-1].coords[1])

        elif self.direction == var.PlayerDirection.RIGHT:
            newCoords = (playerSprites[-1].coords[0] - var.PLAYER_SIZE[0], playerSprites[-1].coords[1])

        elif self.direction == var.PlayerDirection.TOP:
            newCoords = (playerSprites[-1].coords[0], playerSprites[-1].coords[1] + var.PLAYER_SIZE[1])

        else:
            newCoords = (playerSprites[-1].coords[0], playerSprites[-1].coords[1] - var.PLAYER_SIZE[1])
        
        self.body.add(PlayerPart(var.PlayerPartState.BODY, var.PLAYER_SIZE, var.PLAYER_COLOR_BODY, newCoords))


    def check_collision(self):
        for sprite in self.body.sprites():
            if self.body.sprites()[0].rect.colliderect(sprite.rect):
                if sprite.state != var.PlayerPartState.HEAD:
                    self.game.loseGame()



    ######### GESTION DU MOUVEMENTS #########
    def keys(self):
        keys = pygame.key.get_pressed()

        if(keys[pygame.K_z] and self.direction != var.PlayerDirection.BOTTOM):
            self.direction = var.PlayerDirection.TOP

        if(keys[pygame.K_s] and self.direction != var.PlayerDirection.TOP):
            self.direction = var.PlayerDirection.BOTTOM

        if(keys[pygame.K_q] and self.direction != var.PlayerDirection.RIGHT):
            self.direction = var.PlayerDirection.LEFT

        if(keys[pygame.K_d] and self.direction != var.PlayerDirection.LEFT):
            self.direction = var.PlayerDirection.RIGHT
    

    def move_left(self):
        if(self.coords[0] == 0):
            self.coords = (var.GAME_SCREEN_SIZE[0] - var.PLAYER_SIZE[0], self.coords[1])
        else:
            self.coords = tuple(t1 - t2 for t1, t2 in zip(self.coords, (var.PLAYER_SIZE[0], 0)))

    def move_right(self):
        if(self.coords[0] == var.GAME_SCREEN_SIZE[0] - var.PLAYER_SIZE[0]):
            self.coords = (0, self.coords[1])
        else:
            self.coords = tuple(t1 + t2 for t1, t2 in zip(self.coords, (var.PLAYER_SIZE[0], 0)))

    def move_top(self):
        if(self.coords[1] == 0):
            self.coords = (self.coords[0], var.GAME_SCREEN_SIZE[1] - var.PLAYER_SIZE[1])
        else:
            self.coords = tuple(t1 - t2 for t1, t2 in zip(self.coords, (0, var.PLAYER_SIZE[1])))
    
    def move_bottom(self):
        if(self.coords[1] == var.GAME_SCREEN_SIZE[1] - var.PLAYER_SIZE[1]):
            self.coords = (self.coords[0], 0)
        else:
            self.coords = tuple(t1 + t2 for t1, t2 in zip(self.coords, (0, var.PLAYER_SIZE[1])))