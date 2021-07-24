'''
--install pygame
--simple pygame application
--interactivity
--adding functionality
--adding images(có thể tải về một hình ảnh bất kỳ)
--sound and music
--geometric drawing
--fonts and text
--input models
'''
import pygame
import os

pygame.init()

WIDTH = 500
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Review Pygame')

clock = pygame.time.Clock()
img = pygame.image.load(os.path.join('img', 'Pirates.jpg'))

font = pygame.font.SysFont('Calibri', 50, True, False)
text = font.render('Huỳnh Trí Nhân', True, (255, 102, 0))
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # vẽ hình chữ nhật
    # pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(30, 30, 60, 60))
    # vẽ hình tròn
    # pygame.draw.circle(screen, (0, 128, 255), (300, 60), 50, 10)
    # load image on pygame

    # screen.blit(img, (150, 150))
    # load text on pygame
    screen.blit(text, (100, 150))
    # load music
    pygame.mixer.music.load(os.path.join(
        'music', 'Bionic Commando (2009) - 18 - Piano Theme.mp3'))
    pygame.mixer.music.play()
    pygame.display.update()
    clock.tick(60)
