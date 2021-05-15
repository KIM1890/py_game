# 1.import thu vien cần thiết
import pygame
# 2.định nghĩa hằng số trong game
''' FPS ( Frames – per – second) 
toc do khung hinh Đó là tần số xuất hiện 
các khung hình riêng lẻ 
mà máy ảnh của bạn chụp trong một giây'''

# 3.khởi tạo cửa sổ game #

# 4.set tên cho chương trình game

# 5.Kích thước cửa sổ


# 6.khởi tạo bộ đếm thời gian

## 7. Tạo vòng lặp game ##

running = True

while running:
    # 8. thiet lap toc do cua bo dem thoi gian(FPS)
    '''bộ điếm thời gian giúp chúng ra điều khiển
    được tốc độ lặp của một vòng lặp'''
    # 9. thoat game(xu ly su kien thoat game)
    # Du lieu tu nguoi choi
    '''Bằng việc là lấy các sự kiện mà người chơi
    tác động vào trò chơi như nhấp phím space hay click
    trái chuột'''
    # Cap nhat thong so cua game
    '''Cập nhật tọa độ, tốc độ của nhân vật 
    và điểm số người chơi đang đạt được,..'''
    # Ve cac doi tuong ra man hinh game
    '''Vẽ tất cả nhân vật ra ngoài cửa sổ game'''
    pygame.display.flip()

pygame.quit()
