# 1.import thu vien cần thiết
import pygame
import random
# 2.định nghĩa hằng số trong game
''' FPS ( Frames – per – second) 
toc do khung hinh Đó là tần số xuất hiện 
các khung hình riêng lẻ 
mà máy ảnh của bạn chụp trong một giây'''
WIDTH = 500
HEIGHT = 500
FPS = 24

# 3.khởi tạo cửa sổ game #
pygame.init()

# khởi tạo âm thanh(phát tệp âm thanh)
pygame.mixer.init()

# 4.set tên cho chương trình game
pygame.display.set_caption('Drawing')

# 5.set Kích thước cửa sổ
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# 6.khởi tạo bộ đếm thời gian
clock = pygame.time.Clock()

## 7. Tạo vòng lặp game ##
running = True
while running:

    # 8. thiet lap toc do cua bo dem thoi gian(FPS)
    '''bộ đem thời gian giúp chúng ra điều khiển
    được tốc độ lặp của một vòng lặp'''
    clock.tick(FPS)
    # 9. thoat game(xu ly su kien thoat game)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Du lieu tu nguoi choi
    '''Bằng việc là lấy các sự kiện mà người chơi
        tác động vào trò chơi như nhấp phím space hay click
        trái chuột'''
    # Cap nhat thong so cua game
    '''Cập nhật tọa độ, tốc độ của nhân vật 
        và điểm số người chơi đang đạt được,..'''
    # Ve cac doi tuong ra man hinh game

    '''Vẽ tất cả nhân vật ra ngoài cửa sổ game'''
    # Vẽ các hình ra ngoài cửa sổ game
    # hình chữ nhật
    pygame.draw.rect(screen, (102, 204, 255), pygame.Rect(50, 50, 60, 60))
    # hình tròn
    pygame.draw.circle(screen, (204, 51, 0), (150, 150), 75)
    # shift+ alt+f format code in vscode


    # cập nhật thông tin lập trình trên cửa sổ
    pygame.display.flip()

pygame.quit()
