import pygame
import sys
from pygame.locals import *
import os
# Thiet lap ban dau
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Game Map")
WINDOWS_SIZE = (600, 400)
screen = pygame.display.set_mode(WINDOWS_SIZE, 0, 32)

# Chi cho hien thi chieu rong 300 va cao 200

display = pygame.Surface((300, 200))

game_map = [['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
             '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
             '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
             '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '2', '2', '2',
             '2', '2', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
             '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['2', '2', '0', '0', '0', '0', '0', '0', '0', '0',
             '0', '0', '0', '0', '0', '0', '0', '2', '2'],
            ['1', '1', '2', '2', '2', '2', '2', '2', '2', '2',
             '2', '2', '2', '2', '2', '2', '2', '1', '1'],
            ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
             '1', '1', '1', '1', '1', '1', '1', '1', '1'],
            ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
             '1', '1', '1', '1', '1', '1', '1', '1', '1'],
            ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
             '1', '1', '1', '1', '1', '1', '1', '1', '1'],
            ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
             '1', '1', '1', '1', '1', '1', '1', '1', '1'],
            ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1']]

grass_img = pygame.image.load(os.path.join('images', 'grass.png'))
dirt_img = pygame.image.load(os.path.join('images', 'dirt.png'))


# kiểm tra sự va chạm của người chơi
def collision_test(rect, tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    # tra ve
    return hit_list


# kiem tra su cham giua nguoi choi va grass o cac vi tri de thiet lap lai nguoi choi
def move(rect, movement, tiles):
    # kieu du lieu Dic
    collision_types = {'top': False, 'bottom': False,
                       'right': False, 'left': False}
    rect.x += movement[0]
    # goi ham colliston_test de kiem tra su va cham
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[0] > 0:
            rect.right = tile.left
            collision_types['right'] = True
        elif movement[0] < 0:
            rect.left = tile.right
            collision_types['left'] = True
    rect.y += movement[1]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[1] > 0:
            rect.bottom = tile.top
            collision_types['bottom'] = True
        elif movement[1] < 0:
            rect.top = tile.bottom
            collision_types['top'] = True
    return rect, collision_types


running = True
while running:
    display.fill((51, 153, 255))
    tile_rects = []
    y = 0
    # bat su kien trong pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # # Duyet list de chen hinh anh tao map
    for layer in game_map:
        x = 0
        for tile in layer:
            if tile == '1':
                display.blit(dirt_img, (x * 16, y * 16))
            if tile == '2':
                display.blit(grass_img, (x * 16, y * 16))
            if tile != '0':
                tile_rects.append(pygame.Rect(x * 16, y * 16, 16, 16))
            x += 1
        y += 1

    screen.blit(pygame.transform.scale(display, WINDOWS_SIZE), (0, 0))
    pygame.display.update()
    # pygame.display.flip()
    clock.tick(60)
