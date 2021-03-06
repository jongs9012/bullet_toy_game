import pygame
from gameObjects import Bullits, diff, score, time_, print_player, player_y, player_x, Life, edit_life
from random import randint
from time import sleep
pygame.init()

# 화면 크기 설정
size = (1280, 720)  # 1280 * 720
screen = pygame.display.set_mode(size)




# 색상 정의
BLACK = (0, 0, 0)
GRAY = (20, 20, 20)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


# 게임 제목 설정
pygame.display.set_caption("Avoid the Bullets")

# 폰트 설정
myFont = pygame.font.SysFont("Bahnschrift", 15, bold=True)


# 프레임을 정하기 위한 변수
clock = pygame.time.Clock()

# 객체를 담을 리스트
objects = []
life = []
spawn_score = []
# 게임 실행 루프
while True:
    # 초당 120프레임
    clock.tick(120)
    screen.fill(GRAY)
    # 입력받은 키에 종료키가 있다면 break 함
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # QUIT이벤트는 창에서 X버튼
            done = True

    scoretext = myFont.render("Score = " + str(score), True, WHITE)
    difftext = myFont.render("Difficulty = " + str(diff(score)[1]), True, WHITE)
    lifetext = myFont.render(f"Life = {edit_life(0)}", True, WHITE)

    screen.blit(scoretext, (10, 10))
    screen.blit(difftext, (10, 30))
    screen.blit(lifetext, (10, 50))


    # 일정 시간마다 오브젝트관리
    if time_ >= diff(score)[0]:
        # Life 오브젝트 관리
        if score == 0 or len(spawn_score) >= 10:
            pass
        else:
            spawn_score.append(int(2 ** score))

        if score in spawn_score:
            life_ = Life(randint(0, 1280), randint(0, 720), randint(1, 4))
            life.append(life_)

        # 총알 관리
        object_ = Bullits(randint(0, 1280), 5)
        objects.append(object_)
        time_ = 0
        score += 1
    time_ += 1

    for j, k in enumerate(objects):
        if k.remove_check():
            objects.pop(j)
        if k.check_all():
            edit_life(-1)
            print("Finished")
            objects = []


    for j, k in enumerate(life):
        k.draw()
        if k.collision_detection():
            edit_life(k.level)
            del life[j]

    player_x, player_y = print_player(player_x, player_y)

    if edit_life(0) < 0:
        while True:
            pass

    # 화면을 업데이트 해주는 함수
    pygame.display.flip()  # 없으면 화면이 그려지지 않음

pygame.quit()
