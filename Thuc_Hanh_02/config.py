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

# Thiết lập Car ở vị trí tọa độ X,Y

# Thêm đối tượng Car vào danh sách

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
    # Sự kiện nhấn các phím mũi tên trên bàn phím máy tính
    
    # update các đối tượng trong game đua xe 

    # Đổi khung màu nền cho màn hình video game 
    screen.fill(GREEN)
    # Vẽ đường đua cho video game 

    # Vẽ vạch trắng cho đường đua

    # Đưa Car vào đường đua
    # all_sprites_list.draw(screen)

    # Refresh man hinh giúp thay đổi khi người dùng thêm bất kỳ vào video game
    pygame.display.flip()

    # thiết lập tốc độ cho bộ đếm thời gian 
    clock.tick(60)

# Thoát game nhé khi người dùng nhấn phím thoát
pygame.quit()
