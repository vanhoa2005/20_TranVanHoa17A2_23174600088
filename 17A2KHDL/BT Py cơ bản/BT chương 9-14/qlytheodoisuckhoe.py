import pygame
import sys
import random
import math
from pygame.locals import *
import time
# Khởi động Pygame
pygame.init()


# Các hằng số
WINDOWWIDTH = 800
WINDOWHEIGHT = 835
FPS = 60
SIZE = 2.2  # Kích thước viên đạn nổ ra
SPEED_CHANGE_SIZE = 0.05  # Tốc độ nhỏ lại của viên đạn khi nổ ra
CHANGE_SPEED = 0.07  # Tốc độ chậm lại của viên đạn
RAD = math.pi / 180  # Đỏi từ radian sang độ
A_FALL = 1.5  # Gia tốc rơi tự do
NUM_BULLET = 100  # Số đạn nổ ra trong 1 quả pháo
SPEED_MIN = 2  # Tốc độ nhỏ nhất của 1 viên đạn
SPEED_MAX = 4  # Tốc độ lớn nhất của một viên đạn
TIME_CREAT_FW = 40  # Khoảng thời gian liên tiếp giữa 2 lần bắn
NUM_FIREWORKS_MAX = 10  # Số lượng pháo lớn nhất bắn lên
NUM_FIREWORKS_MIN = 2  # Số lượng pháo nhỏ nhất bắn lên
SPEED_FLY_UP_MAX = 15  # Tốc độ lớn nhất của viên đạn bay lên (trước khi nổ)
SPEED_FLY_UP_MIN = 8  # Tốc độ nhỏ nhất của viên đạn bay lên (trước khi nổ)


ĐEN = (0, 0, 0)
TRẮNG = (255, 255, 255)
FONT_SIZE = 36


class Dot():
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color


    def update(self):
        if self.size > 0:
            self.size -= SPEED_CHANGE_SIZE * 5
        else:
            self.size = 0


    def draw(self):
        if self.size > 0:
            pygame.draw.circle(DISPLAYSURF, self.color, (int(self.x), int(self.y)), int(self.size))


class BulletFlyUp():
    def __init__(self, speed, x):
        self.speed = speed
        self.x = x
        self.y = WINDOWHEIGHT
        self.dots = []
        self.size = SIZE / 2
        self.color = (255, 255, 100)


    def update(self):
        self.dots.append(Dot(self.x, self.y, self.size, self.color))
        self.y -= self.speed
        self.speed -= A_FALL * 0.1
        for dot in self.dots:
            dot.update()
        for dot in self.dots:
            if dot.size <= 0:
                self.dots.pop(self.dots.index(dot))


    def draw(self):
        pygame.draw.circle(DISPLAYSURF, self.color, (int(self.x), int(self.y)), int(self.size))
        for dot in self.dots:
            dot.draw()


class Bullet():
    def __init__(self, x, y, speed, angle, color):
        self.x = x
        self.y = y
        self.speed = speed
        self.angle = angle
        self.size = SIZE
        self.color = color


    def update(self):
        speedX = self.speed * math.cos(self.angle * RAD)
        speedY = self.speed * -math.sin(self.angle * RAD)
        self.x += speedX
        self.y += speedY
        self.y += A_FALL
        if self.size > 0:
            self.size -= SPEED_CHANGE_SIZE
        else:
            self.size = 0
        if self.speed > 0:
            self.speed -= CHANGE_SPEED
        else:
            self.speed = 0


    def draw(self):
        if self.size > 0:
            pygame.draw.circle(DISPLAYSURF, self.color, (int(self.x), int(self.y)), int(self.size))


class FireWork():
    def __init__(self, x, y):
        self.x = x
        self.y = y -180
        self.dots = []
        self.bullets = []


        def create_bullets():
            bullets = []
            color = Random.color()
            for i in range(NUM_BULLET):
                angle = (300 / NUM_BULLET) * i
                speed = random.uniform(SPEED_MIN, SPEED_MAX)
                bullets.append(Bullet(self.x, self.y, speed, angle, color))
            return bullets


        self.bullets = create_bullets()


    def update(self):
        for bullet in self.bullets:
            bullet.update()
            self.dots.append(Dot(bullet.x, bullet.y, bullet.size, bullet.color))
        for dot in self.dots:
            dot.update()
        for dot in self.dots:
            if dot.size <= 0:
                self.dots.pop(self.dots.index(dot))


    def draw(self):
        for bullet in self.bullets:
            bullet.draw()
        for dot in self.dots:
            dot.draw()


class Random():
    def __init__(self):
        pass


    @staticmethod
    def color():
        color1 = random.randint(0, 255)
        color2 = random.randint(0, 255)
        if color1 + color2 >= 255:
            color3 = random.randint(0, 255)
        else:
            color3 = random.randint(255 - color1 - color2, 255)
        color_list = [color1, color2, color3]
        random.shuffle(color_list)
        return color_list


    @staticmethod
    def num_fireworks():
        return random.randint(NUM_FIREWORKS_MIN, NUM_FIREWORKS_MAX)


    @staticmethod
    def random_bullet_fly_up_speed():
        speed = random.uniform(SPEED_FLY_UP_MIN, SPEED_FLY_UP_MAX)
        return speed


    @staticmethod
    def random_bullet_fly_up_x():
        x = random.randint(int(WINDOWWIDTH * 0.2), int(WINDOWHEIGHT * 0.8))
        return x


def main():# Tạo màn hình
    import time as timer_module
    global FPSCLOCK, DISPLAYSURF
    màn_hình = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption("Mô phỏng pháo hoa")
    đồng_hồ = pygame.time.Clock()
    fire_works = []
    time = TIME_CREAT_FW
    bullet_fly_ups = []
    thời_gian_bắt_đầu = timer_module.time()
    đếm_ngược_start_time = thời_gian_bắt_đầu
    new_year_display_time = thời_gian_bắt_đầu + 10  # Hiển thị "CHÚC MỪNG NĂM MỚI! " sau 10 giây
    pháo_hoa_start_time = thời_gian_bắt_đầu + 5  # Bắt_tiếp_pháo_hoa sau 5 giây
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.mixer.init()
    explosion_sound = pygame.mixer.Sound("boom_sound.ogg")  
    while True:
            DISPLAYSURF.fill((0, 0, 0))


            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
            màn_hình.fill(ĐEN)
            # Đếm ngược từ 10 đến 1
            thời_gian_hiện_tại = timer_module.time()
            đếm_ngược = 5 - int(thời_gian_hiện_tại - đếm_ngược_start_time)
            if đếm_ngược > 0:
                phông_chữ = pygame.font.Font(None, FONT_SIZE)
                văn_bản = phông_chữ.render(str(đếm_ngược), True, TRẮNG)
                text_rect = văn_bản.get_rect(center=(WINDOWWIDTH // 2, WINDOWHEIGHT // 2))
                màn_hình.blit(văn_bản, text_rect)
            else:
                # Hiển thị "CHÚC MỪNG NĂM MỚI! " sau 10 giây
                if thời_gian_hiện_tại >= new_year_display_time:
                    phông_chữ = pygame.font.Font(None, FONT_SIZE)
                    văn_bản = phông_chữ.render("chúc mừng năm mới 2024! ", True, TRẮNG)
                    text_rect = văn_bản.get_rect(center=(WINDOWWIDTH // 2, WINDOWHEIGHT // 2))
                    màn_hình.blit(văn_bản, text_rect)
            if thời_gian_hiện_tại >= pháo_hoa_start_time:


                for fire_work in fire_works:
                    if fire_work.bullets[0].size <= 0:
                        fire_works.pop(fire_works.index(fire_work))
                        # Phát âm thanh mỗi khi một quả pháo hoa nổ
                        explosion_sound.play()
                if time == TIME_CREAT_FW:
                    for i in range(Random.num_fireworks()):
                        bullet_fly_ups.append(BulletFlyUp(Random.random_bullet_fly_up_speed(), Random.random_bullet_fly_up_x()))


                for bullet_fly_up in bullet_fly_ups:
                    bullet_fly_up.draw()
                    bullet_fly_up.update()


                for fire_work in fire_works:
                    fire_work.draw()
                    fire_work.update()


                for bullet_fly_up in bullet_fly_ups:
                    if bullet_fly_up.speed <= 0:
                        fire_works.append(FireWork(bullet_fly_up.x, bullet_fly_up.y))
                        bullet_fly_ups.pop(bullet_fly_ups.index(bullet_fly_up))
                
            
            


                if time <= TIME_CREAT_FW:
                    time += 1
                else:
                    time = 0


            pygame.display.update()
            FPSCLOCK.tick(FPS)


if __name__ == '__main__':
    main()
