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
        pygame.init()
        pygame.key.set_repeat()
        self.width = cell_size * cols
        self.height = cell_size * rows
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

    # Check ball collision and handle it
    def collision(self):
        check_corner = True
        if self.ball_speed[0] > 0:
            val = self.board[self.ball_y][self.ball_x + 1]
            if not val:
                self.ball_speed = [-self.ball_speed[0], self.ball_speed[1]]
                check_corner = False
                if val == 1:
                    self.del_brick(self.ball_x + 1, self.ball_y)
        else:
            val = self.board[self.ball_y][self.ball_x - 1]
            if not val:
                self.ball_speed = [self.ball_speed[0], -self.ball_speed[1]]
                check_corner = False
                if val == 1:
                    self.del_brick(self.ball_x - 1, self.ball_y)

        if self.ball_speed[1] > 0:
            val = self.board[self.ball_y + 1][self.ball_x]
            if not val:
                self.ball_speed = [-self.ball_speed[0], self.ball_speed[1]]
                check_corner = False
                if val == 1:
                    self.del_brick(self.ball_x, self.ball_y + 1)
        else:
            val = self.board[self.ball_y - 1][self.ball_x]
            if not val:
                self.ball_speed = [self.ball_speed[0], -self.ball_speed[1]]
                check_corner = False
                if val == 1:
                    self.del_brick(self.ball_x, self.ball_y - 1)

        if check_corner:
            val = self.board[self.ball_y + self.ball_speed[1]][self.ball_x + self.ball_speed[0]]
            if not val:
                self.ball_speed = [-self.ball_speed[0], -self.ball_speed[1]]
                if val == 1:
                    self.del_brick(self.ball_x + self.ball_speed[0], self.ball_y + self.ball_speed[1])

    def del_brick(self, brick_x, brick_y):
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
        brick_start = 3
        layer = 5
        self.board = [[0 for x in range(cols)] for y in range(brick_start)]
        self.board += [[1 for x in range(cols)] for y in range(layer)]  # 5 layers brick
        self.board += [[0 for x in range(cols)] for y in range(rows - brick_start - layer)]

    def join_matrixes(self, mat1, mat2, mat1_x, mat1_y):
        for cy, row in enumerate(mat1):
            for cx, val in enumerate(row):
                mat2[mat1_y + cy][mat1_x + cx] = val

    def new_plate(self):
        self.plate_x = int(cols / 2 - len(self.plate) / 2)
        self.plate_y = rows - 3
        self.join_matrixes(self.plate, self.board, self.plate_x, self.plate_y)

    def move_plate(self, delta_x):
        new_x = self.plate_x + delta_x

        if new_x < 0:
            new_x = 0
        if new_x + len(self.plate) > cols:
            new_x = cols - len(self.plate)
        self.plate_x = new_x

    def move_ball(self):
        self.collision()
        self.ball_x += self.ball_speed[0]
        self.ball_y += self.ball_speed[1]
        self.board[self.ball_x][self.ball_y] = 2
        if self.ball_y == rows:
            self.gameover = True

    def init_game(self):
        # implement code
        pass

    def draw_matrix(self, matrix, offset):
        off_x, off_y = offset
        for y, row in enumerate(matrix):
            for x, val in enumerate(row):
                if val:
                    pygame.draw.rect(
                        self.screen,
                        colors[val],
                        pygame.Rect(
                            (off_x + x) *
                            cell_size,
                            (off_y + y) *
                            cell_size,
                            cell_size,
                            cell_size), 0)

    # display message at center
    def center_msg(self, msg):
        for i, line in enumerate(msg.splitlines()):
            msg_image = self.default_font.render(line, False,
                                                 (255, 255, 255), (0, 0, 0))

            msgim_center_x, msgim_center_y = msg_image.get_size()
            msgim_center_x //= 2
            msgim_center_y //= 2

            self.screen.blit(msg_image, (
                self.width // 2 - msgim_center_x,
                self.height // 2 - msgim_center_y + i * 22))


A = atari()
A.new_board()
A.new_plate()
A.collision(3)
print("end")