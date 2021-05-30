import pygame
import random
from car import Car

pygame.init()

GREEN = (20, 255, 140)
GREY = (210, 210, 210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)

SCREENWIDTH = 400
SCREENHEIGHT = 500

# thiet lap kich thuoc cua so

size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Car Racing')

# danh sach chua tat ca cac nhan vat se duoc su dung
all_sprites_list = pygame.sprite.Group()
# khoi tao doi tuong Car mau do voi kich thuoc 20x30
playerCar = Car(RED, 20, 30)
# dat car o vi tri toa do X,Y
playerCar.rect.x = 200
playerCar.rect.y = 300
# them doi tuong Car vao list
all_sprites_list.add(playerCar)
# allowing the user to close the window...

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                running = True
    # khi cac phim mui ten left, right duoc nhan
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        playerCar.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        playerCar.moveRight(5)
    # update
    all_sprites_list.update()
    # doi mau nen
    screen.fill(GREEN)
    # ve duong dua
    pygame.draw.rect(screen, GREY, (40, 0, 200, 300))

    # ve vach trang tren duong dua
    pygame.draw.line(screen, WHITE, (140, 0), (140, 300), 5)

    # chen o to vao duong dua
    all_sprites_list.draw(screen)
    # refresh man hinh

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
