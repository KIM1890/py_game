import pygame
from pygame.locals import *
import os
import sys
import math
import random


pygame.init()

W, H = 800, 447
win = pygame.display.set_mode((W, H))
pygame.display.set_caption('Side Scroller')
# load background
bg = pygame.image.load(os.path.join('images', 'bg.png')).convert()

bgX = 0
bgX2 = bg.get_width()

# thiet lap thoi gian
clock = pygame.time.Clock()

# build player


class Player(object):
    run = [pygame.image.load(os.path.join('images', str(x) + '.png'))
           for x in range(8, 16)]
    jump = [pygame.image.load(os.path.join(
        'images', str(x) + '.png')) for x in range(1, 8)]
    slide = [pygame.image.load(os.path.join('images', 'S1.png')), pygame.image.load(os.path.join('images', 'S2.png')), pygame.image.load(os.path.join('images', 'S2.png')), pygame.image.load(os.path.join('images', 'S2.png')), pygame.image.load(os.path.join('images', 'S2.png')), pygame.image.load(
        os.path.join('images', 'S2.png')), pygame.image.load(os.path.join('images', 'S2.png')), pygame.image.load(os.path.join('images', 'S2.png')), pygame.image.load(os.path.join('images', 'S3.png')), pygame.image.load(os.path.join('images', 'S4.png')), pygame.image.load(os.path.join('images', 'S5.png'))]
    jumpList = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4]
    # load images falling

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.jumping = False
        self.sliding = False
        self.slideCount = 0
        self.jumpCount = 0
        self.runCount = 0
        self.slideUp = False

    def draw(self, win):
        if self.jumping:
            self.y -= self.jumpList[self.jumpCount] * 1.2
            win.blit(self.jump[self.jumpCount//18], (self.x, self.y))
            self.jumpCount += 1
            if self.jumpCount > 108:
                self.jumpCount = 0
                self.jumping = False
                self.runCount = 0
            '''Hitbox for character'''
        elif self.sliding or self.slideUp:
            if self.slideCount < 20:
                self.y += 1
                '''Hitbox for character'''

            elif self.slideCount == 80:
                self.y -= 19
                self.sliding = False
                self.slideUp = True
            '''Hitbox for character'''
            if self.slideCount >= 110:
                self.slideCount = 0
                self.slideUp = False
                '''Hitbox for character'''
                self.runCount = 0
            win.blit(self.slide[self.slideCount//10], (self.x, self.y))
            self.slideCount += 1

        else:
            if self.runCount > 42:
                self.runCount = 0
            win.blit(self.run[self.runCount//6], (self.x, self.y))
            self.runCount += 1
            '''Hitbox for character'''
        '''Draws hitbox'''
        
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)


# obstacles
'''two main obstacles that our player needs to avoid. A saw(răng cưa) and spike(mũi nhọn)'''
# creating a class for our saw


class Saw(object):
    rotate = '''load images array about saw'''

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rotateCount = 0
        self.vel = 1.4
    # bước tiếp theo
    def draw(self, win):
        '''Defines the accurate hitbox for our character'''
        # code in here
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
        # This is what will allow us to animate the saw
        if self.rotateCount >= 8:
            self.rotateCount = 0
        # scales our image down to 64x64 before drawing
        win.blit(pygame.transform.scale(
            self.rotate[self.rotateCount//2], (64, 64)), (self.x, self.y))
        self.rotateCount += 1


# we can code our spike class
'''1.xây dựng lớp vật nhọn
    2. lớp vật nhọn này sẽ kế thừa từ lớp răng cưa
    3.Xây dựng hàm vẽ vật nhọn(code in here)'''


# game loop
run = True
speed = 30
# call class player

runner = Player(200, 313, 64, 64)

'''randomly generating object'''
obstacles = []

# drawing our chracter


def redrawWindow():
    # draws our first bg image
    win.blit(bg, (bgX, 0))
    # draws the second bg image
    win.blit(bg, (bgX2, 0))
    runner.draw(win)
    '''Loops through all obstacles(chướng ngại vật)'''
    # code in here

    pygame.display.update()


# change the background speed
pygame.time.set_timer(USEREVENT+1, 500)
pygame.time.set_timer(USEREVENT+2, random.randrange(2000, 3500))

while run:
    redrawWindow()
    '''moving  the object obstacle This should go in the game loop'''
    for obstacle in obstacles:
        obstacle.x -= 1.4
        # If our obstacle is off the screen we will remove it
        if obstacle.x < obstacle.width * -1:
            obstacles.pop(obstacles.index(obstacle))
    # set time clock
    clock.tick(speed)
    bgX -= 1.4
    # move both background images back
    bgX2 -= 1.4

    if bgX < bg.get_width() * -1:
        bgX = bg.get_width()
    if bgX2 < bg.get_width() * -1:
        bgX2 = bg.get_width()
    # loop through a list of event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()
        ''' This should go in the "for event in pygame.event.get():" loop'''
        if event.type == USEREVENT+2:
            r = random.randrange(0, 2)
            if r == 0:
                obstacles.append(Saw(810, 310, 64, 64))
            elif r == 1:
                obstacles.append(Spike(810, 0, 48, 310))

    # moving our characters
    # should go inside the game loop
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
        if not(runner.jumping):
            runner.jumping = True
    if keys[pygame.K_DOWN]:
        if not(runner.sliding):
            runner.sliding = True
    clock.tick(speed)
