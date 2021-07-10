from test import HEIGHT, WIDTH
import pygame
import random
import os
from pygame import mixer
# khai báo biến
WIDTH = 500
HEIGHT = 600


class Bird:
    # khoi tao
    def __init__(self):
        pygame.init()  # Init pygame
        self.xScreen, self.yScreen = WIDTH, HEIGHT  # Screen create
        ''' Đường dẫn ảnh bird'''
        self.linkImgBird = os.path.join('data', 'bird.png')
        self.screen = pygame.display.set_mode(
            (self.xScreen, self.yScreen))  # Khởi tao kích thước màn hình
        pygame.display.set_caption("Flappybird")
        self.background = pygame.image.load(linkBackGround)
        self.gamerunning = True
        icon = pygame.image.load(self.linkImgBird)
        pygame.display.set_icon(icon)
        # --------------------------------------------------------
        self.xSizeBird = 80  # Chiều rong ảnh Bird
        self.ySizeBird = 60  # Chiều cao ảnh Bird
        self.xBird = self.screen/2  # Vị trí bạn đầu của bird
        self.yBird = self.screen/3   # Vi tri cua bird
        self.VBirdUp = 70  # Tốc độ nhảy bird
        self.VBirdDown = 7  # Tốc độ rớt bird
        # ------------------------------
        self.xColunm = self.screen  # khởi tạo cột đầu tiên
        self.yColunm = 0
        self.xSizeColunm = 100  # Chiều rộng cột
        self.ySizeColunm = 80
        self.Vcolunm = 6  # Tốc độ cột di chuyển
        self.colunmChange = 10

        self.scores = 0
        self.checkLost = False
    # function music

    def music(self, url):  # Âm thanh
        pass
    # function draw images

    def image_draw(self, url, xLocal, yLocal, xImg, yImg):  # In ra người hình ảnh
        PlanesImg = '''load img url'''
        PlanesImg = '''change size image'''
        self.screen.blit(PlanesImg, (xLocal, yLocal))
    # function display points

    def show_score(self, x, y, scores, size):
        # Hiển thị điểm
        pass
    # method column

    def colunm(self):
        pass
    # function run

    def run(self):
        while self.gamerunning:
            self.screen.blit(self.background, (0, 0))
            for event in pygame.event.get():  # Bắt các sự kiện
                if event.type == pygame .QUIT:  # sự kiện nhấn thoát
                    self.gamerunning = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.yBird -= self.VBirdUp  # Bird bay lên
                    self.music(os.path.join("data", "wet-click.wav"))
                if event.type == pygame.KEYDOWN:  # sự kiện có phím nhấn xuống
                    if event.key == pygame.K_SPACE:
                        self.yBird -= self.VBirdUp  # Bird bay lên
                        self.music(os.path.join("data", "wet-click.wav"))
            '''Bird rớt xuống'''
            yColunmChangeTop, yColunmChangeBotton = self.colunm()
            # ---------Check xem bird chạm cột----------------------------------
            if self.yBird < yColunmChangeTop and (self.xColunm+self.xSizeColunm - 5 > self.xBird+self.xSizeBird > self.xColunm + 5 or self.xColunm+self.xSizeColunm > self.xBird > self.xColunm):
                self.checkLost = True
            if self.yBird+self.ySizeBird > yColunmChangeBotton and (self.xColunm+self.xSizeColunm - 5 > self.xBird+self.xSizeBird > self.xColunm + 5 or self.xColunm+self.xSizeColunm > self.xBird > self.xColunm):
                self.checkLost = True
            # ---------Check xem bird có chạm tường-----------------------------
            '''Bird rơi nhanh dần'''
            while(self.checkLost):  # Nếu Bird chạm vật
                self.xColunm = self.xScreen+100
                for event in pygame.event.get():   # Nếu nhấn
                    if event.type == pygame.QUIT:  # Thoát
                        self.gamerunning = False
                        self.checkLost = False
                        break
                    if event.type == pygame.KEYDOWN:  # Thoát
                        self.checkLost = False
                        self.scores = 0
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.checkLost = False
                        self.scores = 0
                '''In điểm'''
                '''In Thông báo thua'''

                self.Vcolunm = 6
                self.VBirdDown = 7
                pygame.display.update()
            self.image_draw(self.linkImgBird, self.xBird,
                            self.yBird, self.xSizeBird, self.ySizeBird)
            self.show_score(self.xScreen - 200, 20,
                            "Do Thi Kim Lien", 15)
            self.show_score(10, 10, "Scores:{}".format(self.scores), 35)
            pygame.display.update()  # Update
            clock = pygame.time.Clock()
            clock.tick(80)


if __name__ == "__main__":
    bird = Bird()
    bird.run()
