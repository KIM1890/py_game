import random
position = [(240, 240)]

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 480

GRIDSIZE = 20
GRID_WIDTH = SCREEN_WIDTH / GRIDSIZE
GRID_HEIGHT = SCREEN_HEIGHT / GRIDSIZE

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

direction = random.choice([UP, DOWN, LEFT, RIGHT])

position = [(240, 240), (250, 250)]

a = [1, 2, 3, 4, 5]

a.pop()

print(a)