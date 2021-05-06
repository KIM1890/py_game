import pygame

# khởi tạo thư viện cho pygame
pygame.init()

# tạo cửa sổ windows với width and height
screen = pygame.display.set_mode((500, 500))

# thiet lap icon

pygame.display.set_icon(pygame.image.load('img_game.png'))


# thiet lap title cua window
pygame.display.set_caption('Hello World')

# tao cua so xuat hien lien tuc cho toi khi tat
x = 60
y = 60
color = (0, 128, 255)
is_red = False
done = False
# xu ly su kien
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_red = not is_red
            if is_red:
                color = (255, 0, 0)

            else:
                color = (0, 128, 255)
    # khi nhan phim space se chuyen mau hinh chu nhat
    pygame.draw.rect(screen, color, pygame.Rect(x, y, 90, 90))
    # cap nhat hien thi tren cua so
    pygame.display.update()
    # pygame.display.flip()
