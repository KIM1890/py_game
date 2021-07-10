import pygame
import random
import os
from pygame import mixer

# khai bao bien
WIDTH = 500
HEIGHT = 600
XSIZEBIRD = 80
YSIZEBIRD = 60
VBIRDUP = 70
VBIRDDOWN = 7
VCOLUMN = 6
SIZECOLUMN = 100
MAGINCOLUMN = 80
TITLE = "Flappybird"
linkBackGround = os.path.join(
    'data', 'background.jpg')  # Đường dẫn ảnh background
linkImgBird = os.path.join(
    "data", "bird.png")  # Đường dẫn ảnh bird
icon = pygame.image.load(linkImgBird)


class Bird:
    def __init__(self):
        pygame.init()  # Init pygame
        self.xScreen, self.yScreen = WIDTH, HEIGHT  # Screen create
        self.screen = pygame.display.set_mode(
            (self.xScreen, self.yScreen))  # Khởi tao kích thước màn hình
        pygame.display.set_caption(TITLE)
        self.background = pygame.image.load(linkBackGround)
        pygame.display.set_icon(icon)
        self.linkImgBird = linkImgBird
        self.gamerunning = True
        # --------------------------------------------------------
        self.xSizeBird = XSIZEBIRD  # Chiều cao ảnh Bird
        self.ySizeBird = YSIZEBIRD  # Chiều rộng ảnh Bird
        self.xBird = self.xScreen/3  # Vị trí bạn đầu của bird
        self.yBird = self.yScreen/2
        self.VBirdUp = VBIRDUP  # Tốc độ nhảy bird
        self.VBirdDown = VBIRDDOWN  # Tốc độ rớt bird
        # ------------------------------
        self.xColunm = self.yScreen+250  # khởi tạo cột đầu tiên
        self.yColunm = 0
        self.xSizeColunm = SIZECOLUMN  # Chiều rộng cột
        self.ySizeColunm = self.yScreen
        self.Vcolunm = VCOLUMN  # Tốc độ cột di chuyển
        self.colunmChange = 0

        self.scores = 0
        self.checkLost = False
    # function music

    def music(self, url):  # Âm thanh
        # bulletSound = mixer.Sound(url)
        # bulletSound.play()
    # function draw images

    def image_draw(self, url, xLocal, yLocal, xImg, yImg):  # In ra  hình ảnh
        # PlanesImg = pygame.image.load(url)
        # PlanesImg = pygame.transform.scale(
        #     PlanesImg, (xImg, yImg))  # change size image
        # self.screen.blit(PlanesImg, (xLocal, yLocal))
    # function display points

    def show_score(self, x, y, scores, size):  # Hiển thị điểm
        # font = pygame.font.SysFont("comicsansms", size)
        # score = font.render(str(scores), True, (255, 255, 255))
        # self.screen.blit(score, (x, y))
    # method column

    def colunm(self):
        maginColunm = MAGINCOLUMN
        yColunmChangeTop = -self.ySizeColunm/2 - maginColunm + \
            self.colunmChange   # Khoảng cách giữa cột trên và đưới là 80*2
        yColunmChangeBotton = self.ySizeColunm/2 + maginColunm+self.colunmChange
        self.image_draw(os.path.join("data", "colunm.png"), self.xColunm,
                        yColunmChangeTop, self.xSizeColunm, self.ySizeColunm)
        self.image_draw(os.path.join("data", "colunm.png"), self.xColunm,
                        yColunmChangeBotton, self.xSizeColunm, self.ySizeColunm)
        self.xColunm = self.xColunm - self.Vcolunm
        if self.xColunm < -100:  # Nếu cột đi qua màn hình
            self.xColunm = self.xScreen  # Tạo cột mới
            # Random khoảng cách cột
            self.colunmChange = random.randint(-150, 150)
            self.scores += 1
        return yColunmChangeTop+self.ySizeColunm, yColunmChangeBotton
    # function run

    def run(self):
        while self.gamerunning:
            self.screen.blit(self.background, (0, 0))
            for event in pygame.event.get():  # Bắt các sự kiện
                # print(event)
                if event.type == pygame .QUIT:  # sự kiện nhấn thoát
                    self.gamerunning = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.yBird -= self.VBirdUp  # Bird bay lên
                    self.music(os.path.join("data", "wet-click.wav"))
                if event.type == pygame.KEYDOWN:  # sự kiện có phím nhấn xuống
                    if event.key == pygame.K_SPACE:
                        self.yBird -= self.VBirdUp  # Bird bay lên
                        self.music(os.path.join("data", "wet-click.wav"))
            self.yBird += self.VBirdDown  # Bird rớt xuống
            yColunmChangeTop, yColunmChangeBotton = self.colunm()
            # print(self.yBird,yColunmChangeTop,self.yBird+self.ySizeBird, yColunmChangeBotton)
            # ---------Check xem bird chạm cột----------------------------------
            if self.yBird < yColunmChangeTop and (self.xColunm+self.xSizeColunm - 5 > self.xBird+self.xSizeBird > self.xColunm + 5 or self.xColunm+self.xSizeColunm > self.xBird > self.xColunm):
                self.checkLost = True
            if self.yBird+self.ySizeBird > yColunmChangeBotton and (self.xColunm+self.xSizeColunm - 5 > self.xBird+self.xSizeBird > self.xColunm + 5 or self.xColunm+self.xSizeColunm > self.xBird > self.xColunm):
                self.checkLost = True
            # ---------Check xem bird có chạm tường-----------------------------
            if (self.yBird + self.ySizeBird > self.yScreen) or self.yBird < 0:
                self.yBird = self.yScreen/2
                self.checkLost = True
            self.Vcolunm = 6 if self.scores < 1 else 6 + self.scores/5  # Tốc độ tăng dần
            self.VBirdDown = 7 if self.scores < 1 else 7 + \
                self.scores/10  # Bird rơi nhanh dần
            # print(self.Vcolunm)
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
                self.show_score(100, 100, "Scores:{}".format(
                    self.scores), 40)  # In điểm
                self.show_score(self.xScreen/2-100, self.yScreen /
                                2-100, "GAME OVER", 50)  # In Thông báo thua
                self.Vcolunm = 6
                self.VBirdDown = 7
                pygame.display.update()
            self.image_draw(self.linkImgBird, self.xBird,
                            self.yBird, self.xSizeBird, self.ySizeBird)
            self.show_score(self.xScreen - 200, 20,
                            "kimliendo1890@gmail.com", 15)
            self.show_score(10, 10, "Scores:{}".format(self.scores), 35)
            pygame.display.update()  # Update
            clock = pygame.time.Clock()
            clock.tick(80)


if __name__ == "__main__":
    bird = Bird()
    bird.run()
