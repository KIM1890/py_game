import pygame
from pygame.locals import *
import os
import sys
import math
import random

pygame.init()

W, H = 800, 447
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption('Side Scroller')


bg = pygame.image.load(os.path.join('images', 'bg.png')).convert()
bgX = 0
bgX2 = bg.get_width()

clock = pygame.time.Clock()

# This should go above our game loop


class player(object):
    run = [pygame.image.load(os.path.join('images', str(x) + '.png'))
           for x in range(8, 16)]

    fall = pygame.image.load(os.path.join('images', '0.png'))
    jump = [pygame.image.load(os.path.join(
        'images', str(x) + '.png')) for x in range(1, 8)]
    slide = [pygame.image.load(os.path.join('images', 'S1.png')), pygame.image.load(os.path.join('images', 'S2.png')), pygame.image.load(os.path.join('images', 'S2.png')), pygame.image.load(os.path.join('images', 'S2.png')), pygame.image.load(os.path.join('images', 'S2.png')), pygame.image.load(
        os.path.join('images', 'S2.png')), pygame.image.load(os.path.join('images', 'S2.png')), pygame.image.load(os.path.join('images', 'S2.png')), pygame.image.load(os.path.join('images', 'S3.png')), pygame.image.load(os.path.join('images', 'S4.png')), pygame.image.load(os.path.join('images', 'S5.png'))]
    jumpList = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.jumping = False
        self.sliding = False
        self.falling = False  # new
        self.slideCount = 0
        self.jumpCount = 0
        self.runCount = 0
        self.slideUp = False

    def draw(self, win):
        if self.falling:
            screen.blit(self.fall, (self.x, self.y+30))
        elif self.jumping:
            self.y -= self.jumpList[self.jumpCount] * 1.2
            win.blit(self.jump[self.jumpCount//18], (self.x, self.y))
            self.jumpCount += 1
            if self.jumpCount > 108:
                self.jumpCount = 0
                self.jumping = False
                self.runCount = 0
            self.hitbox = (self.x + 4, self.y, self.width-24, self.height-10)
        elif self.sliding or self.slideUp:
            if self.slideCount < 20:
                self.y += 1
                self.hitbox = (self.x+4, self.y, self.width-24, self.height-10)
            elif self.slideCount == 80:
                self.y -= 19
                self.sliding = False
                self.slideUp = True
            # New elif statement
            elif self.slideCount > 20 and self.slideCount < 80:
                self.hitbox = (self.x, self.y+3, self.width-8, self.height-35)
            if self.slideCount >= 110:
                self.slideCount = 0
                self.slideUp = False
                self.hitbox = (self.x+4, self.y, self.width-24, self.height-10)
                self.runCount = 0
            win.blit(self.slide[self.slideCount//10], (self.x, self.y))
            self.slideCount += 1
        elif self.falling:
            screen.blit(fall, (self.x, self.y+30))

        else:
            if self.runCount > 42:
                self.runCount = 0
            win.blit(self.run[self.runCount//6], (self.x, self.y))
            self.runCount += 1
            self.hitbox = (self.x+4, self.y, self.width-24, self.height-13)
        pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)
# saw


class saw(object):
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
        self.hitbox = (self.x + 10, self.y + 5,
                       self.width - 20, self.height - 5)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
        if self.rotateCount >= 8:  # This is what will allow us to animate the saw
            self.rotateCount = 0
        # scales our image down to 64x64 before drawing
        win.blit(pygame.transform.scale(
            self.rotate[self.rotateCount//2], (64, 64)), (self.x, self.y))
        self.rotateCount += 1

    def collide(self, rect):
        if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            if rect[1] + rect[3] > self.hitbox[1]:
                return True
        return False
# spike


class spike(saw):  # We are inheriting from saw
    img = pygame.image.load(os.path.join('images', 'spike.png'))

    def draw(self, win):
        self.hitbox = (self.x + 10, self.y, 28, 315)  # defines the hitbox
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
        win.blit(self.img, (self.x, self.y))

    def collide(self, rect):
        if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            if rect[1] < self.hitbox[3]:
                return True
        return False


def updateFile():
    f = open('D:/to-do/py_game/bt3/scores.txt', 'r')
    file = f.readlines()
    last = int(file[0])

    if last < int(score):
        f.close()
        file = open('D:/to-do/py_game/bt3/scores.txt', 'w')
        file.write(str(score))
        file.close()

        return score

    return last


def endScreen():
    global pause, score, speed, obstacles
    pause = 0
    speed = 30
    obstacles = []

    run = True
    while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False
                runner.falling = False
                runner.sliding = False
                runner.jumpin = False

        screen.blit(bg, (0, 0))
        largeFont = pygame.font.SysFont('comicsans', 80)
        lastScore = largeFont.render(
            'Best Score: ' + str(updateFile()), 1, (255, 255, 255))
        currentScore = largeFont.render(
            'Score: ' + str(score), 1, (255, 255, 255))
        screen.blit(lastScore, (W/2 - lastScore.get_width()/2, 150))
        screen.blit(currentScore, (W/2 - currentScore.get_width()/2, 240))
        pygame.display.update()
    score = 0


runner = player(200, 313, 64, 64)

obstacles = []

# Should go above game loop


def redrawWindow():
    screen.blit(bg, (bgX, 0))  # draws our first bg image
    screen.blit(bg, (bgX2, 0))
    runner.draw(screen)  # draws the seconf bg image
    # loop through all obstacles
    for obstacle in obstacles:
        obstacle.draw(screen)
    pygame.display.update()  # updates the screen


run = True
speed = 30
fallSpeed = 0
pause = 0
pygame.time.set_timer(USEREVENT+1, 500)
pygame.time.set_timer(USEREVENT+2, 3000)
score = 0

while run:
    if pause > 0:
        pause += 1
        if pause > fallSpeed*2:
            endScreen()
    score = speed//10-3
    for obstacle in obstacles:

        obstacle.x -= 1.4
        # if obstacle.x < obstacle.width * -1:  # If our obstacle is off the screen we will remove it
        #     obstacles.pop(obstacles.index(obstacle))

        if obstacle.collide(runner.hitbox):
            runner.falling = True

            if pause == 0:
                pause = 1
                fallSpeed = speed
        if obstacle.x < -64:
            obstacles.pop(obstacles.index(obstacle))
        else:
            obstacle.x -= 1.4

    bgX -= 1.4
    bgX2 -= 1.4

    if bgX < bg.get_width() * -1:
        bgX = bg.get_width()

    if bgX2 < bg.get_width() * -1:
        bgX2 = bg.get_width()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()

        if event.type == USEREVENT+1:  # Checks if timer goes off
            speed += 1  # Increases speed

        if event.type == USEREVENT + 2:
            r = random.randrange(0, 2)
            if r == 0:
                obstacles.append(saw(810, 310, 64, 64))
            elif r == 1:
                obstacles.append(spike(810, 0, 48, 310))

    # Should go inside the game loop
    if runner.falling == False:
        keys = pygame.key.get_pressed()
       
        if keys[pygame.K_SPACE] or keys[pygame.K_UP]:  # If user hits space or up arrow key
            if not(runner.jumping):
                # If we are not already jumping
                runner.jumping = True

        if keys[pygame.K_DOWN]:  # If user hits down arrow key
            if not(runner.sliding):  # If we are not already sliding
                runner.sliding = True

    clock.tick(speed)
    redrawWindow()

