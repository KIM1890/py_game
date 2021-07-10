import pygame
import sys

# khoi tao game
pygame.init()

# thiet lap man hinh cho game
screen = pygame.display.set_mode((500, 500))

# fill background
screen.fill((255, 255, 255))

# tao caption cho screen
pygame.display.set_caption('drawing shape')

# create icon
pygame.display.set_icon(pygame.image.load('img_game.png'))

# drawing shape
# drawing a rectangle
pygame.draw.rect(screen, (184, 54, 1), pygame.Rect(200, 150, 100, 50))

# drawing a circle
pygame.draw.circle(screen, (237, 219, 46), (300, 50), 20, 0)
# drawing a line
pygame.draw.line(screen, (46, 103, 237), (60, 60), (120, 60), 5)

# drawing polygon
pygame.draw.polygon(screen, (229, 46, 237), ((145, 0),
                                             (291, 106), (236, 277), (56, 277), (0, 0)))


# drawing eclipse
pygame.draw.ellipse(screen, (237, 46, 123), (200, 150, 100, 50))

done = False
# background image
# background_image = pygame.image.load("ocean.jpg").convert()
# while not done:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True
#     # screen.blit(background_image, [0, 0])
#     # cap nhat hien thi tren cua so
#     pygame.display.flip()
#     pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
