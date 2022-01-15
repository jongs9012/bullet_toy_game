import random

import pygame
from random import randint, randrange
pygame.init()

# 색상 정의
BLACK = (0, 0, 0)
GRAY = (20, 20, 20)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# 화면 크기 설정
size = (1280, 720)  # 1280 * 720
screen = pygame.display.set_mode(size)

# 게임 제목 설정
pygame.display.set_caption("Avoid the Bullets")

# 프레임을 정하기 위한 변수
clock = pygame.time.Clock()

player_x = 200
player_y = 200
width = 20
height = 20
time_ = 0
moveSpeed = 5


class Bullits:
    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y
        self.x_speed = random.uniform(-5, 5)
        self.y_speed = random.uniform(-5, 5)
        self.crached = 0

    def draw(self):
        self.rect = pygame.draw.rect(screen, GREEN, (self.pos_x, self.pos_y, width, height))

    def move(self):
        self.pos_x += self.x_speed
        self.pos_y += self.y_speed

    def wall_check(self):
        if self.pos_x + self.x_speed > 1280 - width or self.pos_x + self.x_speed < height:
            self.x_speed = -self.x_speed
        if self.pos_y + self.y_speed > 720 - width or self.pos_y + self.y_speed < height:
            self.y_speed = -self.y_speed
            self.crashed += 1

    def collision_check(self):
        if self.rect.top < player.bottom and player.top < self.rect.bottom and player.left < self.rect.right and self.rect.left < player.right:
            return True
        else:
            return False

    def check_all(self):
        self.draw()
        self.move()
        self.wall_check()
        if self.collision_check():
            while True:
                pass

objects = []
onGame = True
done = False

# 움직임 구현 함수 (방향키)
def move(li):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and li[0] > 0:
        li[0] -= moveSpeed

    if keys[pygame.K_RIGHT] and li[0] < 1280 - height :
        li[0] += moveSpeed

    if keys[pygame.K_UP] and li[1] > 0:
        li[1] -= moveSpeed

    if keys[pygame.K_DOWN] and li[1] < 720 - width:
        li[1] += moveSpeed
    return li[0], li[1]  # li[0]은 x좌표, li[1]은 y좌표


# 게임 실행 루프
while not done:
    # 초당 120프레임
    clock.tick(120)
    screen.fill(GRAY)
    # 입력받은 키에 종료키가 있다면 break 함
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # QUIT이벤트는 창에서 X버튼
            done = True


    if time_ >= 100:
        object_ = Bullits(randint(0, 1280), 20)
        objects.append(object_)
        time_ = 0
    time_ += 1

    for j in objects:
        j.check_all()

    currLocation = [player_x, player_y]
    player_x, player_y = move(currLocation)

    player = pygame.draw.rect(screen, RED, (player_x, player_y, width, height))

    # 화면을 업데이트 해주는 함수
    pygame.display.flip()  # 없으면 화면이 그려지지 않음

pygame.quit()
