import pgzrun
from random import randint          # randint means 랜덤한 숫자를 import

timer = 30


apple = Actor("apple")
goldapple = Actor("gold_apple")

apple_draw = randint(1, 2)         # (1,10) means it's 10분의 1 확률 for the golden apple to spawn

def draw():                     # draw -> 이미 있는 함수
    screen.clear()

    if(apple_draw == 1):
        goldapple.draw()
    else:
        apple.draw()                # 항상 위치 지정을 안하면 0,0, 왼쪽 위로 간다.

    screen.draw.text(str(round(timer,2)), topleft=(10,10), color=(255,255,193), fontsize=30)        
    # (round(timer,2)) means rounding the numbers to the 2nd 소수점 자리
    


def place_apple():
    apple.x = randint(10, 800)          # randint(10,800) means 좌표 10부터 800 까지 랜덤하게 좌표가 나오는것
    apple.y = randint(10,600)


def place_goldapple():
    goldapple.x = randint(10, 800)
    goldapple.y = randint(10, 600)


def draw_apple():
    global apple_draw

    apple_draw = randint(1, 10)         # (1,10) means it's 10분의 1 확률 for the golden apple to spawn
    

def on_mouse_down(pos):         # 마우스 클릭 이벤트
    if apple.collidepoint(pos):     # collidepoint means 사과를 클릭했을때. 
                                    # (pos) means position of cursor, so 커서가 사과를 클릭했을때를 표현한 코드
        print("Good shot!")
        place_apple()
        draw_apple()
    elif goldapple.collidepoint(pos):
        print("Very good shot!")
        place_goldapple()
        draw_apple()
    else:
        print("You missed!")
        quit()                      # quit() means 강제로 게임을 종료하는거


def update():
    global timer

    timer -= 1/60

    if(timer < 0):
        quit()


place_apple()           # 실행을 해야지 코드가 먹힌다.


pgzrun.go()