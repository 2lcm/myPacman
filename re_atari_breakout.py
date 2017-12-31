import pygame
import sys


class atari(object):
    def __init__(self):
        pygame.init()
        pygame.key.set_repeat()
        self.width = 100
        self.height = 200
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.default_font = pygame.font.Font(
            pygame.font.get_default_font(), 12
        )
        self.board = None
        self.ball = [1]
        self.plate = [[3 for i in range(4)]]
        self.ball_speed = [0, 0]
        self.ball_x = 0
        self.ball_y = 0
        self.plate_x = 0
        self.plate_y = 0
        self.gameover = False
        self.paused = False
        self.score = 0
        self.stage = 1
        #self.plate = Rect()

    def

A = atari()