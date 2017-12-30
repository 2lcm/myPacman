# Last update : Dec/30/2017
# First update : Dec/30/2017
# Created by ChulMin Lee, ChangYup(?) Shin

import pygame
import sys

cell_size = 5
cols = 30
rows = 40
maxfps = 30

# colors and identity
# 0 : Background
# 1 : Brick
# 2 : Plate
# 3 : Ball
colors = [
    (255, 255, 255)
]

class atari(object):
    # initialize class
    def __init__(self):
        self.width = cell_size * cols
        self.height = cell_size * rows
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.default_font = pygame.font.Font(
            pygame.font.get_default_font(), 12
        )
        self.ball = [1]
        self.plate = [3 for i in range(4)]
        self.ball_speed = [0, 0]
        self.plate_speed = [0, 0]
        self.ball_x = 0
        self.ball_y = 0
        self.plate_x = 0
        self.plate_y = 0
        self.gameover = False
        self.paused = False
        self.score = 0

    # Check ball collision and handle it
    def collision(self):
        # implement code
        pass

    #
    def move(self):
        # implement code
        pass

    def run(self):
        dont_burn_my_cpu = pygame.time.Clock()
        while True:
            # display update
            self.screen.fill((0, 0, 0))
            if self.gameover:
                self.ceter_msg()
            else:
                if self.paused:
                    self.center_msg()
                else:
                    # draw display
                    pass

            pygame.display.update()

            for event in pygame.event.get():
                # do it
                pass

            dont_burn_my_cpu(maxfps)

    def new_board(self):
        # implement code
        pass

    def init_game(self):
        # implement code
        pass

    # display message at center
    def center_msg(self):
        #implement code
        pass
