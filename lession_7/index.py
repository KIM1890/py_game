from typing import Mapping
import pygame
import random


colors = [
    (0, 0, 0),
    (120, 37, 179),
    (100, 179, 179),
    (80, 34, 22),
    (80, 134, 22),
    (180, 34, 22),
    (180, 34, 122),
]


class Figure:
    x = 0
    y = 0

    figures = [
        [[1, 5, 9, 13], [4, 5, 6, 7]],
        [[4, 5, 9, 10], [2, 6, 5, 9]],
        [[6, 7, 9, 10], [1, 5, 6, 10]],
        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
        [[1, 2, 5, 6]],
    ]

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = random.randint(0, len(self.figures) - 1)
        self.color = random.randint(1, len(colors) - 1)
        self.rotation = 0

    def image(self):
        return self.figures[self.type][self.rotation]
    # self.rotation = (self.rotation + 1) % len(self.figures[self.type])

    def rotate(self):
        self.rotation = (self.rotation+1) % len(self.figures[self.type])


class Tetris:
    level = 2
    score = 0
    state = "start"  # chúng ta có tiếp tục chơi game hay không
    field = []  # Là một trường của game chứa rỗng,0, các màu có các hình
    height = 0
    width = 0
    x = 100
    y = 60
    zoom = 20
    figure = None

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.field = []
        self.score = 0
        self.state = "start"
        # create field với kích thước là (height x width)
        for i in range(height):
            new_line = []
            for j in range(width):
                new_line.append(0)
            self.field.append(new_line)
    # tạo ra một figure và tại vị trí tọa độ(3,0)

    def new_figure(self):
        self.figure = Figure(3, 0)
    '''intersection =False nghĩa là figure còn lơ lửng ngược lại thì
    chúng đã chạm đáy và các figure khác'''

    def intersects(self):
        intersection = False
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    if i + self.figure.y > self.height - 1 or \
                            j + self.figure.x > self.width - 1 or \
                            j + self.figure.x < 0 or \
                            self.field[i + self.figure.y][j + self.figure.x] > 0:
                        intersection = True
        print(intersection)
        return intersection
    '''Nếu khối hình xếp đầy thành một hàng ngang thì
    người chơi sẽ được ghi điểm
    và đồng thời hàng ngang đó sẽ biến mất'''

    def break_lines(self):
        lines = 0
        for i in range(1, self.height):
            zeros = 0
            for j in range(self.width):
                if self.field[i][j] == 0:
                    zeros += 1
            if zeros == 0:
                lines += 1
                for i1 in range(i, 1, -1):
                    for j in range(self.width):
                        self.field[i1][j] = self.field[i1 - 1][j]
        self.score += lines ** 2

    def go_space(self):
        while not self.intersects():
            self.figure.y += 1
        self.figure.y -= 1
        self.freeze()

    def go_down(self):
        self.figure.y += 1
        if self.intersects():
            self.figure.y -= 1
            self.freeze()

    '''Có tác dụng cố định vị trí các
    figure khi các figure chạm vào các figure khác.
    có thể dùng hàm break_lines và new figure đê hủy một hàng
    '''

    def freeze(self):
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    self.field[i + self.figure.y][j +
                                                  self.figure.x] = self.figure.color
        self.break_lines()
        self.new_figure()
        if self.intersects():
            self.state = "gameover"

    def go_side(self, dx):
        old_x = self.figure.x
        self.figure.x += dx
        if self.intersects():
            self.figure.x = old_x

    def rotate(self):
        old_rotation = self.figure.rotation
        self.figure.rotate()
        if self.intersects():
            self.figure.rotation = old_rotation


def main():
    # Initialize the game engine
    pygame.init()

    # Define some colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (128, 128, 128)

    SIZE = (400, 500)

    # Lặp cho đến khi người dùng nhấn tắt cái button trên video game.
    done = False
    clock = pygame.time.Clock()
    fps = 25
    counter = 0
    # Thiết lập kích thước cho cửa sổ video game
    screen = pygame.display.set_mode(SIZE)
    # Đặt tên cho chương trình game
    pygame.display.set_caption("Tetris")

    ''' gọi class Tetris(20,10)'''
    game = Tetris(20, 10)
    pressing_down = False

    while not done:

        '''Điều kiện figure là None thì sẽ tạo ra một new_figure mới'''
        counter += 1
        if counter > 100000:
            counter = 0
        if counter % (fps // game.level // 2) == 0 or pressing_down:
            if game.state == "start":
                game.go_down()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    '''game sẽ rotate'''
                    game.rotate()

                if event.key == pygame.K_DOWN:
                    pressing_down = True
                if event.key == pygame.K_LEFT:
                    '''game sẽ go side về trái(-1)'''
                    game.go_side(-1)
                if event.key == pygame.K_RIGHT:
                    '''game sẽ go side về trái(-1)'''
                    game.go_side(1)
                if event.key == pygame.K_SPACE:
                    game.go_space()
                if event.key == pygame.K_ESCAPE:
                    '''bắt đầu lại video game init(20,10)'''
                    game.__init__(20, 10)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                pressing_down = False

        screen.fill(WHITE)
        # for i in range(game.height):
        #     for j in range(game.width):
        #         pygame.draw.rect(screen, GRAY, [
        #                          game.x + game.zoom * j, game.y + game.zoom * i, game.zoom, game.zoom], 1)
        #         if game.field[i][j] > 0:
        #             pygame.draw.rect(screen, colors[game.field[i][j]],
        #                              [game.x + game.zoom * j + 1, game.y + game.zoom * i + 1, game.zoom - 2, game.zoom - 1])

        # if game.figure is not None:
        #     for i in range(4):
        #         for j in range(4):
        #             p = i * 4 + j
        #             if p in game.figure.image():
        #                 pygame.draw.rect(screen, colors[game.figure.color],
        #                                  [game.x + game.zoom * (j + game.figure.x) + 1,
        #                                  game.y + game.zoom *
        #                                      (i + game.figure.y) + 1,
        #                                  game.zoom - 2, game.zoom - 2])
        font = pygame.font.SysFont('Calibri', 25, True, False)
        font1 = pygame.font.SysFont('Calibri', 65, True, False)
        text_game_over = font1.render("Game Over", True, (255, 125, 0))
        text_game_over1 = font1.render("Press ESC", True, (255, 215, 0))

        # screen.blit(text, [0, 0])
        # if game.state == "gameover":
        #     screen.blit(text_game_over, [20, 200])
        #     screen.blit(text_game_over1, [25, 265])
        '''cập nhật tất cả lên video '''
        pygame.display.update()
        # Thời gian xuất hiện của khung hình trong một giây
        clock.tick(fps)


if __name__ == '__main__':
    main()
pygame.quit()
