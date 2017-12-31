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
        self.board = None
        self.ball = [1]
        self.plate = [3 for i in range(4)]
        self.ball_speed = [0, 0]
        self.ball_x = 0
        self.ball_y = 0
        self.plate_x = 0
        self.plate_y = 0
        self.gameover = False
        self.paused = False
        self.score = 0
        self.stage = 1

    # Check ball collision and handle it
    def collision(self):
        # when collide to wall
        if ([self.ball_x, self.ball_y] == [0 , 0])\
                or ([self.ball_x, self.ball_y] == [cols, 0]):
            self.ball_speed = [-self.ball_speed[0], -self.ball_speed[1]]
        elif self.ball_x == 0 or self.ball == cols:
            self.ball_speed = [-self.ball_speed[0], self.ball_speed[1]]
        elif self.ball_y == 0:
            self.ball_speed = [self.ball_speed[0], -self.ball_speed[1]]
        elif self.ball_y == rows:
            return
        # when collide to brick or plate
        else:
            check_corner = True
            for i, off in enumerate([(0, -1), (1, 0), (0, 1), (-1, 0)]):
                x = self.ball_x + off[0]
                y = self.ball_y + off[1]
                val = self.board[x][y]
                if not val:
                    check_corner = False
                    if i == 0 or i == 3:
                        self.ball_speed = [self.ball_speed[0], -self.ball_speed[1]]
                    else:
                        self.ball_speed = [-self.ball_speed[0], self.ball_speed[1]]
                # delete brick
            if check_corner:
                for i, off in enumerate([(-1, -1), (1, -1), (1, 1), (-1, 1)]):
                    if not self.board[x][y]:
                        self.ball_speed = [-self.ball_speed[0], -self.ball_speed[1]]
                        break



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
