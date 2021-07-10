import pygame

# Định nghĩa một hằng về màu sắc
WHITE = (255, 255, 255)


# class Car(pygame.sprite.Sprite):
#     def __init__(self, color, width, height):
class Car(pygame.sprite.Sprite):
    def __init__(self, color, width, height):

        # khoi tao
        super().__init__()

        # khoi tao chieu cao, chieu rong
        # thiet lap mau nen
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        # co the thay the hinh oto bang 1 hinh anh car.png
        # self.image = pygame.image.load('car.png').convert_alpha()

        # ve o to bang hinh chu nhat
        pygame.draw.rect(self.image, color,[0,0, width,height])

        self.rect = self.image.get_rect()
    def moveRight(self,pixels):
        self.rect.x += pixels

    def moveLeft(self,pixels):
        self.rect.x -= pixels
