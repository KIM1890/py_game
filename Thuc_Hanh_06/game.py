import pygame
import random
import os

from pygame import mixer


class Bird:
    def __init__(self):
        pygame.init()  # Init pygame
        self.xScreen, self.yScreen = 500, 600  # Screen create
        linkBackGround = os.path.join(
            'data', 'background.jpg')  # Đường dẫn ảnh background
        self.linkImgBird = os.path.join(
            "data", "bird.png")  # Đường dẫn ảnh bird
        self.screen = pygame.display.set_mode(
            (self.xScreen, self.yScreen))  # Khởi tao kích thước màn hình
        pygame.display.set_caption("Flappybird")
        self.background = pygame.image.load(linkBackGround)
        self.gamerunning = True
        icon = pygame.image.load(self.linkImgBird)
        pygame.display.set_icon(icon)
        # --------------------------------------------------------
        self.xSizeBird = 80  # Chiều cao ảnh Bird
        self.ySizeBird = 60  # Chiều rộng ảnh Bird
        self.xBird = self.xScreen/3  # Vị trí bạn đầu của bird
        self.yBird = self.yScreen/2
        self.VBirdUp = 70  # Tốc độ nhảy bird
        self.VBirdDown = 7  # Tốc độ rớt bird
        # ------------------------------
        self.xColunm = self.yScreen+250  # khởi tạo cột đầu tiên
        self.yColunm = 0
        self.xSizeColunm = 100  # Chiều rộng cột
        self.ySizeColunm = self.yScreen
        self.Vcolunm = 6  # Tốc độ cột di chuyển
        self.colunmChange = 0

        self.scores = 0
        self.checkLost = False
    # function music

    def music(self, url):  # Âm thanh
        bulletSound = mixer.Sound(url)
        bulletSound.play()

    # function draw images

    def image_draw(self, url, xLocal, yLocal, xImg, yImg):  # In ra người hình ảnh
        PlanesImg = pygame.image.load(url)
        PlanesImg = pygame.transform.scale(PlanesImg, (xImg, yImg))
        self.screen.blit(PlanesImg, (xLocal, yLocal))

        # function display points

    def show_score(self, x, y, scores, size):  # Hiển thị điểm
        font = pygame.font.SysFont("comicsansms", size)
        score = font.render(str(scores), True, (255, 51, 0))
        self.screen.blit(score, (x, y))

    # method column

    def colunm(self):
        maginColumn = 80
        yColumnChangeTop = -self.ySizeColunm/2 - maginColumn + self.colunmChange
        yColumnChangeBotton = self.ySizeColunm/2 + maginColumn + self.colunmChange
        self.image_draw(os.path.join('data', 'colunm.png'), self.xColunm,
                        yColumnChangeTop, self.xSizeColunm, self.ySizeColunm)
        self.image_draw(os.path.join('data', 'colunm.png'), self.xColunm,
                        yColumnChangeBotton, self.xSizeColunm, self.ySizeColunm)

        self.xColunm = self.xColunm - self.Vcolunm
        if self.xColunm < -100:
            self.xColunm = self.xScreen
            # random khoang cach giua cac cot
            self.colunmChange = random.randint(-150, 150)
            self.scores += 1

        return yColumnChangeTop+self.ySizeColunm, yColumnChangeBotton

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
