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

# The elements in the hitbox are (top left x, top left y, width, height)


class Player(object):
    run = [pygame.image.load(os.path.join('images', str(x) + '.png'))
           for x in range(8, 16)]
    jump = [pygame.image.load(os.path.join(
        'images', str(x) + '.png')) for x in range(1, 8)]
    slide = [pygame.image.load(os.path.join('images', 'S1.png')), pygame.image.load(os.path.join('images', 'S2.png')), pygame.image.load(os.path.join('images', 'S2.png')), pygame.image.load(os.path.join('images', 'S2.png')), pygame.image.load(os.path.join('images', 'S2.png')), pygame.image.load(
        os.path.join('images', 'S2.png')), pygame.image.load(os.path.join('images', 'S2.png')), pygame.image.load(os.path.join('images', 'S2.png')), pygame.image.load(os.path.join('images', 'S3.png')), pygame.image.load(os.path.join('images', 'S4.png')), pygame.image.load(os.path.join('images', 'S5.png'))]
    jumpList = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4]
    # slide
    slide = [pygame.image.load(os.path.join('images', 'S1.png')), pygame.image.load(os.path.join('images', 'S2.png')), pygame.image.load(os.path.join('images', 'S2.png')), pygame.image.load(os.path.join('images', 'S2.png')), pygame.image.load(os.path.join('images', 'S2.png')), pygame.image.load(
        os.path.join('images', 'S2.png')), pygame.image.load(os.path.join('images', 'S2.png')), pygame.image.load(os.path.join('images', 'S2.png')), pygame.image.load(os.path.join('images', 'S3.png')), pygame.image.load(os.path.join('images', 'S4.png')), pygame.image.load(os.path.join('images', 'S5.png'))]
    # falling
    fall = pygame.image.load(os.path.join('images', '0.png'))  # NEW

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.jumping = False
        self.sliding = False
        self.falling = False  # NEW
        self.slideCount = 0
        self.slideCount = 0
        self.jumpCount = 0
        self.runCount = 0
        self.slideUp = False

    def draw(self, win):
        if self.falling:  # NEW
            win.blit(self.fall, (self.x, self.y + 30))  # NEW

        if self.jumping:
            self.y -= self.jumpList[self.jumpCount] * 1.2
            win.blit(self.jump[self.jumpCount//18], (self.x, self.y))
            self.jumpCount += 1
            if self.jumpCount > 108:
                self.jumpCount = 0
                self.jumping = False
                self.runCount = 0
            # Hitbox for character
            self.hitbox = (self.x + 4, self.y, self.width -
                           24, self.height-10)  # NEW
        elif self.sliding or self.slideUp:
            if self.slideCount < 20:
                self.y += 1
                # Hitbox for character
                self.hitbox = (self.x + 4, self.y, self.width -
                               24, self.height-10)  # NEW
            elif self.slideCount == 80:
                self.y -= 19
                self.sliding = False
                self.slideUp = True
            # Hitbox for character
            elif self.slideCount > 20 and self.slideCount < 80:  # NEW
                self.hitbox = (self.x, self.y+3, self.width -
                               8, self.height-35)  # NEW
            if self.slideCount >= 110:
                self.slideCount = 0
                self.slideUp = False
                # Hitbox for character
                self.hitbox = (self.x + 4, self.y, self.width -
                               24, self.height-10)  # NEW
                self.runCount = 0
            win.blit(self.slide[self.slideCount//10], (self.x, self.y))
            self.slideCount += 1

        else:
            if self.runCount > 42:
                self.runCount = 0
            win.blit(self.run[self.runCount//6], (self.x, self.y))
            self.runCount += 1
            # Hitbox for character
            self.hitbox = (self.x + 4, self.y, self.width -
                           24, self.height-13)  # NEW
        # NEW - Draws hitbox
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)


# obstacles
'''two main obstacles that our player needs to avoid. A saw and spike'''
# creating a class for our saw


class Saw(object):
    rotate = [pygame.image.load(os.path.join('images', 'SAW0.PNG')), pygame.image.load(os.path.join(
        'images', 'SAW1.PNG')), pygame.image.load(os.path.join('images', 'SAW2.PNG')), pygame.image.load(os.path.join('images', 'SAW3.PNG'))]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rotateCount = 0
        self.vel = 1.4

    def draw(self, win):
        # Defines the accurate hitbox for our character
        # self.hitbox = (self.x + 10, self.y + 5,
        #                self.width - 20, self.height - 5)
        # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
        self.hitbox = (self.x + 10, self.y + 5,
                       self.width - 20, self.height - 5)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 3)
        if self.rotateCount >= 8:  # This is what will allow us to animate the saw
            self.rotateCount = 0
        # scales our image down to 64x64 before drawing
        win.blit(pygame.transform.scale(
            self.rotate[self.rotateCount//2], (64, 64)), (self.x, self.y))
        self.rotateCount += 1
# we can code our spike class


# class Spike(Saw):
#     img = pygame.image.load(os.path.join('images', 'spike.png'))

#     def draw(self, win):
#         self.hitbox = (self.x + 10, self.y, 28, 315)  # defines the hitbox
#         pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
#         win.blit(self.img, (self.x, self.y))
class Spike(Saw):
    img = pygame.image.load(os.path.join('images', 'spike.png'))

    def draw(self, win):
        self.hitbox = (self.x + 10, self.y, 28, 315)  # defines the hitbox
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
        win.blit(self.img, (self.x, self.y))


# game loop
run = True
speed = 30
# call class player

runner = Player(200, 313, 64, 64)

'''We will store all of our objects in a list and loop through the list to draw each one.'''
obstacles = []

# drawing our chracter


def redrawWindow():
    win.blit(bg, (bgX, 0))  # draws our first bg image
    win.blit(bg, (bgX2, 0))  # draws the seconf bg image
    runner.draw(win)  # NEW
    # Loops through all obstacles

    # for obstacle in obstacles:

    #     obstacle.draw(win)
    # pygame.display.update()
    for obstacle in obstacles:
        obstacle.draw(win)
    
    pygame.display.update()


# change the background speed
pygame.time.set_timer(USEREVENT+1, 500)
'''Now that we have a list storing all of our obstacles we need to populate it. 
    We will need to create another timer event 
    so that each time it is triggered we generate a new obstacle'''
pygame.time.set_timer(USEREVENT+2, random.randrange(2000, 3500))

while run:
    redrawWindow()
    '''moving  the object obstacle This should go in the game loop'''
    for obstacle in obstacles:
        obstacle.x -= 1.4
        if obstacle.x < obstacle.width * -1:  # If our obstacle is off the screen we will remove it
            obstacles.pop(obstacles.index(obstacle))
    # set time clock
    clock.tick(speed)
    bgX -= 1.4
    bgX2 -= 1.4  # move both background images back

    if bgX < bg.get_width() * -1:
        bgX = bg.get_width()
    if bgX2 < bg.get_width() * -1:
        bgX2 = bg.get_width()
    for event in pygame.event.get():  # loop through a list of event
        if event.type == pygame.QUIT:  # See if the user clicks the red x
            run = False  # end the loop
            pygame.quit()  # quit the game
            quit()
        ''' This should go in the "for event in pygame.event.get():" loop'''
        if event.type == USEREVENT+2:
            r = random.randrange(0, 2)
            if r == 0:
                obstacles.append(Saw(810, 310, 64, 64))
            elif r == 1:
                obstacles.append(Spike(810, 0, 48, 310))

    # moving our characters
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
        if not(runner.jumping):
            runner.jumping = True
    if keys[pygame.K_DOWN]:
        if not(runner.sliding):
            runner.sliding = True
    clock.tick(speed)
