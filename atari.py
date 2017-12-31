from random import randrange as rand
import pygame, sys

cell_size = 5
cols = 30
rows = 40

colors = [
    (0 ,0 ,0),
    (255, 85, 85),
    (100, 200, 115),
    (120, 108, 245),
    (255, 140, 50),
    (50, 120, 52),
    (146, 202, 73),
    (150, 161, 218),
    (35, 35, 35)
]

# brick : 1, ball : 2, plate : 3

class atari(object):
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
        self.ball_x = 0
        self.ball_y = 0
        self.plate_x = 0
        self.plate_y = 0
        self.gameover = False
        self.paused = False
        self.score = 0
    def new_board(self):
        brick_start = 3
        layer = 5
        self.board = [[0 for x in range(cols)] for y in range(brick_start)]
        self.board += [[1 for x in range(cols)] for y in range(layer)] # 5 layers brick
        self.board += [[0 for x in range(cols)] for y in range(rows - brick_start - layer)]
        # default board

    def join_matrixes(self, mat1, mat2, mat1_x, mat1_y):
        for cy, row in enumerate(mat1):
            for cx, val in enumerate(mat1):
                mat2[mat1_y+cy][mat1_x+cx] = val


    def new_plate(self):
        self.plate_x = int(cols / 2 - len(self.plate) /2)
        self.plate_y = rows-3
        self.join_matrixes(self.plate, self.board, self.plate_x, self.plate_y)

    def move_plate(self, delta_x):
        new_x = self.plate_x + delta_x

        if new_x < 0:
            new_x = 0
        if new_x + len(self.plate) > cols :
            new_x = cols - len(self.plate)

    def move_ball(self):
        self.collision()
        self.ball_x += self.ball_speed[0]
        self.ball_y += self.ball_speed[1]
        self.board[ball_x][ball_y] = 2
        if ball_y == rows :
            self.gameover = True


    def center_msg(self, msg):
        for i, line in enumerate(msg.splitlines()):
            msg_image = self.default_font.render(line, False,
                                                 (255, 255, 255), (0, 0, 0))

            msgim_center_x, msgim_center_y = msg_image.get_size()
            msgim_center_x //= 2
            msgim_center_y //= 2

            self.screen.blit(msg_image, (
                self.width // 2 - msgim_center_x,
                self.height // 2 - msgim_center_y + i*22))
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
                            (off_y+y) *
                            cell_size,
                            cell_size,
                            cell_size), 0)


    def run(self):
        dont_burn_my_cpu = pygame.time.Clock()
        while True:
            # display update
            self.screen.fill((0, 0, 0))
            if self.gameover:
                self.center_msg("""Game Over Horse! \n
                Your score : %d Press space to continue""" % self.score)
            else:
                if self.paused:
                    self.center_msg("Paused horse!")
                else:
                    self.draw_matrix(self.board, (0,0))
                    self.draw_matrix()
                    pass

            pygame.display.update()

            for event in pygame.event.get():
                # do it
                pass

            dont_burn_my_cpu(maxfps)




