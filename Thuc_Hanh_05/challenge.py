import pygame
import sys
import random
from pygame import draw

# create snake object


class Snake(object):
    def __init__(self):
        pass

    def get_head_position(self):
        pass

    def turn(self, point):
        pass

    def move(self):
        pass

    def reset(self):
        pass

    def draw(self, surface):
        pass

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                pass
            '''Tiếp tục code tại đây'''

        # create food object


class Food(object):
    def __init__(self):
        pass

    def randomize_position(self):
        pass

    def draw(self, surface):
        pass

# draw coordinates for grid game


def drawGrid(surface):
    pass


# kích thước ô cửa sổ game
screen_width = 480
screen_height = 480
# kích thước mỗi ô caro
gridsize = 20
grid_width = screen_width/gridsize
grid_height = screen_height/gridsize

# lưu phương hướng cho con rắn
up = (0, -1)
down = (0, 1)
left = (-1, 0)
right = (1, 0)
# build main function


def main():
    # khoi tao pygame
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((500, 500))
    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    drawGrid(surface)
    '''Tạo rắn và thức ăn cho rắn'''
    myfont = pygame.font.SysFont('monospace', 16)
    score = 0
    run = True
    # vòng lặp chính của game
    while run:
        # Quy định game chạy với tốc độ 10 khung hình 1 giây
        clock.tick(10)
        ##########snakes##########
        # gọi handle_keys
        # vẽ bàn cờ caro
        # gọi hàm move
        '''điều kiện khi mà rắn nó ăn mồi'''
        # vẽ lại rắn và đồ ăn
        # gọi hàm vẽ con rắn
        ##########food###########
        # Vẽ đồ ăn mà rắn sẽ ăn
        screen.blit(surface, (0, 0))
        '''Tạo một ô nhở để hiển thị điểm số'''
        text = 'code in here'
        screen.blit(text, (5, 10))
        pygame.display.update()


# gọi hàm main
main()
