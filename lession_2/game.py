import pygame
import random
from car import Car

# Khởi tạo cửa sổ game 
pygame.init()

# Khai báo các hằng số trong game 
GREEN = (20, 255, 140)
GREY = (210, 210, 210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)

SCREENWIDTH = 400
SCREENHEIGHT = 500

# thiet lap kich thuoc cua so

size = (SCREENWIDTH, SCREENHEIGHT)

# set kích thước cho cửa sổ 
screen = pygame.display.set_mode(size)

# Đặt tên cho chương trình game 
pygame.display.set_caption('Car Racing')

# Danh chứa tất cả các nhân vật trong game 
all_sprites_list = pygame.sprite.Group()

# Khởi tạo đối tượng car
playerCar = Car(RED, 20, 30)

# dat car o vi tri toa do X,Y
playerCar.rect.x = 200
playerCar.rect.y = 300

# them doi tuong Car vao list
# all_sprites_list.add(playerCar)
all_sprites_list.add(playerCar)

# Khởi tạo bộ đếm thời gian
clock = pygame.time.Clock()

# Vòng lặp cho video game 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                running = True
    # khi cac phim mui ten left, right duoc nhan
    # keys = pygame.key.get_pressed()
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        playerCar.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        playerCar.moveRight(5)
    # update
    all_sprites_list.update()
    all_sprites_list.update()

    # doi mau nen cho game
    screen.fill(GREEN)
    # ve duong dua
    pygame.draw.rect(screen, GREY, (40, 0, 200, 300))
    # pygame.draw.rect(screen,GREY,(40,0,200,300))

    # ve vach trang tren duong dua
    pygame.draw.line(screen, WHITE, (140, 0), (140, 300), 5)
    # pygame.draw.line(screen,WHITE,(),(),10)

    # chen o to vao duong dua
    all_sprites_list.draw(screen)
    all_sprites_list.draw(screen)

    # refresh man hinh
    pygame.display.flip()

    # thiết lập tốc độ cho bộ đếm thời gian 
    clock.tick(60)

pygame.quit()
