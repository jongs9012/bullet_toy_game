import pygame
from random import randint

# 기본 변수 정의
player_x = 200
player_y = 200
width = 20
height = 20
time_ = 0
moveSpeed = 8
score = 0
player_life = 3

# 화면 크기 설정
size = (1280, 720)  # 1280 * 720
screen = pygame.display.set_mode(size)

# 버블 이미지
bubbleImg = pygame.image.load("images/bubble.PNG").convert()
bubbleImg = pygame.transform.scale(bubbleImg, (30, 30))

# 플레이어
playerImg = pygame.image.load("images/niddle.PNG").convert()
playerImg = pygame.transform.scale(playerImg, (30, 30))
player = screen.blit(playerImg, (player_x, player_y))

# Life 이미지
lifeImg = pygame.image.load("images/heart.png").convert()
lifeImg = pygame.transform.scale(lifeImg, (30, 30))

class Bullits:
    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y
        if diff(score)[1] == "Easy":
            speed = randint(-1, 1)
        elif diff(score)[1] == "Normal":
            speed = randint(-3, 3)
        elif diff(score)[1] == "Hard":
            speed = randint(-5, 5)
        if speed == 0:
            speed = 1
        self.x_speed = speed
        self.y_speed = speed
        self.crashed = 0

    def draw(self):
        self.bubble = screen.blit(bubbleImg, (self.pos_x, self.pos_y))

    def move(self):
        self.pos_x += self.x_speed
        self.pos_y += self.y_speed

    def wall_check(self):
        if self.pos_x + self.x_speed > 1280 - width or self.pos_x + self.x_speed < 0:
            self.x_speed = -self.x_speed
            self.crashed += 1
        if self.pos_y + self.y_speed > 720 - height or self.pos_y + self.y_speed < 0:
            self.y_speed = -self.y_speed
            self.crashed += 1

    def collision_check(self):
        if self.bubble.top < player.bottom and player.top < self.bubble.bottom and player.left < self.bubble.right and self.bubble.left < player.right:
            return True
        else:
            return False

    def remove_check(self):
        Curr_difficulty = diff(score)[1]
        print(Curr_difficulty)
        if self.crashed >= {Curr_difficulty == "Easy": 5, Curr_difficulty == "Normal": 4}.get(True, 3):
            return True
        elif self.crashed < {Curr_difficulty == "Easy": 5, Curr_difficulty == "Normal": 4}.get(True, 3):
            return False

    def check_all(self):
        self.move()
        self.draw()
        self.wall_check()
        if self.collision_check() and int(edit_life(0)) == 0:
            print("end")
            while True:  # 게임 오버
                pass

class Life:
    def __init__(self, pos_x, pos_y, level):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.level = level

    def draw(self):
        self.life = screen.blit(lifeImg, (self.pos_x, self.pos_y))

    # 부딛히면 True, 아닐시 False를 반환
    def collision_detection(self):
        if self.life.top < player.bottom and player.top < self.life.bottom and player.left < self.life.right and self.life.left < player.right:
            return True
        else:
            return False


# 난이도 리턴 함수
difficulty = {"easy": 100, "normal" : 50, "hard" : 20}
def diff(score):
    if score < 20:
        return difficulty["easy"], "Easy"
    elif 20 <= score < 50:
        return difficulty["normal"], "Normal"
    else:
        return difficulty["hard"], "Hard"



# 움직임 구현 함수 (방향키)
def move(li):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and li[0] > 0:
        li[0] -= moveSpeed

    if keys[pygame.K_RIGHT] and li[0] < 1280 - width :
        li[0] += moveSpeed

    if keys[pygame.K_UP] and li[1] > 0:
        li[1] -= moveSpeed

    if keys[pygame.K_DOWN] and li[1] < 720 - height:
        li[1] += moveSpeed
    return li[0], li[1]  # li[0]은 x좌표, li[1]은 y좌표

# 플레이어 함수
def print_player(x, y):
    global player
    currLocation = [x, y]
    player_x, player_y = move(currLocation)
    screen.blit(playerImg, (player_x, player_y))
    player = screen.blit(playerImg, (player_x, player_y))
    return player_x, player_y

def edit_life(level):
    global player_life
    player_life += level
    return player_life