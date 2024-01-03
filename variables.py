import pygame
from enum import Enum

GAME_ROWS, GAME_COLS = 24, 24
GAME_CELL_SIZE = 32
GAME_SCREEN_SIZE = (GAME_ROWS * GAME_CELL_SIZE, GAME_ROWS * GAME_CELL_SIZE)
GAME_COLOR = pygame.Color(15, 23, 42, 1)
GAME_TILE_COLOR = pygame.Color(28, 39, 57, 1)

GAME_INTERVAL = 200
GAME_SCORE = 10

GUI_SIZE = (200, GAME_SCREEN_SIZE[1])
GUI_COLOR = pygame.Color(255,255,255)

SCREEN_SIZE = (GAME_SCREEN_SIZE[0] + GUI_SIZE[0], GAME_SCREEN_SIZE[1])
SCREEN_TITLE = "Ultimate Snake - PADOW"
SCREEN_COLOR = pygame.Color(2, 6, 23, 1)

PLAYER_SIZE = (32, 32)
PLAYER_COLOR_BODY = pygame.Color(101, 163, 13, 1)
PLAYER_COLOR_HEAD = pygame.Color(180, 83, 9, 1)

APPLE_COLOR = pygame.Color(185, 28, 28, 1)
MULTI_COLOR = pygame.Color(2,132,199, 1)
DIVIDE_COLOR = pygame.Color(192,38,211, 1)

class PlayerPartState(Enum):
    HEAD = 0
    BODY = 1


class PlayerDirection(Enum):
    LEFT = 0
    RIGHT = 1
    TOP = 2
    BOTTOM = 3