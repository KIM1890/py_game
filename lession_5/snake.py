import pygame
import sys
import random


class Snake(object):
    def __init__(self):
        self.length = 1
        self.position = [((screen_width/2), (screen_height/2))]
        self.direction = random.choice([up, down, right, left])
        self.color = (0, 20, 51)
        self.score = 0

    def get_head_position(self):
        # return self.positions[0]
        pass

    def turn(self, point):
        if self.length > 1 and (point[0]*-1, point[1]*-1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction

        new = (((cur[0]+(x*gridsize)) % screen_width),
               (cur[1]+(y*gridsize)) % screen_height)
        if len(self.position) > 2 and new in self.position[2:]:
            self.reset()
        else:
            self.position.insert(0, new)
            if len(self.position) > self.length:
                self.position.pop()

    def reset(self):
        self.length = 1
        self.positions = [((screen_width/2), (screen_height/2))]
        self.direction = random.choice([up, down, left, right])
        self.score = 0

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (gridsize, gridsize))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, (93, 216, 228), r, 1)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(up)
                elif event.key == pygame.K_DOWN:
                    self.turn(down)
                elif event.key == pygame.K_RIGHT:
                    self.turn(right)
                elif event.key == pygame.K_LEFT:
                    self.turn(left)


class Food(object):
    def __init__(self):
        self.position = (0, 0)
        self.color = (0, 0, 255)
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, grid_width-1) *
                         gridsize, random.randint(0, grid_height-1)*gridsize)
        # self.position = (random.randint(0, grid_width-1)*gridsize,
        #                  random.randint(0, grid_height-1)*gridsize)

    def draw(self, surface):
        r = pygame.Rect(
            (self.position[0], self.position[1]), (gridsize, gridsize))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (0, 0, 255), r, 4)

# vẽ bàn cờ caro
def drawGrid(surface):
    for y in range(0, int(grid_height)):
        for x in range(0, int(grid_width)):
            if (x+y) % 2 == 0:
                r = pygame.Rect((x*gridsize, y*gridsize), (gridsize, gridsize))
                # pygame.draw.rect(surface, (93, 216, 228), r)
                pygame.draw.rect(surface, (204, 102, 0), r)
            else:
                rr = pygame.Rect((x*gridsize, y*gridsize),
                                 (gridsize, gridsize))
                # pygame.draw.rect(surface, (84, 194, 205), rr)
                pygame.draw.rect(surface, (84, 194, 205), rr)


screen_width = 480
screen_height = 480

gridsize = 20
grid_width = screen_width/gridsize
grid_height = screen_height/gridsize

up = (0, -1)
down = (0, 1)
left = (-1, 0)
right = (1, 0)


def main():

    # init + background
    pygame.init()

    pygame.display.set_caption('Game Snake')
    # time clock
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    drawGrid(surface)

    snake = Snake()
    food = Food()

    myfont = pygame.font.SysFont("monospace", 20)

    while (True):
        clock.tick(8)
        snake.handle_keys()
        drawGrid(surface)
        snake.move()
        if snake.get_head_position() == food.position:
            snake.length += 1
            snake.score += 1
            food.randomize_position()
        snake.draw(surface)
        food.draw(surface)
        screen.blit(surface, (0, 0))
        text = myfont.render("SCORE: {0}".format(snake.score), True, (0, 0, 0))
        screen.blit(text, (5, 10))
        pygame.display.update()


main()
